#!/usr/bin/python
import sys
sys.path.append("../..")

import ply.yacc as yacc
import erros
from lexico import tokens, lexico
TEST_ERROR = 1
from lexico import *
#if "main" not in sys.argv[0]:
#    print ("usage : main inputfile")
#    raise SystemExit


def p_program(t):
    '''program : program program
                | variable_Declaration
                | statement
                | comment
                '''


def p_statement(t):
    '''statement : for_statement
                 | while_statement
                 | if_statement
                 | switch_statement '''

def p_comment(t):
    '''comment : COD_COMMENT
               | COMMENT_MONOLINE'''
    pass
def p_variable_Declaration(t):
    '''variable_Declaration : type sequence_variable SEMICOLON'''


def p_define_type(t):
    '''type : FLOAT
            | INT
            | CHAR
            '''

def p_sequence_variable(t):
    '''sequence_variable  : variable_characteristics COMMA sequence_variable
                          | variable_characteristics
    '''


def p_variable_characteristics(t):
    '''variable_characteristics   :  NAME LCOLC NUMBER RCOLC
                            |  NAME ASSIGN expression
                            |  NAME ASSIGN NUMBER POINT NUMBER
                            |  NAME ASSIGN NUMBER
                            |  NAME
                            | expression'''

def p_statement_if(t):
    '''if_statement : IF LPAREN expression RPAREN LBRACE block RBRACE ELSE LBRACE block RBRACE
                    | IF LPAREN expression RPAREN LBRACE block RBRACE'''

def p_statement_while(t):
    'while_statement : WHILE LPAREN expression RPAREN LBRACE block RBRACE'

def p_statement_for(t):
    'for_statement  :  FOR LPAREN type NAME ASSIGN expression SEMICOLON expression SEMICOLON down_up RPAREN LBRACE block RBRACE'

def p_statement_switch(p):
    '''switch_statement : SWITCH LPAREN NAME RPAREN LBRACE body_case body_case body_case sintax_default RBRACE
                        | SWITCH LPAREN NAME RPAREN LBRACE body_case body_case sintax_default RBRACE
                        | SWITCH LPAREN NAME RPAREN LBRACE body_case sintax_default RBRACE '''

def p_body_case(p):
    '''body_case : CASE sintax_case
                '''
def p_sintax_case(p):
    '''sintax_case : expression COLON LBRACE block break_statement RBRACE
                '''
def p_sintax_default(p):
    '''sintax_default : DEFAULT COLON LBRACE block RBRACE
                      | empty
                '''

def p_down_up(p):
    '''down_up : NAME MINUS MINUS
                   | NAME PLUS PLUS
                   | NAME ASSIGN expression
                   | expression'''


def p_expression_logop(t):
    '''expression : expression BIGGER expression
                  | expression SMALLER expression
                  | expression BIGGEREQUALS expression
                  | expression SMALLEREQUALS expression
                  | expression EQUALS expression
                  | expression DIFF expression
                  | expression AND expression
                  | expression OR expression
    '''

def p_binary_operators(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
    '''
def p_assignment_operators(p):
    '''expression :   variable SUMEQUALS expression
                  |   variable MINUSEQUALS expression
                  |   variable TIMESEQUALS  expression
                  |   variable DIVIDEEQUALS expression
    '''
def p_define_expression_literal(t):
    'expression : literal'

def p_define_expression_var(t):
    'expression : variable'

def p_literal(t):  # NORMALSTRING não sei o que é ANTIGO FLOAT
    '''literal : NORMALSTRING
                | NUMBER
                '''

def p_variable(t):
    '''variable : NAME
                '''


def p_block(t):
    '''block : list_Declarations '''


def p_list_Declarations(t):
    '''list_Declarations : variable_Declaration list_Declarations
                            | sequence_variable SEMICOLON list_Declarations
                            | empty'''

def p_empty(p):
    'empty :'
    pass

def p_statement_break(t):
    'break_statement : BREAK SEMICOLON'

def p_error(p):
    if TEST_ERROR:
        if p is not None:
            print("***   ERRO DE CONTEXTO : {}   ***".format(str(p.value)))
            print("***   ERRO DE SINTAXE NA LINHA : {}   ***".format(str(p.lexer.lineno)))
        else:
            print("***   ERRO LEXICO NA LINHA : {}   ***".format(lexico.lexer.lineno))
    else:
        raise Exception('EXCEPTION SINTAXE', 'ERROR')


def p_error(t):
    parser.errok()
    erros.unknownError(t)
######################################################################################################
def uParser(conteudo):
    parser.parse(conteudo, tracking=True)


parser = yacc.yacc()


if __name__ == '__main__':
    with open("teste.txt", "r") as arquivo:
        conteudo = arquivo.read()
        uParser(conteudo)