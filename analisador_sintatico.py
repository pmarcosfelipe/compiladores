import ply.lex as lex

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from analisador_lexico import tokens


def p_program(p):
	# <program> => <decSeq>

def p_dec(p):
	# <dec> => <varDec>
	#        | id '(' <paramList> ')' '{' <block> '}'
	#        | <type> id '(' <paramList> ')' '{' <block> '}'


def p_varDec(p):
	# <varDec> => <type> <varSpecSeq> ';'


def p_varSpec(p):
	# <varSpec> => id
 	#           | id '=' <literal>
 	#           | id '[' num ']'
 	#           | id '[' num ']' '=' '{' <literalSeq> '}'

def p_type(p):
	# <type> => "int"
 	#        | "string"
 	#        | "bool"

def p_param(p):
	# <param> => <type> id
 	#         | <type> id '[' ']'

def p_block(p):
	# <block> => <varDecList> <stmtList>

def p_stmt(p):
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
	# <ifStmt> => "if" '(' <exp> ')' '{' <block> '}'
 	#          | "if" '(' <exp> ')' '{' <block> '}' "else" '{' <block> '}'

def p_whileStmt(p):
	# <whileStmt> => "while" '(' <exp> ')' '{' <block> '}'


def p_forStmt(p):
	# <forStmt> => "for" '(' <assign> ';' <exp> ';' <assign> ')' '{' <block> '}'

def p_breakStmt(p):
	# <breakStmt> => "break" ';'

def p_readStmt(p):
	# <readStmt> => "read" <var> ';'

def p_writeStmt(p):
	# <writeStmt> => "write" <expList> ';'

def p_returnStmt(p):
	# <returnStmt> => "return" ';'
 	#              | "return" <exp> ';'

def p_subCall(p):
 	# <subCall> => id '(' <expList> ')'

def p_assign(p):
	# <assign> => <var> '='  <exp>
	#          | <var> "+=" <exp>
	#          | <var> "-=" <exp>
	#          | <var> "*=" <exp>
	#          | <var> "/=" <exp>
	#          | <var> "%=" <exp>

def p_var(p):
	# <var> => id
	#       | id '[' <exp> ']'

def p_exp(p):
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
	# <literal> => num
	#           | str
	#           | logic


def p_paramList(p):
	# <paramList> => <paramSeq>
	#             | ε

def p_paramSeq(p):
	# <paramSeq> => <param> ',' <paramSeq>
	#            | <param>

def p_varDecList(p):
	# <varDecList> => <varDec> <varDecList>
	#              | ε

def p_varSpecSeq(p):
	# <varSpecSeq> => <varSpec> ',' <varSpecSeq>
	#              | <varSpec>

def p_decSeq(p):
	# <decSeq> => <dec> <decSeq>
	#          | <dec>

def p_stmtList(p):
	# <stmtList> => <stmt> <stmtList>
	#            | ε

def p_literalSeq(p):
	# <literalSeq> => <literal> ',' <literalSeq>
	#              | <literal>

def p_expList(p):
	# <expList> => <expSeq>
	#           | ε

def p_expSeq(p):
	# <expSeq> => <exp> ',' <expSeq>
	#          | <exp>



















# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     p[0] = p[1] + p[3]

# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]

# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]

# def p_term_times(p):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]

# def p_term_div(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]

# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]

# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]

# def p_factor_expr(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)