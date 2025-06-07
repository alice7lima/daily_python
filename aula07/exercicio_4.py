def converter_celcius_para_fahrenheit(temperatura: float) -> float:
    valor_fahrenheit = temperatura * 1.8 + 32
    return f"{valor_fahrenheit:.2f}"

if __name__ == '__main__':
    temperatura = 21
    print(converter_celcius_para_fahrenheit(temperatura=temperatura))