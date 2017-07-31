#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.dabeaz.com/ply/ply.html#ply_nn25

# git add -A
# git commit -a -m "Mensagem"
# git push


txt = " "
cont = 0
def incrementarContador():
	global cont
	cont += 1
	return "%d" %cont



class Nodo():
	pass

class Null(Nodo):
	def __init__(self):
		self.type = 'void'

		def imprimir(self, ident):
			print ident + "nodo nulo"

		def traducao(self):
			global txt
			id = incrementarContador()
			txt += id+"[label= "+"nodo_nulo"+"]"+"\n\t"

			return id

class program(Nodo):
	def __init__(self, decSeq, name):
		self.name = name
		self.name = decSeq

		def imprimir();
			self.decSeq.imprimir(" "+ident) #Nome dos Filhos

			print ident + "Nodo: "+self.name #Nome dos Pais

		def traducao(self):
			global txt
			id = incrementarContador()
			filho1 = self.filho1.traducao()

			txt += id +"[label = "+self.name+"]"+"\n\t"
			txt += id +"->"+filho1+"\n\t"
    
			# return "digraph G {\n\t"+txt+"}" 

















class dec(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class varDec(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class varSpec(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class type(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class param(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class block(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class stmt(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class ifStmt(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class whileStmt(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class forStmt(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class breakStmt(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class readStmt(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class writeStmt(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class returnStmt(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class subCall(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class assign(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class var(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class exp(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class literal(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class paramList(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class paramSeq(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class varDecList(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class varSpecSeq(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class decSeq(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class stmtList(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class literalSeq(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class expList(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class expSeq(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id

class empty(Nodo):
	def __init__(self, name):
		self.name = name

		def imprimir();
			self.

		def traducao(self):
			global txt
			id = incrementarContador()

			return id
	pass


# Error rule for syntax errors
# class error(Nodo):
#     if p:
#         print "Syntax error at " + "Line: " + str(p.lineno) + ", " + "Column: " + str(findColumn()) + " - Token " + str(p.value)
#     else:
#         print "Syntax error at EOF"



# class findColumn(Nodo):
#     last_cr = lex.lexer.lexdata.rfind('\n', 0, lex.lexer.lexpos)
#     column = lex.lexer.lexpos - last_cr - 1
#     return column




# Build the parser
# parser = yacc.yacc()
# resultado = parser.parse(arqEntrada)
