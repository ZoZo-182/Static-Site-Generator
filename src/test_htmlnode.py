import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

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

if __name__ == "__main__":
    unittest.main()
