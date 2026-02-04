print ("Bem vindo a agência de ajudas da GCorps, o que gostaria de fazer a seguir?")

print ("[1] Falar com atendente")
print ("[2] Segunda via de boleto")
print ("[3] Cancelar serviço")
print ("[4] Informações sobre planos")
print ("[5] Sair")

opcao_menu = input("digite uma das opções acima: ")

match opcao_menu:
    case "1":
        print("Um atendente está sendo acionado, aguarde um tempo.")
    
    case "2":
        print("acesse o link: segundavia.gov") 

    case "3":
        print("iremos acionar um operador para cancelar seus serviços!")

    case "4":
        print("para ver seu plano, acesse o link: meuplano.GCorps.com.br")

    case "5":
        print("Volte sempre, a GCorps agradece pela breve companhia!!")  
    
    case _: 
        print ("Digito invalido.")
        