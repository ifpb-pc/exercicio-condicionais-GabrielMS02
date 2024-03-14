def q1():
    """
    1. Escreva um programa que solicita um número ao usuário e determina se 
    é positivo, negativo ou zero. 
    """
    n = int(input("Digite um numero: "))
    if n > 0:
        print("positivo")
    elif n < 0:
        print("negativo")
    else:
        print("zero")

def q2():
    """
    2. Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário 
    um número e imprima se ele é par ou ímpar.
    """
    n = int(input('Digite um número: '))

    if n % 2 == 0:
        print('É par')
    else:
        print('É ímpar')


def q3():
    """
    3. Calculadora Simples: Faça uma calculadora que pede ao usuário dois 
    números e uma operação (+, -, *, /) e imprima o resultado dessa operação.
    """
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite mais um número: '))
    operacao = input('Escolha uma operação matemática (+,-,*,/): ')
    if operacao == '+':
        print(n1 + n2)
    elif operacao == '-':
        print(n1 - n2)
    elif operacao == '*':
        print(n1 * n2)
    else:
        print(n1 / n2)           


def q4():
    """
    4. Maior de Três Números: Escreva um programa que solicita três números 
    ao usuário e imprima o maior dentre eles.
    """
 
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    n3 = float(input('Digite mais um número: '))
    
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    else:
        print(n3)    



def q5():
    """
    5. Classificação de Idade: Peça a idade do usuário e imprima a classificação
    em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).
    """
 
    idade = int(input('Digite a sua idade: '))
    if idade >= 0 and idade <= 12: 
        print('Criança')    
    elif idade >= 13 and idade <= 19:
        print('Adolescente')    
    elif idade >= 20 and idade <= 59:
        print('Adulto')
    else:
        print('Idoso')
        
def q6():
    """"
    6. Verificação de Triângulo: Peça ao usuário o comprimento de três 
    lados e verifique se eles podem formar um triângulo. Se sim, determine 
    se é um triângulo equilátero, isósceles ou escaleno.
    """

    ladoA = int(input(''))
    ladoB = int(input(''))
    ladoC = int(input(''))

    if (ladoA >= ladoB + ladoC) or (ladoB > ladoA + ladoC) or (ladoC > ladoA + ladoB):
        print('Inválido')
    else:
        if(ladoA == ladoB) and (ladoA == ladoC):
            print('Equilátero')
        elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB ==C):
            print('Isósceles')
        else:
            print('Escaleno')            


def q7():
    """
    7. Conversão de Notas: Escreva um programa que converte uma nota 
    de 0 a 100 em uma escala de conceitos: 
    A (90-100), B (80-89), C (70-79), D (60-69), E (50-59).e F (0-49)
    """
    nota = int(input(''))
    match nota:
        case n if n >= 90 and n <= 100:
            print('A')
        case n if n >= 80 and n < 90:    
            print('B')
        case n if n >= 70 and n < 80:
            print('C')
        case n if n >= 60 and n < 70:
            print('D')
        case n if n >= 50 and n < 60:
            print('E')
        case n if n >= 0 and n < 50:
            print('F')
        case _:
            print('')                    

def q8(): 
    """
    8. Validação de Login: Crie um programa que pede ao usuário um nome 
    de usuário e uma senha. Se o nome de usuário for "admin" e a senha for 
    "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".
    """
    nome = input('')
    senha = input('')
    ADMIN = 'Admin'
    PASSWORD = '12345'

    if nome == ADMIN and senha == PASSWORD:
        print('Acesso concedido')
    else:
        print('Acesso negado')    

def q9():
    """
    9. Calculadora de IMC: Peça ao usuário sua altura e peso e calcule o
      índice de massa corporal (IMC). Em seguida, mostre uma mensagem 
      indicando se a pessoa está: Abaixo do peso, Peso normal, Sobrepeso, 
      Obesa ou Muito obesa.
    """
    h = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))
    imc = peso/h**2

    match imc:
        case imc if imc < 18.5:
            print('Abaixo do peso')
        case imc if imc > 18.5 and imc < 25:
            print('Peso normal')
        case imc if imc > 26 and imc < 30:
            print('Sobrepeso')
        case imc if imc > 30 and imc < 35:
            print('Obesidade')
        case imc if imc > 35:
            print('Muito obeso')                 

def q10():
    """
    10. Verificação de Ano Bissexto: Escreva um programa que verifica 
    se um ano fornecido pelo usuário é bissexto ou não.
    """
    ano = int(input(''))
    if ( (ano % 4 == 0) and (ano % 100 != 0)) and ano % 400 == 0:
        print('bissexto')
    else:
        print('não')
    """
    #Passo1
    if ano % 4 == 0:
        #Passo2
        if ano % 100 == 0:
            #passo3
            if ano % 400 == 0:
                print('bissexto')
            else:
                print('não')    
        else:
            print('bissexto')   
    else:      
        print('não')
    """