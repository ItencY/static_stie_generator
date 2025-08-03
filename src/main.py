from textnode import TextNode, TextType

def main():
    res = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(res)

main()