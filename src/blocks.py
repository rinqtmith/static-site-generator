from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(md):
    blocks = md.split("\n\n")
    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = list(filter(lambda x: x != "", blocks))

    return blocks


def block_to_blocktype(block):
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("-"):
        return BlockType.UNORDERED_LIST
    elif block[0].isdigit() and block[1] == ".":
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
