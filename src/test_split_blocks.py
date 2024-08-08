import unittest
from split_blocks import markdown_to_blocks

class Testsplitblocks(unittest.TestCase):
    def test_markdowntoblocks(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

        # Expected output
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

        # Call the function
        result = markdown_to_blocks(text)

        # Assert the result matches expected output
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
