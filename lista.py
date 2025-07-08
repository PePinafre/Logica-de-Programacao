numeros = []

def ler_numeros():
    soma = 0
    maior = None
    menor = None

    for i in range(10):
        num = float(input(f"Digite o {i+1}º numero:"))

        soma += num
        if maior is None or num> maior:
           maior = num

        if menor is None or num < menor:
            menor = num

    print(f"Soma dos numeros: {soma}")
    print(f"Soma dos numeros: {maior}")
    print(f"Soma dos numeros: {menor}")

    ler_numeros()
