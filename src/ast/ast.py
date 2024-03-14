# AST - > Abstract Syntax Tree -> internal representation of
# the source code


class Node:
    def token_literal(self, program):
        if program.statements:
            return program.statements[0].token_literal()
        else:
            return ""


class Statement(Node):
    def statement_node(self):
        pass


class Expression(Node):
    def expression_node(self):
        pass


class Program:
    def init(self, statements):
        self.statements = statements
