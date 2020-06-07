from typing import List, TypeVar
from dataclasses import dataclass

@dataclass
class TextContent:
    title: str
    content: str

@dataclass
class ImageContent:
    title: str
    url: str
    width: str
    height: str

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
    date: str # @todo, have to use some sort of date
    content: List[CompoundContent]
    
    