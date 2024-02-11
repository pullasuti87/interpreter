/*
converting source code into set of tokens
*/

package lexer

type Lexer struct {
	input        string
	position     int  // position in input
	readPosition int  // points to next char in input
	ch           byte // current char
}

func New(input string) *Lexer {
	l := &Lexer{input: input}
	return l
}

// gives the next char
// moves the position in the input
func (l *Lexer) readChar() {
	if l.readPosition >= len(l.input) {
		l.ch = 0
	} else {
		l.ch = l.input[l.readPosition]
	}
	l.position = l.readPosition
	l.readPosition += 1
}


