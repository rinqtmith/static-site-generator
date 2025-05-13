def markdown_to_blocks(md):
    blocks = md.split("\n\n")
    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = list(filter(lambda x: x != "", blocks))

    return blocks
