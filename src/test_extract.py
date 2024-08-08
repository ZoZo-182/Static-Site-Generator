from extract import extract_markdown_images, extract_markdown_links, split_nodes_link, text_to_textnodes
from textnode import TextNode
from htmlnode import HTMLNode
from split_blocks import block_to_block_type, markdown_to_blocks, markdown_to_html_node
import unittest

class TestExtract(unittest.TestCase):
    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])


    def test_split_link(self):
        node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    "text",)
        self.assertEqual(split_nodes_link([node]), [
                                                        TextNode("This is text with a link ", "text"),
                                                        TextNode("to boot dev", "link", "https://www.boot.dev"),
                                                        TextNode(" and ", "text"),
                                                        TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
                                                    ])
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(text), [
                                                        TextNode("This is ", "text"),
                                                        TextNode("text", "bold"),
                                                        TextNode(" with an ", "text"),
                                                        TextNode("italic", "italic"),
                                                        TextNode(" word and a ", "text"),
                                                        TextNode("code block", "code"),
                                                        TextNode(" and an ", "text"),
                                                        TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
                                                        TextNode(" and a ", "text"),
                                                        TextNode("link", "link", "https://boot.dev"),
                                                    ])

    def test_block_to_block(self):
        text = "* 1847589342"
        self.assertEqual(block_to_block_type(text), "unordered_list")

    def test_md_to_html_heading(self):
        input = "# Heading 1"
        expected_node = HTMLNode("<h1>", "Heading 1")  # This reflects what the function returns
        self.assertEqual(markdown_to_html_node(input).tag, expected_node.tag)
        self.assertEqual(markdown_to_html_node(input).value, expected_node.value)

if __name__ == "__main__":
    unittest.main()



