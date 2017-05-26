#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

reserved = {
	'bool' : 'BOOL',
	'break': 'BREAK',
	'for' : 'FOR',
	'false' : 'FALSE',
	'if' : 'IF',
	'int' : 'INT',
	'return' : 'RETURN',
	'string' : 'STRING',
	'true' : 'TRUE',
	'while' : 'WHILE'
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
   'IGUAL_COMP',
   'DIFERENTE',
   'MAIOR',
   'MAIOR_IGUAL',
   'MENOR',
   'MENOR_IGUAL',
   'OU_LOGICO',
   'E_LOGICO',
   'NEGACAO',
   'IGUAL_ATRIB',
   'INCREMENTO',
   'DECREMENTO',
   'MULT_ATRIB',
   'DIV_ATRIB',
   'MOD_IGUAL',
   'TERN_IF',
   'TERN_ELSE',
   'COMENTARIO',
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
t_IGUAL_COMP   = r'=='
t_DIFERENTE    = r'!='
t_MAIOR 	   = r'>'
t_MAIOR_IGUAL  = r'>='
t_MENOR        = r'<'
t_MENOR_IGUAL  = r'<='
t_OU_LOGICO    = r'\|\|'
t_E_LOGICO     = r'&&'
t_NEGACAO      = r'!'
t_IGUAL_ATRIB  = r'='
t_INCREMENTO   = r'\+='
t_DECREMENTO   = r'-='
t_MULT_ATRIB   = r'\*='
t_DIV_ATRIB    = r'/='
t_MOD_IGUAL    = r'%='
t_TERN_IF      = r'\?'
t_TERN_ELSE    = r':'
t_COMENTARIO   = r'(//.*)|(/\*(.|\n)*\*/)'
t_CADEIA_CHAR  = r'(\"(.|\n)*?\")'

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
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Compute column. 
#     input is the input text string
#     token is a token instance
def find_column(input,token):
    last_cr = input.rfind('\n',0,lex.lexer.lexpos)
    if last_cr < 0:
	last_cr = 0
    column = (lex.lexer.lexpos - last_cr) + 1
    return column

# Build the lexer
lexer = lex.lex()

# Test it out
# data = ''' () [] {} , ; + - * /  == != > >= < <= || && ! = += -= *= /= %= ? : if then else'''

data = '''
int v[10];
/*
Procedimento de ordenação por troca
Observe como um parâmetro de arranjo é declarado
*/
bubblesort(int v[], int n) {
int i=0, j;
bool trocou = true;
while (i < n-1 && trocou) {
trocou = false;
for (j=0; j < n-i-1; j+=1) {
if (v[j] > v[j+1]) {
int aux;
aux = v[j];
v[j] = v[j+1];
v[j+1] = aux;
trocou = true;
}
}
i += 1;
}
}
main() {
int i;
for (i=0; i < 10; i+=1) {
read v[i];
}
bubblesort(v, 10);
for (i=0; i < 10; i+=1) {
write v[i], " ";
}
}
'''
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    coluna = find_column(data,tok)
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, coluna)