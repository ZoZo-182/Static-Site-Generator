import unittest

from textnode import TextNode
from splitnodes import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        node3 = TextNode("This is a text node", "bold", "www.iusenvimbtw.com")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)

    def test_nourl(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)
    
    def test_splitnodes(self):
        node = TextNode("This is text with a `code block` word", "text")
        self.assertEqual(split_nodes_delimiter([node], "`", "code"), [
                                                                        TextNode("This is text with a ", "text"),
                                                                        TextNode("code block", "code"),
                                                                        TextNode(" word", "text"),
                                                                    ]  
                         )

if __name__ == "__main__":
    unittest.main()
