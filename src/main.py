import os
import shutil
from split_blocks import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode
from textnode import TextNode
from pathlib import Path

def copy_contents(source_dir, dest_dir):
    if os.path.exists(source_dir):
        shutil.rmtree(dest_dir)
        os.makedirs(dest_dir)
        items = os.listdir(source_dir)
        for item in items:
            item_path = os.path.join(source_dir, item)
            if os.path.isfile(item_path):
                shutil.copy2(item_path, dest_dir)
            elif os.path.isdir(item_path):
                new_dest_dir = os.path.join(dest_dir, item)
                if not os.path.exists(new_dest_dir):
                    os.makedirs(new_dest_dir)
                copy_contents(item_path, new_dest_dir)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
   
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

def main():
#    from_file = '/home/lulu/workspace/github.com/ZoZo-182/Static-Site-Generator/content/index.md'
    source_dir = '~/workspace/github.com/ZoZo-182/Static-Site-Generator/static'
    dest_dir = '~/workspace/github.com/ZoZo-182/Static-Site-Generator/public'
    copy_contents(source_dir, dest_dir)

    from_file = '/home/lulu/workspace/github.com/ZoZo-182/Static-Site-Generator/content'
    template = '/home/lulu/workspace/github.com/ZoZo-182/Static-Site-Generator/template.html'
    dest = '/home/lulu/workspace/github.com/ZoZo-182/Static-Site-Generator/public'
    generate_pages_recursive(from_file, template, dest)


if __name__ == "__main__":
    main()
