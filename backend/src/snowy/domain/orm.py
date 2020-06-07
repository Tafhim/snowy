from sqlalchemy import MetaData, Integer, String, Text, Table, Column
from sqlalchemy.orm import mapper, relationship
from snowy.domain.model import TextContent, ImageContent

metadata = MetaData()

text_contents = Table(
    'text_contents', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255)),
    Column('text', Text)
)

images = Table(
    'image_content', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255), nullable=True),
    Column('key', String(255), unique=True),
    Column('url', String(255)),
    Column('width', String(10), nullable=True),
    Column('height', String(10), nullable=True)
)

def start_mappers():
    mapper(TextContent, text_contents)
    mapper(ImageContent, images, properties={
        'title': images.c.title,
        'url': images.c.url,
        'width': images.c.width,
        'height': images.c.height
    })