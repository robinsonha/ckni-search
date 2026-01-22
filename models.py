from pydantic import BaseModel
from typing import Optional

class CNKIArticle(BaseModel):
    title: str
    authors: Optional[str] = None
    abstract: Optional[str] = None
    source: Optional[str] = None
    year: Optional[str] = None
    doi: Optional[str] = None
