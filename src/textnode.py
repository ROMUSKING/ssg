
from enum import Enum
from htmlnode import LeafNode 

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    TEXT = "text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self,
                    text,
                    text_type,
                    url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self,
            other):
        return (self.text == other.text and 
            self.text_type == other.text_type and
            self.url == other.url)
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props=f'href="{text_node.url}"')
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props=f'src="{text_node.url}" alt="{text_node.text}"')
        case _:
            raise Exception("Invalid text node type")