# -*- coding: utf-8 -*-

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property  # getter
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property  # getter
    def nome(self):
        return self._nome

    @nome.setter  # setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome:{programa._nome} Likes: {programa.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome:{self._nome} - {self.duracao} mins - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome:{self._nome} - {self.temporadas} temporadas - Likes: {self.likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def tamanho(self):
        return len(self.programas)
    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 110)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

lista = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fds', lista)

for programa in minha_playlist.listagem:
    print(programa)

print(f'Tamanho: {minha_playlist.tamanho}')
