#-*- coding: utf-8 -*-

class Filme:
	def __init__(self, nome, ano, duracao):
		self._nome = nome
		self.ano  = ano
		self.duracao = duracao
		self._likes = 0

	@property 	#getter
	def likes(self):
		return self._likes

	def dar_like(self):
		self._likes += 1

	@property 	#getter
	def nome(self):
		return self._nome

	@nome.setter #setter
	def nome(self,nome):
		self._nome = nome

class Serie:
	def __init__(self, nome, ano, temporadas):
		self.nome = nome
		self.ano  = ano
		self.temporadas = temporadas

	@property	#getter
	def likes(self):
		return self._likes

	def dar_like(self):
		self._likes += 1

	@property 	#getter
	def nome(self):
		return self._nome

	@nome.setter #setter
	def nome(self,nome):
		self._nome = nome

		
vingadores = Filme('vingadores - guerra infinita', '2018', 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}')

atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}')
