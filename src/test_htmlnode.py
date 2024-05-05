from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

def main():

    test1 = HTMLNode()
    test2 = HTMLNode("p","Some text",[],{"href": "https://www.google.com", "target": "_blank"})

    test3 = test1.props_to_html()
    test4 = test2.props_to_html()

    test5 = LeafNode("b","This text is bolded")
    test6 = LeafNode(None,"this is plain test")
    test7 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    test8 = LeafNode("i","This text is italics")
    test9 = LeafNode(None,"More plain text")

    test11 = ParentNode("p",[test5,test6,test7],)
    test12 = ParentNode("p",[test8,test9],)
    test13 = ParentNode("body",[test11,test12],)
    test14 = ParentNode("html",[test13],)
    test15 = test14.to_html()

    print(test15)

main()
