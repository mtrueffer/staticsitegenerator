import unittest

from textnode import TextNode
from textnode import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_ne(self):
        node = TextNode("This is a text node", "bold", "www.boot.dev")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    def test_ne2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)
    def test_eq2(self):
        node = TextNode("This is a text node", "bold", "www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "www.boot.dev")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()