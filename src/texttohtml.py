from htmlnode import LeafNode 
from textnode import TextNode

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(tag=None, value=text_node.text)

    if text_node.text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)

    if text_node.text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)

    if text_node.text_type == "code":
        return LeafNode(tag="code", value=text_node.text)

    if text_node.text_type == "link":
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url}) 

    if text_node.text_type == "image":
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")



    
      

