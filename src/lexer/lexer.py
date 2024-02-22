from src.token import Token, TokenType, lookup_ident


class Lexer:
    def __init__(self, input_string):
        self.input = input_string
        self.position = 0
        self.read_position = 0
        self.ch = ""

        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = "\0"  # null character, 0 is also ok
        else:
            self.ch = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def next_token(self):
        self.skip_whitespace()

        match self.ch:
            case "=":
                if self.peek_char() == "=":
                    self.read_char()
                    tok = Token(TokenType.EQ, "==")
                else:
                    tok = Token(TokenType.ASSIGN, self.ch)
            case "+":
                tok = Token(TokenType.PLUS, self.ch)
            case "-":
                tok = Token(TokenType.MINUS, self.ch)
            case "!":
                if self.peek_char() == "=":
                    self.read_char()
                    tok = Token(TokenType.NOT_EQ, "!=")
                else:
                    tok = Token(TokenType.BANG, self.ch)
            case "/":
                tok = Token(TokenType.SLASH, self.ch)
            case "*":
                tok = Token(TokenType.ASTERISK, self.ch)
            case "<":
                tok = Token(TokenType.LT, self.ch)
            case ">":
                tok = Token(TokenType.GT, self.ch)
            case ";":
                tok = Token(TokenType.SEMICOLON, self.ch)
            case "(":
                tok = Token(TokenType.LPAREN, self.ch)
            case ")":
                tok = Token(TokenType.RPAREN, self.ch)
            case ",":
                tok = Token(TokenType.COMMA, self.ch)
            case "{":
                tok = Token(TokenType.LBRACE, self.ch)
            case "}":
                tok = Token(TokenType.RBRACE, self.ch)
            case "\0":
                tok = Token(TokenType.EOF, self.ch)
            case _ if self.ch.isalpha() or self.ch == "_":
                literal = self.read_identifier()
                tok_type = lookup_ident(literal)
                tok = Token(tok_type, literal)
                return tok
            case _ if self.ch.isdigit():
                literal = self.read_number()
                tok = Token(TokenType.INT, literal)
                return tok
            case _:
                tok = Token(TokenType.ILLEGAL, self.ch)

        self.read_char()
        return tok

    def skip_whitespace(self):
        while self.ch in [" ", "\t", "\n", "\r"]:
            self.read_char()

    def peek_char(self):
        if self.read_position >= len(self.input):
            return "\0"
        else:
            return self.input[self.read_position]

    def read_identifier(self):
        position = self.position

        while self.ch.isalpha() or self.ch == "_":
            self.read_char()

        return self.input[position : self.position]

    def read_number(self):
        position = self.position

        while self.ch.isdigit():
            self.read_char()

        return self.input[position : self.position]

# NOT NEEDED
#    def new_token(self, token_type, ch):
#        return Token(Type=token_type, Literal=str(ch))
