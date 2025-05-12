import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty_props(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_props(self):
        node = HTMLNode(props={"class": "btn", "id": "submit"})
        self.assertEqual(node.props_to_html(), ' class="btn" id="submit"')

    def test_props_to_html_none_props(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
