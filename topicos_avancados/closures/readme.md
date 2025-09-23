# Closures

- São funções declaradas dentro de outras funções, que **preservam variáveis do escopo da função externa em que foram criadas**. Tais variáveis não pertencem ao escopo local da função interna nem ao escopo global, mas **continuam acessíveis para ela mesmo depois da execução da função externa**.

## Exemplo
```python
def funcao_externa(frase):
    variavel_local = "sou variavel local da funcao_externa"
    def closure():
        print(frase)
        print(variavel_local)
        print(outra_variavel_local)
    outra_variavel_local = "sou a segunda variavel local de funcao_externa"
    return closure

closure = funcao_externa("sou um argumento externo")
closure()
```

Output
```
sou um argumento externo
sou variavel local da funcao_externa
sou a segunda variavel local de funcao_externa
```

## Quando é útil?

- Quando se faz necessário criar várias funções parecidas com configurações diferentes (factory function);
- Manter estado entre chamadas de funções (stateful functions)
- Implementação de callback functions
- Memoização


- Importante lembrar: qualquer variável que receba atribuição dentro de uma função é tratada como local, a menos que se declare explicitamente `global` ou `nonlocal`.
Exemplo que dá errado:
```python
b = 6
def f2(a):
    print(a)
    print(b)
    b = 9

f2(3)
```
Output:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f2
UnboundLocalError: local variable 'b' referenced before assignment
```
Exemplo retirado do livro [Python Fluente](https://pythonfluente.com/)