import sys
from sly import Lexer

class MyLexer(Lexer):
    def __init__(self):
        self.symbolTable = set()

    tokens = {
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN', 
        'GT', 'GE', 'LT', 'LE', 'EQ', 
        'INCREMENT', 'DECREMENT', 'LPAREN', 'RPAREN', 'SEMICOLON', 
        'IDENTIFIER', 'IF', 'THEN', 'ELSE', 'ENDIF',
        'WHILE', 'DO', 'ENDWHILE', 'PRINT', 'NEWLINE', 
        'READ', 'INTEGER', 'STRING'
    }

    ignore = ' \t'
    ignore_single_comment = r'//.*'

    @_(r'/\*[\s\S]*?\*/')
    def ignore_block_comment(self, t):
        self.lineno += t.value.count('\n')

    INCREMENT = r'\+\+'
    DECREMENT = r'--'
    GE = r'>='
    LE = r'<='
    EQ = r'=='
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    GT = r'>'
    LT = r'<'

    LPAREN = r'\('
    RPAREN = r'\)'
    SEMICOLON = r';'

    STRING = r'"[^"\n]*"'


    @_(r'\d+[a-zA-Z][a-zA-Z0-9]*|[a-zA-Z0-9]*_[a-zA-Z0-9_]*')
    def INVALID_IDENTIFIER(self, t):
        print(f"Lexical error: unexpected character {t.value}")
        sys.exit(1)

    IDENTIFIER = r'[a-zA-Z][a-zA-Z0-9]*'
    IDENTIFIER['if'] = 'IF'
    IDENTIFIER['then'] = 'THEN'
    IDENTIFIER['else'] = 'ELSE'
    IDENTIFIER['endif'] = 'ENDIF'
    IDENTIFIER['while'] = 'WHILE'
    IDENTIFIER['do'] = 'DO'
    IDENTIFIER['endwhile'] = 'ENDWHILE'
    IDENTIFIER['print'] = 'PRINT'
    IDENTIFIER['newline'] = 'NEWLINE'
    IDENTIFIER['read'] = 'READ'

    def IDENTIFIER(self, t):
        if t.value not in self.symbolTable:
            self.symbolTable.add(t.value)
            return t
        else:
            print(f'identifier "{t.value}" already in symbol table')

    @_(r'\d+')
    def INTEGER(self, t):
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print(f"Lexical error: unexpected character {t.value[0]}")
        sys.exit(1)