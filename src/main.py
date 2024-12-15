from textnode import TextNode, TextType

def main():
    text = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(text)

    print(TextType.CODE.value[1])
main()