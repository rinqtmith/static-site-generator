import unittest

from blocks import BlockType, block_to_blocktype, markdown_to_blocks


class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading(self):
        self.assertEqual(block_to_blocktype("# Heading"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_blocktype("```code block```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_blocktype("> Quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_blocktype("- List item"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_blocktype("1. List item"), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        self.assertEqual(block_to_blocktype("Just a paragraph"), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
