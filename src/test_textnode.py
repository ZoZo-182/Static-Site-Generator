import unittest

from textnode import TextNode


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

if __name__ == "__main__":
    unittest.main()
