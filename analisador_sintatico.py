#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.dabeaz.com/ply/ply.html#ply_nn25

# git add -A
# git commit -a -m "Mensagem"
# git push
import ply.lex as lex

import ply.yacc as yacc

import sys

# Get the token map from the lexer.  This is required.
import analisador_lexico

with open(sys.argv[1], 'r') as f:
    contents = f.read()
arqEntrada = contents

tokens = analisador_lexico.tokens
analisador_lexico.lexer.lineno = 1

precedence = (
    ('right', 'TERN_IF'),
    ('left', 'OU_LOGICO'),
    ('left', 'E_LOGICO'),
    ('left', 'IGUAL_COMP', 'DIFERENTE'),
    ('left', 'MAIOR', 'MAIOR_IGUAL', 'MENOR', 'MENOR_IGUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'NEGACAO', 'INVERTESINAL')
)

# precedence = (
#     ('right', 'NEGACAO'),
#     ('left', 'E_LOGICO', 'OU_LOGICO'),
#     ('left', 'MAIOR_IGUAL', 'MENOR_IGUAL', 'MAIOR', 'MENOR', 'IGUAL_COMP', 'DIFERENTE'),
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'TIMES', 'DIVIDE', 'MOD'),
#     ('right', 'TERN_IF'),
# );

def p_program(p):
	'''program : decSeq'''

	p[0] = ('program', p[1])
	# p[0] = program(p[1], "program");


def p_dec(p):
	'''dec : varDec
		   | ID LPAREN paramList RPAREN LCHAVES block RCHAVES
		   | type ID LPAREN paramList RPAREN LCHAVES block RCHAVES
	'''
	
	if len(p) == 2:
		p[0] = ('dec', p[1])
	elif len(p) == 8:
		p[0] = ('dec', p[1], p[3], p[6])
	elif len(p) == 9:
		p[0] = ('dec', p[1], p[2], p[4], p[7])

	# <dec> => <varDec>
	#         | id '(' <paramList> ')' '{' <block> '}'
	#         | <type> id '(' <paramList> ')' '{' <block> '}'


def p_varDec(p):
	'''varDec : type varSpecSeq PONTOVIRGULA'''

	p[0] = ('varDec', p[1])

	# <varDec> => <type> <varSpecSeq> ';'


def p_varSpec(p):
	'''varSpec : ID
			   | ID IGUAL_ATRIB literal
			   | ID LCOL NUMBER RCOL
			   | ID LCOL NUMBER RCOL IGUAL_ATRIB LCHAVES literalSeq RCHAVES
	'''

	if len(p) == 2:
		p[0] = ('varSpec', p[1])
	elif len(p) == 4:
		p[0] = ('varSpec', p[1], p[3])
	elif len(p) == 5:
		p[0] = ('varSpec', p[1], p[3])
	elif len(p) == 9:
		p[0] = ('varSpec', p[1], p[3], p[5], p[7])

	# <varSpec> => id
 	#           | id '=' <literal>
 	#           | id '[' num ']'
 	#           | id '[' num ']' '=' '{' <literalSeq> '}'


def p_type(p):
	'''type : INT
			| STRING
			| BOOL
	'''

	p[0] = ('type', p[1])

	# <type> => "int"
 	#        | "string"
 	#        | "bool"


def p_param(p):
	'''param : type ID
			 | type ID LCOL RCOL
	'''

	if len(p) == 3:
		p[0] = ('param', p[1], p[2])
	elif len(p) == 5:
		p[0] = ('param', p[1], p[2])

	# <param> => <type> id
 	#         | <type> id '[' ']'


def p_block(p):
	'''block : varDecList stmtList'''

	p[0] = ('block', p[1], p[2])

	# <block> => <varDecList> <stmtList>


def p_stmt(p):
	''' stmt : ifStmt
			 | whileStmt
			 | forStmt
			 | breakStmt
			 | returnStmt
			 | readStmt
			 | writeStmt
			 | assign PONTOVIRGULA
			 | subCall PONTOVIRGULA
	'''

	if len(p) == 2:
		p[0] = ('stmt', p[1])
	elif len(p) == 3:
		p[0] = ('stmt', p[1])

	# <stmt> => <ifStmt>
 	#        | <whileStmt>
 	#        | <forStmt>
 	#        | <breakStmt>
 	#        | <returnStmt>
 	#        | <readStmt>
 	#        | <writeStmt>
 	#        | <assign> ';'
 	#        | <subCall> ';'


def p_ifStmt(p):
	''' ifStmt : IF LPAREN exp RPAREN LCHAVES block RCHAVES
			   | IF LPAREN exp RPAREN LCHAVES block RCHAVES ELSE LCHAVES block RCHAVES
	'''

	if len(p) == 8:
		p[0] = ('ifStmt', p[3], p[6])
	elif len(p) == 12:
		p[0] == ('ifStmt', p[3], p[6], p[10])

	# <ifStmt> => "if" '(' <exp> ')' '{' <block> '}'
 	#          | "if" '(' <exp> ')' '{' <block> '}' "else" '{' <block> '}'


def p_whileStmt(p):
	''' whileStmt : WHILE LPAREN exp RPAREN LCHAVES block RCHAVES '''

	p[0] = ('whileStmt', p[3], p[6])

	# <whileStmt> => "while" '(' <exp> ')' '{' <block> '}'


def p_forStmt(p):
	'''forStmt : FOR LPAREN assign PONTOVIRGULA exp PONTOVIRGULA assign RPAREN LCHAVES block RCHAVES'''

	p[0] = ('forStmt', p[3], p[5], p[7], p[10])

	# <forStmt> => "for" '(' <assign> ';' <exp> ';' <assign> ')' '{' <block> '}'


def p_breakStmt(p):
	'''breakStmt : BREAK PONTOVIRGULA'''

	p[0] = ('breakStmt', p[1])

	# <breakStmt> => "break" ';'


def p_readStmt(p):
	'''readStmt : READ var PONTOVIRGULA'''

	p[0] = ('readStmt', p[2])

	# <readStmt> => "read" <var> ';'


def p_writeStmt(p):
	'''writeStmt : WRITE expList PONTOVIRGULA'''

	p[0] = ('writeStmt', p[2])

	# <writeStmt> => "write" <expList> ';'


def p_returnStmt(p):
	'''returnStmt : RETURN PONTOVIRGULA
				  | RETURN exp PONTOVIRGULA
	'''

	if len(p) == 3:
		p[0] = ('returnStmt', p[1])
	elif len(p) == 4:
		p[0] = ('returnStmt', p[1], p[2])
	# <returnStmt> => "return" ';'
 	#              | "return" <exp> ';'


def p_subCall(p):
	'''subCall : ID LPAREN expList RPAREN'''

	p[0] = ('subCall', p[1], p[3])

 	# <subCall> => id '(' <expList> ')'


def p_assign(p):
	'''assign : var IGUAL_ATRIB exp
			  | var INCREMENTO exp
			  | var DECREMENTO exp
			  | var MULT_ATRIB exp
			  | var DIV_ATRIB exp
			  | var MOD_IGUAL exp
	'''

	p[0] = ('assign', p[1], p[3])

	# <assign> => <var> '='  <exp>
	#          | <var> "+=" <exp>
	#          | <var> "-=" <exp>
	#          | <var> "*=" <exp>
	#          | <var> "/=" <exp>
	#          | <var> "%=" <exp>


def p_var(p):
	'''var : ID
   		   | ID LCOL exp RCOL
	'''

	if len(p) == 2:
		p[0] = ('var', p[1])
	elif len(p) == 5:
		p[0] = ('var', p[1], p[3])	
	

	# <var> => id
	#       | id '[' <exp> ']'


def p_exp(p):
	'''exp : exp PLUS exp
		   | exp MINUS exp
		   | exp TIMES exp
		   | exp DIVIDE exp
		   | exp MOD exp
		   | exp IGUAL_COMP exp
		   | exp DIFERENTE exp
		   | exp MENOR exp
		   | exp MENOR_IGUAL exp
		   | exp MAIOR exp
		   | exp MAIOR_IGUAL exp
		   | exp OU_LOGICO exp
		   | exp E_LOGICO exp
		   | NEGACAO exp
		   | INVERTESINAL exp
		   | exp TERN_IF exp TERN_ELSE exp
		   | subCall
		   | var
		   | literal
		   | LPAREN exp RPAREN
	'''

	if len(p) == 2:
		p[0] = ('exp', p[1])
	elif len(p) == 3:
		p[0] = ('exp', p[2])
	elif len(p) == 4:
		p[0] = ('exp', p[1], p[3])
	elif len(p) == 6:
		p[0] = ('exp', p[1], p[3], p[5])

	# <exp> => <exp> '+'   <exp>
	#       | <exp> '-'   <exp>
	#       | <exp> '*'   <exp>
	#       | <exp> '/'   <exp>
	#       | <exp> '%'   <exp>
	#       | <exp> "=="  <exp>
	#       | <exp> "!="  <exp>
	#       | <exp> "<="  <exp>
	#       | <exp> ">="  <exp>
	#       | <exp> '>'   <exp>
	#       | <exp> '<'   <exp>
	#       | <exp> "&&"  <exp>
	#       | <exp> "||"  <exp>
	#       | '!' <exp>
	#       | '-' <exp>
	#       | <exp> '?' <exp> ':' <exp>
	#       | <subCall>
	#       | <var>
	#       | <literal>
	#       | '(' <exp> ')'


def p_literal(p):
	''' literal : NUMBER
				| CADEIA_CHAR
				| TRUE
	            | FALSE
	'''

	p[0] = ('literal', p[1])

	# <literal> => num
	#           | str
	#           | true
	#           | false


def p_paramList(p):
	'''paramList : paramSeq
				 | empty
	'''

	p[0] = ('paramList', p[1])

	# <paramList> => <paramSeq>
	#             | ε


def p_paramSeq(p):
	'''paramSeq : param VIRGULA paramSeq
				| param
	'''

	if len(p) == 2:
		p[0] = ('paramSeq', p[1])
	elif len(p) == 4:
		p[0] = ('paramSeq', p[1], p[3])

	# <paramSeq> => <param> ',' <paramSeq>
	#            | <param>


def p_varDecList(p):
	'''varDecList : varDec varDecList
				  | empty
	'''

	if len(p) == 2:
		p[0] = ('varDecList', p[1])
	elif len(p) == 3:
		p[0] = ('varDecList', p[1], p[2])

	# <varDecList> => <varDec> <varDecList>
	#              | ε


def p_varSpecSeq(p):
	'''varSpecSeq : varSpec VIRGULA varSpecSeq
				  | varSpec
	'''

	if len(p) == 2:
		p[0] = ('varSpecSeq', p[1])
	elif len(p) == 4:
		p[0] == ('varSpecSeq', p[1], p[3])

	# <varSpecSeq> => <varSpec> ',' <varSpecSeq>
	#              | <varSpec>


def p_decSeq(p):
	'''decSeq : dec decSeq
			  | dec
	'''

	if len(p) == 3:
		p[0] = ('decSeq', p[1], p[2])
	elif len(p) == 2:
		p[0] = ('decSeq', p[1])


	# <decSeq> => <dec> <decSeq>
	#          | <dec>


def p_stmtList(p):
	'''stmtList : stmt stmtList
				| empty
	'''

	if len(p) == 3:
		p[0] = ('stmtList', p[1], p[2])
	elif len(p) == 2:
		p[0] = ('stmtList', p[1])


	# <stmtList> => <stmt> <stmtList>
	#            | ε


def p_literalSeq(p):
	'''literalSeq : literal VIRGULA literalSeq
				  | literal
	'''

	if len(p) == 4:
		p[0] = ('literalSeq', p[1], p[3])
	elif len(p) == 2:
		p[0] = ('literalSeq', p[1])


	# <literalSeq> => <literal> ',' <literalSeq>
	#              | <literal>


def p_expList(p):
	'''expList : expSeq
			   | empty
	'''

	p[0] = ('expList', p[1])

	# <expList> => <expSeq>
	#           | ε


def p_expSeq(p):
	'''expSeq : exp VIRGULA expSeq
			  | exp
	'''

	if len(p) == 4:
		p[0] = ('expSeq', p[1], p[3])
	elif len(p) == 2:
		p[0] = ('expSeq', p[1])

	# <expSeq> => <exp> ',' <expSeq>
	#          | <exp>


def p_empty(p):
	'''empty :'''

	# p[0] = Null()
	pass


# Error rule for syntax errors
def p_error(p):
    if p:
        print "Syntax error at " + "Line: " + str(p.lineno) + ", " + "Column: " + str(findColumn()) + " - Token " + str(p.value)
    else:
        print "Syntax error at EOF"



def findColumn():
    last_cr = lex.lexer.lexdata.rfind('\n', 0, lex.lexer.lexpos)
    column = lex.lexer.lexpos - last_cr - 1
    return column 




# Build the parser
parser = yacc.yacc()
resultado = parser.parse(arqEntrada)

print(resultado)
# resultado.imprimir(" ")
#print resultado.traducao()

# graphFile = open('graphvizthree.vz', 'w')
# graphFile.write(result.traducao())
# graphFile.close()