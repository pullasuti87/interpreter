from src.lexer import Lexer


def start():

    prompt = ">> "
    while True:
        line = input(prompt)

        lexer = Lexer(line)
        tok = lexer.next_token()
        while tok.Type != "EOF":
            print(f"{{Type:{tok.Type} Literal:{tok.Literal}}}")
            tok = lexer.next_token()
