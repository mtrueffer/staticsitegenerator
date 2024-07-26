from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from textnode import text_node_to_html_node


def main():
    test1 = TextNode("This is a next node", "bold", "https://www.boot.dev")
    test2 = TextNode("This is a text node", "italic")
    test2b = TextNode("The alt text","image","https://www.yourmom.com/extralarge.jpeg")

    test3 = text_node_to_html_node(test1)
    test4 = text_node_to_html_node(test2)

    test5 = ParentNode("html",[test3,test4,text_node_to_html_node(test2b)],)

    print(test1)
    print(test2)

    print(test3)
    print(test4)

    print(test5.to_html())

main()