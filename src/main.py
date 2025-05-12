from textnode import TextNode, TextType


def main():
    first_node = TextNode("This is a test", TextType.LINK, "https://www.boot.dev")
    print(first_node)


main()
