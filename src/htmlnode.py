class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        self.props = props if props else {}

    def to_html(self):
        raise NotImplementedError("Child classes should override this method")

    def props_to_html(self):
        if not self.props:
            return ""

        attributes = []
        for key,value in self.props.items():
            attributes.append(f'{key}="{value}"')

        return " " + " ".join(attributes)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
        self.value = value

    def to_html(self):
        if not self.value: 
            raise ValueError("All leaf nodes MUST have a value")

        if not self.tag:
            return self.value 

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        
