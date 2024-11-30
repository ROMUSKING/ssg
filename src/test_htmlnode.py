import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        node = HTMLNode("b", 
                        "This is a text node",
                        children=None,
                        props={"href": "https://www.google.com", "target": "_blank"})
        
        self.assertEqual(node.props_to_html(), 
                         ' href="https://www.google.com" target="_blank"')
    
    def test_leaf(self):
        leaf = LeafNode("a",
                        "a link text",
                        {"href": "https://www.google.com", "target": "_blank"}
                        )
        self.assertEqual(leaf.to_html(),
                         '<a href="https://www.google.com" target="_blank">a link text</a>')
    
    def test_parent(self):
        
        leaf0 = LeafNode("a",
                        "a link text",
                        {"href": "https://www.twitch.com"}
                        )
        leaf1 = LeafNode("b",
                        "bold text"
                        )
        leaf2 = LeafNode("p",
                        "a paragraph text",
                        {"style": "width:100%"}
                        )
        
        parent = ParentNode("div",
                        (leaf0, leaf1, leaf2),
                        {"padding": "12px"}
                        
                        )
        self.assertEqual(parent.to_html(),
                         '<div padding="12px"><a href="https://www.twitch.com">a link text</a><b>bold text</b><p style="width:100%">a paragraph text</p></div>')
    
    def test_parent_parent(self):
        
        leaf0 = LeafNode("a",
                        "a link text",
                        {"href": "https://www.twitch.com"}
                        )
        leaf1 = LeafNode("b",
                        "bold text"
                        )
        leaf2 = LeafNode("p",
                        "a paragraph text",
                        {"style": "width:100%"}
                        )
        
        parent = ParentNode("div",
                        (leaf0, leaf1),
                        {"padding": "12px"}
                        
                        )
        parent_parent = ParentNode("div",
                        (parent, leaf2),
                        {"margin": "12px"}
                        
                        )
        self.assertEqual(parent_parent.to_html(),
                         '<div margin="12px"><div padding="12px"><a href="https://www.twitch.com">a link text</a><b>bold text</b></div><p style="width:100%">a paragraph text</p></div>')
    
    # def test_not_parent(self):
        
        
        
    #     parent = ParentNode("div", 
    #                         "",                       
    #                     props = {"padding": "12px"}
                        
    #                     )
    #     self.assertRaises(ValueError("parent has no children"), parent.to_html())
    
if __name__ == "__main__":
    unittest.main()