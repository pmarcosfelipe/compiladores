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
analisador_lexico.lexer.lineno = 2



def p_program(p):
	'''program : decSeq'''
	
	# p[0] = p[1];


def p_dec(p):
	'''dec : varDec
		   | ID LPAREN paramList RPAREN LCHAVES block RCHAVES
		   | type ID LPAREN paramList RPAREN LCHAVES block RCHAVES
	'''

	# <dec> => <varDec>
	#         | id '(' <paramList> ')' '{' <block> '}'
	#         | <type> id '(' <paramList> ')' '{' <block> '}'


def p_varDec(p):
	'''varDec : type varSpecSeq PONTOVIRGULA'''

	# <varDec> => <type> <varSpecSeq> ';'


def p_varSpec(p):
	'''varSpec : ID
			   | ID IGUAL_ATRIB literal
			   | ID LCOL NUMBER RCOL
			   | ID LCOL NUMBER RCOL IGUAL_ATRIB LCHAVES literalSeq RCHAVES
	'''
	# <varSpec> => id
 	#           | id '=' <literal>
 	#           | id '[' num ']'
 	#           | id '[' num ']' '=' '{' <literalSeq> '}'

def p_type(p):
	'''type : INT
			| STRING
			| BOOL
	'''

	# <type> => "int"
 	#        | "string"
 	#        | "bool"

def p_param(p):
	'''param : type ID
			 | type ID LCOL RCOL
	'''

	# <param> => <type> id
 	#         | <type> id '[' ']'

def p_block(p):
	'''block : varDecList stmtList'''

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

	# <ifStmt> => "if" '(' <exp> ')' '{' <block> '}'
 	#          | "if" '(' <exp> ')' '{' <block> '}' "else" '{' <block> '}'

def p_whileStmt(p):
	'''whileStmt : WHILE LPAREN exp RPAREN LCHAVES block RCHAVES'''

	# <whileStmt> => "while" '(' <exp> ')' '{' <block> '}'


def p_forStmt(p):
	'''forStmt : FOR LPAREN assign PONTOVIRGULA exp PONTOVIRGULA assign RPAREN block'''

	# <forStmt> => "for" '(' <assign> ';' <exp> ';' <assign> ')' '{' <block> '}'

def p_breakStmt(p):
	'''breakStmt : BREAK PONTOVIRGULA'''

	# <breakStmt> => "break" ';'

def p_readStmt(p):
	'''readStmt : READ var PONTOVIRGULA'''

	# <readStmt> => "read" <var> ';'

def p_writeStmt(p):
	'''writeStmt : WRITE expList PONTOVIRGULA'''

	# <writeStmt> => "write" <expList> ';'

def p_returnStmt(p):
	'''returnStmt : RETURN PONTOVIRGULA
				  | RETURN exp PONTOVIRGULA
	'''

	# <returnStmt> => "return" ';'
 	#              | "return" <exp> ';'

def p_subCall(p):
	'''subCall : ID LPAREN expList RPAREN'''

 	# <subCall> => id '(' <expList> ')'

def p_assign(p):
	'''assign : var IGUAL_ATRIB exp
			  | var INCREMENTO exp
			  | var DECREMENTO exp
			  | var MULT_ATRIB exp
			  | var DIV_ATRIB exp
			  | var MOD_IGUAL exp
	'''

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
		   | exp TERN_IF exp TERN_ELSE
		   | subCall
		   | var
		   | literal
		   | LPAREN exp RPAREN
	'''

	# <exp> => <exp> '+'  <exp>
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

	# <literal> => num
	#           | str
	#           | true
	#           | false


def p_paramList(p):
	'''paramList : paramSeq
				 | empty
	'''

	# <paramList> => <paramSeq>
	#             | ε

def p_paramSeq(p):
	'''paramSeq : param VIRGULA paramSeq
				| param
	'''

	# <paramSeq> => <param> ',' <paramSeq>
	#            | <param>

def p_varDecList(p):
	'''varDecList : varDec varDecList
				  | empty
	'''
	# <varDecList> => <varDec> <varDecList>
	#              | ε

def p_varSpecSeq(p):
	'''varSpecSeq : varSpec VIRGULA varSpecSeq
				  | varSpec
	'''

	# <varSpecSeq> => <varSpec> ',' <varSpecSeq>
	#              | <varSpec>

def p_decSeq(p):
	'''decSeq : dec decSeq
			  | dec
	'''

	# <decSeq> => <dec> <decSeq>
	#          | <dec>

def p_stmtList(p):
	'''stmtList : stmt stmtList
				| empty
	'''

	# <stmtList> => <stmt> <stmtList>
	#            | ε

def p_literalSeq(p):
	'''literalSeq : literal VIRGULA literalSeq
				  | literal
	'''

	# <literalSeq> => <literal> ',' <literalSeq>
	#              | <literal>

def p_expList(p):
	'''expList : expSeq
			   | empty
	'''

	# <expList> => <expSeq>
	#           | ε

def p_expSeq(p):
	'''expSeq : exp VIRGULA expSeq
			  | exp
	'''
	# <expSeq> => <exp> ',' <expSeq>
	#          | <exp>

def p_empty(p):
	'''empty :'''
	pass


# Error rule for syntax errors
# def p_error(p):
#     print("Syntax error in input!")


# def p_error(p):
#     last_cr = p.lexer.lexdata.rfind('\n', 0, p.lexer.lexpos)
#     column = p.lexer.lexpos - last_cr - 1

#     if p:
#         print("Erro de sintaxe em {0} na linha {1} coluna {2}".format(p.value, p.lexer.lineno, column))
#         # yacc.yacc().errok()
#     else:
#         print("Erro de sintaxe EOF")


def p_error(p):
    if p:
        print "Syntax error at " + "Line: " + str(p.lineno) + ", " + "Column: " + str(findColumn()) + " - Token " + str(p.value);
    else:
        print "Syntax error at EOF";



def findColumn():
    last_cr = lex.lexer.lexdata.rfind('\n', 0, lex.lexer.lexpos);
    column = lex.lexer.lexpos - last_cr - 1;
    return column;




# Build the parser
parser = yacc.yacc()
resultado = parser.parse(arqEntrada)
