class Token:
    def __init__(self, token_type, literal):
        self.Type = token_type
        self.Literal = literal


class TokenType:

    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # identifiers and literals
    IDENT = "IDENT"
    INT = "INT"

    # operators
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"

    LT = "<"
    GT = ">"
    EQ = "=="
    NOT_EQ = "!="

    # delimiters
    COMMA = ","
    SEMICOLON = ";"

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # keywords
    FUNCTION = "FUNCTION"
    LET = "LET"
    TRUE = "TRUE"
    FALSE = "FALSE"
    IF = "IF"
    ELSE = "ELSE"
    RETURN = "RETURN"


keywords = {
    "fn": TokenType.FUNCTION,
    "let": TokenType.LET,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "return": TokenType.RETURN,
}


def lookup_ident(ident):
    if ident in keywords:
        return keywords[ident]
    return TokenType.IDENT
