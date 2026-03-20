from typing import List, Optional
from pydantic import BaseModel


class FileNode(BaseModel):
    path: str
    name: str
    type: str
    size: int
    modified_at: float


class MetadataRecord(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    category: Optional[str] = None
    updated_at: Optional[str] = None


class FileContent(BaseModel):
    path: str
    content: str
    type: str
    size: int
    metadata: Optional[MetadataRecord] = None


class MetadataPayload(BaseModel):
    path: str
    title: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    category: Optional[str] = None


class SearchResult(BaseModel):
    path: str
    name: str
    type: str
    snippet: Optional[str] = None
    score: float


class StatusResponse(BaseModel):
    status: str
    path: Optional[str] = None
    count: Optional[int] = None
    framework_root: Optional[str] = None


class AgentQueryRequest(BaseModel):
    query: str
    scope: Optional[str] = None
    max_results: Optional[int] = 20


class AgentQueryResponse(BaseModel):
    results: List[SearchResult]
