from textnode import TextNode

def xstr(s):
    if s is None:
        return "<None>"
    else:
        return str(s)

def main():
    test1 = TextNode("This is a next node", "bold", "https://www.boot.dev")
    test2 = TextNode("This is a text node", "italics")

    print(test1)

    print(test2)

main()