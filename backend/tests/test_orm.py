from snowy.domain.model import TextContent, ImageContent
from snowy.domain.orm import text_contents, images
from . import conftest

def test_text_content_mapper_can_load_texts(session):
    session.execute(
        text_contents.insert(), [
            {'title': "Text from the future", 'text': "This is a very import text that will never be read by anyone"},
            {'title': "Text from the past", 'text': "Nobody cares about the past, move on"}
        ]
    )
    expected = [
        TextContent('Text from the future', 'This is a very import text that will never be read by anyone'),
        TextContent('Text from the past', 'Nobody cares about the past, move on')
    ]
    assert session.query(TextContent).all() == expected

def test_added_images_are_mapped_through_orm(session):
    # This test uses multiple execute calls because DBAPI's executemany only works when each dict has same set of keys
    session.execute(
        images.insert(), {'title': "Tasty image", 'key': 'imageKey', 'url': 'http://testimage.com/image.png'}
    )
    session.execute(
        images.insert(), {'title': "Dirty image", 'key': 'imageKey2', 'url': 'http://testimage.com/image2.png', 'width': '120px', 'height': '120px'}
    )
    expected = [
        ImageContent('Tasty image', 'http://testimage.com/image.png'),
        ImageContent('Dirty image', 'http://testimage.com/image2.png', '120px', '120px')
    ]
    assert session.query(ImageContent).filter(ImageContent.title == 'Tasty image').first() == expected[0]
    assert session.query(ImageContent).filter(ImageContent.title == 'Dirty image').first() == expected[1]