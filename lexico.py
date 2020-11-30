#!/usr/bin/python
import sys
sys.path.append("../..")

from ply import *
import ply.lex as lex

reserved = {
	'char'	:	'CHAR',
	'for'	:	'FOR',
	'if'	:	'IF',
	'else'	:	'ELSE',
	'int'	:	'INT',
	'float':	'FLOAT',
	'while'	:	'WHILE',
    'break' : 'BREAK',
    'switch':'SWITCH',
    'case':'CASE',
    'default':'DEFAULT'
}




tokens = ['POINT','NAME', 'NUMBER', 'NORMALSTRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
 'RPAREN', 'LPAREN', 'RCOLC', 'LCOLC', 'RBRACE', 'LBRACE', 'COMMA', 'SEMICOLON', 'OR', 'AND', 'EXPLAMATION', 'INTERROGATION', 'COLON',
 'EQUALS', 'DIFF', 'SMALLER', 'BIGGER', 'SMALLEREQUALS', 'BIGGEREQUALS', 'SUMEQUALS', 'MINUSEQUALS', 'TIMESEQUALS', 'DIVIDEEQUALS', 'MOD','COMMENT_MONOLINE','COD_COMMENT'
 ]+ list(reserved.values())


'''
tokens e simbolos
( ) [ ] { } , ; + - * / == != > >= < <= || && ! = += -= *= /= %= ? :
'''
t_ignore 		= ' \t'
t_RPAREN		= r'\)'
t_LPAREN		= r'\('

t_RCOLC			= r'\]'
t_LCOLC			= r'\['
t_RBRACE		= r'\}'
t_LBRACE		= r'\{'

t_COMMA			= r','
t_SEMICOLON		= r';'
t_OR 			= r'\|\|'
t_AND			= r'&&'
t_EXPLAMATION	= r'!'
t_INTERROGATION = r'\?'
t_COLON 		= r':'


t_EQUALS		= r'=='
t_DIFF			= r'!='
t_SMALLER		= r'<'
t_BIGGER		= r'>'
t_SMALLEREQUALS	= r'<='
t_BIGGEREQUALS 	= r'>='

t_SUMEQUALS		= r'\+='
t_MINUSEQUALS	= r'-='
t_TIMESEQUALS 	= r'\*='
t_DIVIDEEQUALS	= r'/='
t_MOD			= r'%='

t_PLUS   		= r'\+'
t_MINUS			= r'-'
t_TIMES			= r'\*'
t_DIVIDE		= r'/'
t_ASSIGN		= r'='
t_POINT 		= r'.'



def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:# Check for reserved words
        t.type = reserved[ t.value ]
#	print(t)
    return t


def t_NORMALSTRING(t):
	r'\"([^\\\n]|(\\.))*?\"'
#	print(t)
	return t

def t_NUMBER(t):
	r'[+-]?([0-9]*[.])?[0-9]+'
#	print(t)
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT_MONOLINE(t):
    r'//.*'
    return t
    #pass
    # No return value. Token discarded

def t_COD_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    return t

def lexico(data,lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

lexer=lex.lex()

if __name__ == '__main__':

    f = open('teste.txt')
    data = f.read()
    f.close()
    lexico(data, lexer)