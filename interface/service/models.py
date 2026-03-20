from datetime import datetime, timezone
from typing import List, Optional

from sqlalchemy import Column, JSON
from sqlmodel import SQLModel, Field


class FileMetadata(SQLModel, table=True):
    path: str = Field(primary_key=True, index=True)
    title: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    category: Optional[str] = None
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
