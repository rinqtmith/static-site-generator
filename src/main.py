import re

from htmlnode import LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode(
                "a",
                text_node.text,
                {"href": text_node.url},
            )
        case TextType.IMAGE:
            return LeafNode(
                "img",
                None,
                {"src": text_node.url, "alt": text_node.text},
            )
        case _:
            raise ValueError(f"Unknown text type: {text_node.text_type}")


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            new_lines = node.text.split(delimiter)
            if len(new_lines) < 3:
                raise Exception("invalid Markdown")
            new_list = list(
                map(
                    lambda x: TextNode(x, text_type)
                    if new_lines.index(x) % 2 != 0
                    else TextNode(x, TextType.TEXT),
                    new_lines,
                )
            )
            new_nodes.extend(new_list)

    return new_nodes


def main():
    first_node = TextNode("This is a test", TextType.LINK, "https://www.boot.dev")
    print(first_node)


main()
