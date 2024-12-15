import unittest

from textnode import TextNode, TextType
from markdown import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = [TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)]
        nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter(node,  TextType.BOLD) , nodes)
    def test_eq2(self):
        node = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        
        nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter(node, TextType.CODE), nodes)
    def test_eq_image(self):
        node = [TextNode(text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type=TextType.TEXT)]

        
        nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode(text="rick roll", text_type=TextType.IMAGE, url="https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode(text="obi wan", text_type=TextType.IMAGE, url="https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(split_nodes_delimiter(node,  TextType.IMAGE), nodes)
    def test_eq_link(self):
        node = [TextNode(text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type=TextType.TEXT)]

        
        nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(text="to youtube", text_type=TextType.LINK, url="https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(split_nodes_delimiter(node, TextType.LINK), nodes)
    
if __name__ == "__main__":
    unittest.main()
    
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"