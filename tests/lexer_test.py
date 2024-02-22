import unittest

from src.lexer import Lexer
from src.token import TokenType


class TestNextToken(unittest.TestCase):
    def test_next_token(self):
        input_program = "=+(){},;"
        tests = [
            (TokenType.ASSIGN, "="),
            (TokenType.PLUS, "+"),
            (TokenType.LPAREN, "("),
            (TokenType.RPAREN, ")"),
            (TokenType.LBRACE, "{"),
            (TokenType.RBRACE, "}"),
            (TokenType.COMMA, ","),
            (TokenType.SEMICOLON, ";"),
            (TokenType.EOF, ""),
        ]

        lexer = Lexer(input_program)

        for i, test in enumerate(tests):
            tok = lexer.next_token()

            with self.subTest(i=i):
                self.assertEqual(tok.Type, test[0])
                self.assertEqual(tok.Literal, test[1])


if __name__ == "__main__":
    unittest.main()
