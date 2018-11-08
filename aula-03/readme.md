# Reduzindo ifs com polimorfismo

Nessa aula vimos como utilizar do polimorfismo em python. Polimorfismo está estritamente ligado com a herança de classes e o relacionamento "é um". Assim, não importa a classe usada, contando que ela herde de uma classe específica, podemos usar qualquer método dessa classe específica.

Vimos também a utilização da função built-in __str__, que gera uma represetanção textual para o usuário final. 

```python
class Pai():
    def __str__(self):
        return f'Nome:{programa._nome} Likes: {programa.likes}'
print(Pai)
```
O código acima mostra a utilização da função __str__. É possível chamar apensar o método print para obter infomações de classes que contenham o método __str__.

O que vimos: 
* Polimorfismo
* Relacionamento *é um*
* Representação textual de um objeto