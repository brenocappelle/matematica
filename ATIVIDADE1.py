# Função para verificar semelhança pelo critério LAL (Lado-Ângulo-Lado)
def semelhança_LAL(lado1_1, lado1_2, lado2_1, lado2_2, angulo1, angulo2):
    if (lado1_1 / lado2_1 == lado1_2 / lado2_2) and (angulo1 == angulo2):
        return True
    return False

# Função para verificar semelhança pelo critério AA (Ângulo-Ângulo)
def semelhança_AA(angulo1_1, angulo1_2, angulo2_1, angulo2_2):
    if (angulo1_1 == angulo2_1) and (angulo1_2 == angulo2_2):
        return True
    return False

# Função para verificar semelhança pelo critério LLL (Lado-Lado-Lado)
def semelhança_LLL(lado1_1, lado1_2, lado1_3, lado2_1, lado2_2, lado2_3):
    if (lado1_1 / lado2_1 == lado1_2 / lado2_2 == lado1_3 / lado2_3):
        return True
    return False

# Função principal que recebe os dados e verifica os três critérios
def verificar_semelhança():
    print("Verificação de semelhança de triângulos.")
    print("Escolha o critério de semelhança: LAL, AA, LLL.")
    
    critério = input("Digite o critério (LAL/AA/LLL): ").upper()
    
    if critério == "LAL":
        lado1_1 = float(input("Digite o lado 1 do primeiro triângulo: "))
        lado1_2 = float(input("Digite o lado 2 do primeiro triângulo: "))
        angulo1 = float(input("Digite o ângulo entre os dois lados do primeiro triângulo: "))
        
        lado2_1 = float(input("Digite o lado 1 do segundo triângulo: "))
        lado2_2 = float(input("Digite o lado 2 do segundo triângulo: "))
        angulo2 = float(input("Digite o ângulo entre os dois lados do segundo triângulo: "))
        
        if semelhança_LAL(lado1_1, lado1_2, lado2_1, lado2_2, angulo1, angulo2):
            print("Os triângulos são semelhantes pelo critério LAL.")
        else:
            print("Os triângulos NÃO são semelhantes pelo critério LAL.")
    
    elif critério == "AA":
        angulo1_1 = float(input("Digite o primeiro ângulo do primeiro triângulo: "))
        angulo1_2 = float(input("Digite o segundo ângulo do primeiro triângulo: "))
        
        angulo2_1 = float(input("Digite o primeiro ângulo do segundo triângulo: "))
        angulo2_2 = float(input("Digite o segundo ângulo do segundo triângulo: "))
        
        if semelhança_AA(angulo1_1, angulo1_2, angulo2_1, angulo2_2):
            print("Os triângulos são semelhantes pelo critério AA.")
        else:
            print("Os triângulos NÃO são semelhantes pelo critério AA.")
    
    elif critério == "LLL":
        lado1_1 = float(input("Digite o lado 1 do primeiro triângulo: "))
        lado1_2 = float(input("Digite o lado 2 do primeiro triângulo: "))
        lado1_3 = float(input("Digite o lado 3 do primeiro triângulo: "))
        
        lado2_1 = float(input("Digite o lado 1 do segundo triângulo: "))
        lado2_2 = float(input("Digite o lado 2 do segundo triângulo: "))
        lado2_3 = float(input("Digite o lado 3 do segundo triângulo: "))
        
        if semelhança_LLL(lado1_1, lado1_2, lado1_3, lado2_1, lado2_2, lado2_3):
            print("Os triângulos são semelhantes pelo critério LLL.")
        else:
            print("Os triângulos NÃO são semelhantes pelo critério LLL.")
    
    else:
        print("Critério inválido.")

# Teste o programa
verificar_semelhança()
