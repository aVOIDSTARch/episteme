from typing import List, Optional
from pydantic import BaseModel, Field


class FileNode(BaseModel):
    path: str = Field(description="Repo-relative path under episteme-framework")
    name: str = Field(description="File or directory name")
    type: str = Field(description="Node type: 'file' or 'dir'")
    size: int = Field(description="Size in bytes")
    modified_at: float = Field(description="Last modified timestamp (unix epoch)")


class MetadataRecord(BaseModel):
    title: Optional[str] = Field(default=None, description="Human-readable title")
    description: Optional[str] = Field(default=None, description="Short description")
    tags: Optional[List[str]] = Field(default=None, description="Classification tags")
    category: Optional[str] = Field(default=None, description="Category grouping")
    updated_at: Optional[str] = Field(default=None, description="Last updated ISO timestamp")


class FileContent(BaseModel):
    path: str = Field(description="Repo-relative path under episteme-framework")
    content: str = Field(description="Raw text content of the file")
    type: str = Field(description="Always 'file'")
    size: int = Field(description="Size in bytes")
    metadata: Optional[MetadataRecord] = Field(default=None, description="Stored metadata if any")


class MetadataPayload(BaseModel):
    path: str = Field(description="Repo-relative path to annotate")
    title: Optional[str] = Field(default=None, description="Title to set (null to leave unchanged)")
    description: Optional[str] = Field(default=None, description="Description to set")
    tags: Optional[List[str]] = Field(default=None, description="Tags to set (replaces existing)")
    category: Optional[str] = Field(default=None, description="Category to set")


class SearchResult(BaseModel):
    path: str = Field(description="Repo-relative path of matching file")
    name: str = Field(description="Filename")
    type: str = Field(description="Node type: 'file' or 'dir'")
    snippet: Optional[str] = Field(default=None, description="Content snippet around the match")
    score: float = Field(description="Relevance score (higher is better)")


class StatusResponse(BaseModel):
    status: str = Field(description="Operation result: 'ok'")
    path: Optional[str] = Field(default=None, description="Affected path, if applicable")
    count: Optional[int] = Field(default=None, description="Count of affected items, if applicable")


class HealthResponse(BaseModel):
    status: str = Field(description="Service status: 'healthy', 'halted', or 'degraded'")
    service_id: str = Field(description="Service identifier")
    version: str = Field(description="Service version")
    halted: bool = Field(description="Whether the service is halted by operator")
    halt_reason: Optional[str] = Field(default=None, description="Reason for halt, if halted")
    framework_root_exists: bool = Field(description="Whether the knowledge directory is accessible")
    session_id: Optional[str] = Field(default=None, description="Cloak registration session ID")
    uptime_seconds: float = Field(description="Seconds since service started")


class ErrorResponse(BaseModel):
    error: str = Field(description="Machine-readable error code (snake_case)")
    detail: str = Field(description="Human-readable error message")
    service: str = Field(default="episteme", description="Originating service")
    status_code: int = Field(description="HTTP status code")


class AgentQueryRequest(BaseModel):
    query: str = Field(description="Search query string")
    scope: Optional[str] = Field(default=None, description="Path prefix to restrict search scope")
    max_results: Optional[int] = Field(default=20, description="Maximum number of results to return")


class AgentQueryResponse(BaseModel):
    results: List[SearchResult] = Field(description="Matching knowledge results")


# ---------------------------------------------------------------------------
# Domain-specific schemas
# ---------------------------------------------------------------------------

class SkillSummary(BaseModel):
    name: str = Field(description="Skill folder name")
    folder: str = Field(description="Path relative to skills root")
    tags: Optional[List[str]] = Field(default=None, description="Tags from SKILL.md frontmatter")
    trigger: Optional[str] = Field(default=None, description="Trigger description from frontmatter")


class SkillDetail(BaseModel):
    name: str = Field(description="Skill folder name")
    folder: str = Field(description="Path relative to skills root")
    metadata: Optional[dict] = Field(default=None, description="Parsed YAML frontmatter")
    body: str = Field(description="Markdown body after frontmatter")
    raw: str = Field(description="Full raw SKILL.md content")


class ProjectSummary(BaseModel):
    slug: str = Field(description="Project folder name (URL-safe slug)")
    files: List[str] = Field(description="List of document filenames in the project")
    file_count: int = Field(description="Number of documents")


class TopicSummary(BaseModel):
    name: str = Field(description="Topic filename (without extension)")
    filename: str = Field(description="Full filename")
    size: int = Field(description="File size in bytes")
    modified_at: float = Field(description="Last modified timestamp (unix epoch)")


class IdeaEntry(BaseModel):
    body: str = Field(description="Idea content to append to the topic file")


class CreateTopicRequest(BaseModel):
    name: str = Field(description="Topic name (used as filename, e.g. 'my-topic' becomes my-topic.md)")


class GuideCategorySummary(BaseModel):
    category: str = Field(description="Category folder name")
    guide_count: int = Field(description="Number of guide files in this category")


class GuideSummary(BaseModel):
    name: str = Field(description="Guide filename")
    category: str = Field(description="Parent category folder")
    path: str = Field(description="Full relative path")


class DocFile(BaseModel):
    name: str = Field(description="Document filename")
    path: str = Field(description="Relative path from framework root")
    size: int = Field(description="File size in bytes")
    modified_at: float = Field(description="Last modified timestamp (unix epoch)")
    section: str = Field(description="Document section: 'agent', 'project', or 'config'")
