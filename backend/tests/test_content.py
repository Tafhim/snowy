from snowy.domain.model import TextContent, ImageContent, CodeContent, QuoteContent, CompoundContent, Post

def test_image_sizing():
    image = ImageContent("test-image", "https://via.placeholder.com/150", "120px", "120px")

    assert image.withImgSize() == '<img src="https://via.placeholder.com/150" width="120px" height="120px"/>'

def test_compound_content_type_contains_multiple_content_types():
    text1 = TextContent('test-text-1', 'This is first text')
    text2 = TextContent('test-text-2', 'This is second text')
    image = ImageContent('test-image-1', 'https://via.placeholder.com/150', '10%', '10%')
    code1 = CodeContent('test-code-1', 'C++', '#include <cstdio>')
    quote1 = QuoteContent('test-quote-1', 'Shakespeare', 'To be or not to be that is the question')

    compoundContent = CompoundContent('test-compound-component', [text1, text2, image, code1, quote1])

    assert compoundContent.content[0].content == 'This is first text'
    assert compoundContent.content[1].content == 'This is second text'
    assert compoundContent.content[2].withImgSize() == '<img src="https://via.placeholder.com/150" width="10%" height="10%"/>'
    assert compoundContent.content[3].language == 'C++'
    assert compoundContent.content[3].code == '#include <cstdio>'
    assert compoundContent.content[4].author == 'Shakespeare'
    assert compoundContent.content[4].quote == 'To be or not to be that is the question'