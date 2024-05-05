class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return None
        return ''.join(map(lambda kv: " " + kv[0] + "='" + kv[1] + "'",self.props.items()))
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be None in leaf node.")
        elif self.tag is None:
            return self.value
        elif self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None in parent node.")
        elif self.children is None:
            raise ValueError("Children cannot be None in a parent node")
        else:
            line = ""
            for child in self.children:
                line = line + child.to_html()
            return f"<{self.tag}>{line}</{self.tag}>"
                 
