import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode(tag="p", value="Test")
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode(tag="a", props={"href": "https://www.youtube.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.youtube.com"')
        
    def test_multiple_props(self):
        multiple_props = {"href": "https://www.google.com", "target": "_blank",}
        node = HTMLNode(tag="a", props=multiple_props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_leaf_with_no_prop(self):
        node = LeafNode(value="This is a paragraph of text.", tag="p")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_with_prop(self):
        node = LeafNode(value="Click me!", tag="a", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_with_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(value=None)
            node.to_html()

    def test_PN_no_child(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag="p", children=None)
            node.to_html()
    
    def test_PN_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag=None, children=[LeafNode("b", "Bold text")])
            node.to_html()

    def test_nested_wo_child(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag="p", children=[ParentNode(tag="a", children=None)])
            node.to_html()

    def test_parent_node(self):
        node = ParentNode(
                "p",
                [
                    LeafNode(tag="b", value="Bold text"),
                    LeafNode(tag=None, value="Normal text"),
                    LeafNode(tag="i", value="italic text"),
                    LeafNode(tag=None, value="Normal text"),
                ],
        )

        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>') 

    def test_nested_parent_with_leaf(self):
        node = ParentNode(
                "p",
                [
                    ParentNode("p", [
                                        LeafNode(tag="b", value="Bold text"),
                                        LeafNode(tag=None, value="Normal text"),
                                        LeafNode(tag="i", value="italic text"),
                                        LeafNode(tag=None, value="Normal text"),
                                    ]
                              )
                ],
                    
        )
        
        self.assertEqual(node.to_html(), '<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>')


    def test_extreme_nested(self):
        node = ParentNode(
                "p",
                [
                    ParentNode("p", [
                                       ParentNode("p", [
                                                            LeafNode(tag="b", value="Bold text"),
                                                            LeafNode(tag=None, value="Normal text"),
                                                            LeafNode(tag="i", value="italic text"),
                                                            LeafNode(tag=None, value="Normal text"), 
                                                        ], 
                                                ),
 
                                        LeafNode(tag="b", value="Bold text"),
                                        LeafNode(tag=None, value="Normal text"),
                                        LeafNode(tag="i", value="italic text"),
                                        LeafNode(tag=None, value="Normal text"),
                                    ]
                              )
                ],
                    
        )
        
        self.assertEqual(node.to_html(), '<p><p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>')
  

    def test_parent_with_prop(self):
        node = ParentNode(
                "p",
                [
                    LeafNode(tag="b", value="Bold text"),
                    LeafNode(tag=None, value="Normal text"),
                    LeafNode(tag="i", value="italic text"),
                    LeafNode(tag=None, value="Normal text"),
                    ], props={"href": "https://www.google.com"}
        )

        self.assertEqual(node.to_html(), '<p href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>') 
 

    def test_nested_parent_with_prop(self):
        node = ParentNode(
                "p",
                [
                    ParentNode("p", [
                                       ParentNode("p", [
                                                            LeafNode(tag="b", value="Bold text"),
                                                            LeafNode(tag=None, value="Normal text"),
                                                            LeafNode(tag="i", value="italic text"),
                                                            LeafNode(tag=None, value="Normal text"), 
                                                        ], props={"href": "https://www.google.com"}
  
                                                  ),
 
                                        LeafNode(tag="b", value="Bold text"),
                                        LeafNode(tag=None, value="Normal text"),
                                        LeafNode(tag="i", value="italic text"),
                                        LeafNode(tag=None, value="Normal text"),
                                    ]
                              )
                ],
                    
        )
        
        self.assertEqual(node.to_html(), '<p><p><p href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>') 

if __name__ == "__main__":
    unittest.main()
