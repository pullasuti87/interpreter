class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()
        self.peek_token = self.lexer.next_token()

    def next_token(self):
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()
