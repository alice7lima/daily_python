# Funções de ordem superior em Python - anotações

Uma função de ordem superior (higher-order function), é aquela que recebe uma função como argumento ou devolve uma função como resultado. Um exemplo de função de ordem superior no Python é a função `map`.

Exemplo:
```
nomes = ["aLiCe ", "iara ", " MariaNa "]

# padronizacao dos nomes
nomes_padronizados = list(map(lambda x: x.strip().capitalize(), nomes))

print(nomes_padronizados)

```
Output:
```
['Alice', 'Iara', 'Mariana']
```
Como ilustra o exemplo acima, a função `map` recebe dois argumentos: 

1. uma função (`lambda x: x.strip().capitalize()`) que retira espaços em branco no início e no fim e deixa a primeira letra maiúscula;
2. uma lista de elementos (`nomes`).

A função `map` aplica a cada um dos elementos da lista a função fornecida no primeiro argumento, e retorna um iterável, este é convertido a uma lista usando `list()`.