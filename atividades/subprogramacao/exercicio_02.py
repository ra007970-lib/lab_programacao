def celsius_para_fahrenheit(celsius):
    return celsius *1.8 + 32

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

print(f" {temperatura_celsius}°C convertido é {temperatura_fahrenheit}°F")