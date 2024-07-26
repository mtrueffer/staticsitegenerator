from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        if self.url is None:
            return "TextNode(" + self.text + ", " + self.text_type + ", )"
        return "TextNode(" + self.text + ", " + self.text_type + ", " + self.url + ")"

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None,text_node.text,)
    elif text_node.text_type == "bold":
        return LeafNode("b",text_node.text,)
    elif text_node.text_type == "italic":
        return LeafNode("i",text_node.text,)
    elif text_node.text_type == "code":
        return LeafNode("code",text_node.text,)
    elif text_node.text_type == "link":
        return LeafNode("a",text_node.text,"href")
    elif text_node.text_type == "image":
        return LeafNode("img","",{"src" : text_node.url, "alt" : text_node.text})
    else:
        raise ValueError(f"Invalid text_type of {text_node.text_type} added to text_node_to_html_node")

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    split_nodes = []
    for node in old_nodes:
        if text_type == "text" and node.text.find(delimiter) != -1:
            if node.text[0] == delimiter and node.text[-1] == delimiter:
                split_nodes.append(TextNode(node.text,text_type,))
            elif node.text.find(delimiter) != -1 and node.text[node.text.find(delimiter)+1::].find(delimiter) == -1:
                raise ValueError(f"The text {node.text} is not valid markdown script.")
            else:
                words = node.text.split()
                tmp_list = []
                tmp_type = None
                for word in words:
                    if not tmp_list:
                        if word[0::] == delimiter:
                            tmp_type = text_type
                        else:
                            tmp_type = "text"
                    else:
                        if word[0::] == delimiter:
                            pass
                        elif word[:-1:] == delimiter:
                            pass
                    tmp_list.append(word)

        else:
            split_nodes.append(node)
    return split_nodes