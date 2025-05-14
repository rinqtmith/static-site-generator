from blocks import extract_title, markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using template {template_path}"
    )
    with open(from_path, "r") as f:
        content = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    title = extract_title(content)
    html_content = markdown_to_html_node(content).to_html()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)

    with open(dest_path, "w") as f:
        f.write(template)
