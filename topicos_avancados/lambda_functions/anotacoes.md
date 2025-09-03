# Funções `lambda` em Python

- No python, a palavra reservada `lambda` cria uma **função anônima** dentro de uma expressão
- Seu melhor uso é no contexto de uma lista de argumentos para uma função de ordem superior (higher-order function), como `map`, `filter`, `reduce`, `sorted`, entre outras
- As funções lambda são expressões, então podem receber um nome:
    ```
    add_two = lambda x: x + 2
    add_two(2) 
    #resultado: 4
    ```

- Uma função lambda pode ser uma função de ordem superior ao receber uma função como um argumento:
    ```
    high_order_func = lambda x, func: x + func(x)
    high_order_func(2, lambda x: x * x) # resultado: 6
    high_order_func(2, lambda x: x + 3) # resultado: 7
    ```

- Quando se tem a necessidade de utilizar uma função pequena e que não será utilizadas muitas vezes no código, faz sentido o uso de `lambda`

- Para lógicas complexas, que exigem mais que uma expressão, é mais adequado utilizar uma função regular, utilizando `def`