from src.token import Token, TokenType


class Lexer:
    def __init__(self, input_string):
        self.input = input_string
        self.position = 0
        self.read_position = 0
        self.ch = ""

        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = "\0" # null character
        else:
            self.ch = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def next_token(self):
        tok = Token(TokenType.EOF, "")

        if self.ch == "=":
            tok = Token(TokenType.ASSIGN, self.ch)
        elif self.ch == ";":
            tok = Token(TokenType.SEMICOLON, self.ch)
        elif self.ch == "(":
            tok = Token(TokenType.LPAREN, self.ch)
        elif self.ch == ")":
            tok = Token(TokenType.RPAREN, self.ch)
        elif self.ch == ",":
            tok = Token(TokenType.COMMA, self.ch)
        elif self.ch == "+":
            tok = Token(TokenType.PLUS, self.ch)
        elif self.ch == "{":
            tok = Token(TokenType.LBRACE, self.ch)
        elif self.ch == "}":
            tok = Token(TokenType.RBRACE, self.ch)

        self.read_char()
        return tok


#    def new_token(self, token_type, ch):
#        return Token(Type=token_type, Literal=str(ch))
