from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
import uuid

class ContactMessage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: EmailStr
    message: str
    language: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    read: bool = False

class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    message: str
    language: str