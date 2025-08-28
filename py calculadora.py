cd calculadora-python

def calcular(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Erro: divisão por zero!"
        return a / b
    else:
        return "Operador inválido!"

print("=== Calculadora Simples ===")
print("Digite 'sair' para encerrar")

while True:
    entrada = input("Digite a expressão (ex: 2 + 3): ")

    if entrada.lower() == "sair":
        print("Até mais! 👋")
        break

    try:
        a, op, b = entrada.split()
        a = float(a)
        b = float(b)
        resultado = calcular(a, op, b)
        print("Resultado:", resultado)
    except ValueError:
        print("Entrada inválida! Use o formato: número operador número")
    except Exception as e:
        print("Erro:", e)

