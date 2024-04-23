# AST - > Abstract Syntax Tree -> internal representation of
# the source code

# from src.token import Token


class Node:
    def token_literal(self):
        raise NotImplementedError("token_literal method not used")


class Statement(Node):
    pass


class Expression(Node):
    pass


class Program:
    def __init__(self):
        self.statements = []

    def token_literal(self):
        if self.statements:
            return self.statements[0].token_literal()
        else:
            return ""


class LetStatement(Statement):
    def __init__(self, token, name, value):
        self.token = token
        self.name = name
        self.value = value

    def token_literal(self):
        return self.token.literal
