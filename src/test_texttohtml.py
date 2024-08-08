import unittest
from htmlnode import HTMLNode, LeafNode
from textnode import TextNode

class TestTexttoHtml(unittest.TestCase):
    def boldtest(self):
        node = TextNode("This should be bold text.", "bold")
        self.assertEqual(text_node_to_html_node(node), "<b>This should be bold text.</b>")

    def codetest(self):
        node = TextNode('print("hello world!")', "code")
        self.assertEqual(text_node_to_html_node(node), '<code>print("hello world!")</code>')

    def imagetest(self):
        node = TextNode("This is some alt text that describes the image", "img", "https://www.google.com")
        self.assertEqual(text_node_to_html_node(node), '<img src="https://www.google.com" alt="This is some alt text that describes the image">')

if __name__ == "__main__":
    unittest.main()
