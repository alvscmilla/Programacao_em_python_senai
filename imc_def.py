def imc():
    altura = float(input("Digite a altura em metros: "))
    peso = float(input("Digite o peso em kg: "))
    imc_valor = peso / (altura ** 2)
    print(f"O IMC calculado é: {imc_valor:.2f}")
    return imc_valor
    
imc()