import unittest

from main import split_nodes_delimiter, text_node_to_html_node
from textnode import TextNode, TextType


class TestMain(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_split_node_bold(self):
        node = TextNode("This is text with a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes[0],
            TextNode("This is text with a ", TextType.TEXT),
        )
        self.assertEqual(
            new_nodes[1],
            TextNode("code block", TextType.BOLD),
        )
        self.assertEqual(
            new_nodes[2],
            TextNode(" word", TextType.TEXT),
        )


if __name__ == "__main__":
    unittest.main()
