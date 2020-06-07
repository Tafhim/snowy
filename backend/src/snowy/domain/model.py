from typing import List, TypeVar, Optional
from dataclasses import dataclass

# @TODO Created Updated needed

@dataclass
class TextContent:
    title: str
    text: str

@dataclass
class ImageContent:
    title: str
    url: str
    width: str # @TODO Instead should we just have dimension column?
    height: str

    def __init__(self, title: str, url: str, width: Optional[str] = None, height: Optional[str] = None):
        self.title = title
        self.url = url
        self.width = width
        self.height = height

    def withImgSize(self) -> str:
        return '<img src="{url}" width="{width}" height="{height}"/>'.format(url=self.url, width=self.width, height=self.height)

@dataclass
class CodeContent:
    title: str
    language: str
    code: str

@dataclass
class QuoteContent:
    title: str
    author: str
    quote: str

CompoundContentSupportedTypes = TypeVar('CompoundContentSupportedTypes', TextContent, ImageContent, CodeContent, QuoteContent)
@dataclass
class CompoundContent:
    title: str
    content: List[CompoundContentSupportedTypes]

@dataclass
class Post:
    title: str
    author: str
    date: str # @todo, have to use some sort of date
    content: List[CompoundContent]
