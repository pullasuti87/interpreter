/*
converting source code into set of tokens
*/

package lexer

import "github.com/pullasuti87/interpreter/token"

// structure of the lexer 
type Lexer struct {
	input        string
	position     int  // current position in input (points to current char)
	readPosition int  // current reading position in input (after current char)
	currentChar  byte // current char under examination
}

// creates new Lexer
func New(input string) *Lexer {
	lexer := &Lexer{input: input}
	lexer.readChar()
	return lexer
}

// reads input and returns next token.
func (lexer *Lexer) NextToken() token.Token {
	var tok token.Token

	lexer.skipWhitespace()

	// finds out token type
	switch lexer.currentChar {
	case '=':
		if lexer.peekChar() == '=' {
			ch := lexer.currentChar
			lexer.readChar()
			literal := string(ch) + string(lexer.currentChar)
			tok = token.Token{Type: token.EQ, Literal: literal}
		} else {
			tok = newToken(token.ASSIGN, lexer.currentChar)
		}
	case '+':
		tok = newToken(token.PLUS, lexer.currentChar)
	case '-':
		tok = newToken(token.MINUS, lexer.currentChar)
	case '!':
		if lexer.peekChar() == '=' {
			ch := lexer.currentChar
			lexer.readChar()
			literal := string(ch) + string(lexer.currentChar)
			tok = token.Token{Type: token.NOT_EQ, Literal: literal}
		} else {
			tok = newToken(token.BANG, lexer.currentChar)
		}
	case '/':
		tok = newToken(token.SLASH, lexer.currentChar)
	case '*':
		tok = newToken(token.ASTERISK, lexer.currentChar)
	case '<':
		tok = newToken(token.LT, lexer.currentChar)
	case '>':
		tok = newToken(token.GT, lexer.currentChar)
	case ';':
		tok = newToken(token.SEMICOLON, lexer.currentChar)
	case ',':
		tok = newToken(token.COMMA, lexer.currentChar)
	case '{':
		tok = newToken(token.LBRACE, lexer.currentChar)
	case '}':
		tok = newToken(token.RBRACE, lexer.currentChar)
	case '(':
		tok = newToken(token.LPAREN, lexer.currentChar)
	case ')':
		tok = newToken(token.RPAREN, lexer.currentChar)
	case 0:
		tok.Literal = ""
		tok.Type = token.EOF
	default:
		if isLetter(lexer.currentChar) {
			tok.Literal = lexer.readIdentifier()
			tok.Type = token.LookupIdent(tok.Literal)
			return tok
		} else if isDigit(lexer.currentChar) {
			tok.Type = token.INT
			tok.Literal = lexer.readNumber()
			return tok
		} else {
			tok = newToken(token.ILLEGAL, lexer.currentChar)
		}
	}

	lexer.readChar()
	return tok
}

// moves lexer position over whitespace
func (lexer *Lexer) skipWhitespace() {
	for lexer.currentChar == ' ' || lexer.currentChar == '\t' || lexer.currentChar == '\n' || lexer.currentChar == '\r' {
		lexer.readChar()
	}
}

// reads next char in the input and updates lexer's position.
func (lexer *Lexer) readChar() {
	if lexer.readPosition >= len(lexer.input) {
		lexer.currentChar = 0
	} else {
		lexer.currentChar = lexer.input[lexer.readPosition]
	}
	lexer.position = lexer.readPosition
	lexer.readPosition += 1
}

// peeks next char, lexer dosen't move 
func (lexer *Lexer) peekChar() byte {
	if lexer.readPosition >= len(lexer.input) {
		return 0
	} else {
		return lexer.input[lexer.readPosition]
	}
}

func (lexer *Lexer) readIdentifier() string {
	position := lexer.position
	for isLetter(lexer.currentChar) {
		lexer.readChar()
	}
	return lexer.input[position:lexer.position]
}

func (lexer *Lexer) readNumber() string {
	position := lexer.position
	for isDigit(lexer.currentChar) {
		lexer.readChar()
	}
	return lexer.input[position:lexer.position]
}

func isLetter(ch byte) bool {
	return 'a' <= ch && ch <= 'z' || 'A' <= ch && ch <= 'Z' || ch == '_'
}

func isDigit(ch byte) bool {
	return '0' <= ch && ch <= '9'
}

// creates new token
func newToken(tokenType token.TokenType, ch byte) token.Token {
	return token.Token{Type: tokenType, Literal: string(ch)}
}
