#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

import sys

# Leitura de Arquivo
with open(sys.argv[1], 'r') as f:
    contents = f.read()
arqEntrada = contents



reserved = {
	'bool' : 'BOOL',
	'break': 'BREAK',
	'for' : 'FOR',
	'false' : 'FALSE',
	'if' : 'IF',
    'else' : 'ELSE',
	'int' : 'INT',
	'return' : 'RETURN',
	'string' : 'STRING',
    # 'logic' : 'LOGIC',
	'true' : 'TRUE',
	'while' : 'WHILE',
    'read' : 'READ',
    'write' : 'WRITE'
}

# List of token names.   This is always required
tokens = [
   'ID',
   'LPAREN',
   'RPAREN',
   'LCOL',
   'RCOL',
   'LCHAVES',
   'RCHAVES',
   'VIRGULA',
   'PONTOVIRGULA',
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'MOD',
   'IGUAL_COMP',
   'DIFERENTE',
   'MAIOR',
   'MAIOR_IGUAL',
   'MENOR',
   'MENOR_IGUAL',
   'OU_LOGICO',
   'E_LOGICO',
   'NEGACAO',
   'INVERTESINAL',
   'IGUAL_ATRIB',
   'INCREMENTO',
   'DECREMENTO',
   'MULT_ATRIB',
   'DIV_ATRIB',
   'MOD_IGUAL',
   'TERN_IF',
   'TERN_ELSE',
   # 'COMENTARIO',
   'CADEIA_CHAR'
] + list(reserved.values())


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Regular expression rules for simple tokens
t_LPAREN       = r'\('
t_RPAREN       = r'\)'
t_LCOL         = r'\['
t_RCOL         = r'\]'
t_LCHAVES      = r'\{'
t_RCHAVES      = r'\}'
t_VIRGULA      = r'\,'
t_PONTOVIRGULA = r'\;'
t_PLUS         = r'\+'
t_MINUS        = r'-'
t_TIMES        = r'\*'
t_DIVIDE       = r'/'
t_MOD          = r'%'
t_IGUAL_COMP   = r'=='
t_DIFERENTE    = r'!='
t_MAIOR 	     = r'>'
t_MAIOR_IGUAL  = r'>='
t_MENOR        = r'<'
t_MENOR_IGUAL  = r'<='
t_OU_LOGICO    = r'\|\|'
t_E_LOGICO     = r'&&'
t_NEGACAO      = r'!'
t_INVERTESINAL = r'-'
t_IGUAL_ATRIB  = r'='
t_INCREMENTO   = r'\+='
t_DECREMENTO   = r'-='
t_MULT_ATRIB   = r'\*='
t_DIV_ATRIB    = r'/='
t_MOD_IGUAL    = r'%='
t_TERN_IF      = r'\?'
t_TERN_ELSE    = r':'
# t_COMENTARIO   = r'(//.*)|(/\*(.|\n)*\*/)'
t_CADEIA_CHAR  = r'(\"(.|\n)*?\")'


def t_comment_multiline(t):
    r'((//.*)|(/\*(.|\n)*\*/))'
    # No return value. Token discarded
    pass

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
# def t_error(t):
#     print("Illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)




# Compute column. 
#     input is the input text string
#     token is a token instance
def find_column(input,token):
    last_cr = input.rfind('\n',0,lex.lexer.lexpos)
    if last_cr < 0:
	last_cr = 0
    column = (lex.lexer.lexpos - last_cr) + 1
    return column


def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  print("Line: " + repr(t.lineno) + " Column: " + repr(find_column(arqEntrada, t)) + '\n')
  t.lexer.skip(1)

  
# Build the lexer
lexer = lex.lex()

lexer.input(arqEntrada)

# Test it out
# data = ''' () [] {} , ; + - * /  == != > >= < <= || && ! = += -= *= /= %= ? : if then else'''


# Tokenize
while True:
    tok = lexer.token()
    coluna = find_column(arqEntrada,tok)
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, coluna)