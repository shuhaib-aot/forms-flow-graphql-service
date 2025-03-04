from beanie import Document
from typing import Optional


class FormModel(Document):
    title: str
    name: str
    path: str
    type: str
    isBundle: Optional[bool]
    display: Optional[str] = None

    class Settings:
        name = "forms"
