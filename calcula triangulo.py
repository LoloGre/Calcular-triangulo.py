def calcular_area(base, altura):
    area = 0.5 * base * altura
    return area

if __name__ == "__main__":
    print("Calculadora de área de triángulo")
    base = float(input("Ingrese la longitud de la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = calcular_area(base, altura)
    print(f"El área del triángulo es: {area}")

