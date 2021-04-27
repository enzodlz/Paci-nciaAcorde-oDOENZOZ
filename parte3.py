def extrai_valor (carta):
    divide_str = [list(letra) for letra in carta]
    if len(divide_str) == 3:
        return divide_str [0] [0] + divide_str [1] [0]
    if len(divide_str) == 2:
        return divide_str [0] [0]