# Removendo duplicação com herança

Costuma-se entender por 'herança' algo que é passado para alguém. No contexto pythonico, herança é tudo aquilo (atributos e métodos) que uma classe mais abstrata passa para uma classe específica. A sintaxe é bem fácil:
```python
	class Pai():
		def __init__(self, cor_olhos, cor_cabelo, sobrenome):
			self.cor_olhos  = cor_olhos
			self.cor_cabelo = cor_cabelo
			self.sobrenome  = sobrenome

	class Filha(Pai):
		def __init__(self, endereço, altura):
			super.()__init__(cor_olhos, cor_cabelo, sobrenome)
			self.endereço = endereço
			self.altura   = altura
```

No exemplo acima, a classe Filha herda da classe Pai os atributos cor_olhos, cor_cabelo e sobrenome.
O que aprendemos:
* Herança 
* Generalização/Especificação
* Método ```super()```  