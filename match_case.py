# VARIAVEL = CAIXINHA COM O NOME QUE GUARDA UM VALOR 
# Calculadora simples

primeiro_numero = int(input("digite o primeiro numero: "))
segundo_numero = int(input("digite o segundo numero: "))
operador = input("digite o operador : ")    

match operador:
    case "+":        
        print("o resultado é: ", primeiro_numero + segundo_numero )
    case "-":
        print("o resultado é: ", primeiro_numero - segundo_numero)
    case "*":
        print("o resultado é: ", primeiro_numero * segundo_numero)
    case "/":
        print("o resultado é: ", primeiro_numero / segundo_numero)
