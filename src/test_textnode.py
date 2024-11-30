import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)
    def test_neq2(self):
        node = TextNode("This is a text node", TextType.IMAGE, "imgare.com/image.jpg")
        node2 = TextNode("This is a text node", TextType.IMAGE, "imgage.com/image.jpg")
        self.assertNotEqual(node, node2)
    def test_conversion(self):
        node = TextNode("This is a text node", TextType.IMAGE, "imgare.com/image.jpg")
        node = text_node_to_html_node(node)
        node2 = LeafNode(tag="img", value="", props='src="imgare.com/image.jpg" alt="This is a text node"')
        self.assertEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()