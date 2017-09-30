###Calculadora ML###
###Feito por Francisco Sita###
while True:
    print(50 * "=")
    valorloja = float(input("\nDigite o valor do produto: "))
    tipoanuncio = int(input("\nDigite 1 para clássico, 2 para premium: "))
    if tipoanuncio == 1 and valorloja >= 90.00:
        classico = valorloja + 17.80
        diferencaclass = classico - valorloja
        print("\nO valor que deve ser adicionado é: {0:.2f}. \nE o total do anúncio é: {0:.2f}".format(diferencaclass, classico))
        print(classico)
        print(50 * "=")
    elif tipoanuncio == 2 and valorloja >= 84.00:
        premium1 = valorloja + 17.80
        premium2 = premium1 * 8 / 100
        somapremium = premium1 ++ premium2
        diferencapremium = somapremium - valorloja

        print("\nO valor que deve ser adicionado é: {:.2f}. "
              ""
              "\nE o total do anúncio é: {:.2f}".format(diferencapremium, somapremium))
        print(50 * "=")
    if tipoanuncio == 2 and valorloja <= 83.00:  # valor deste premium é menor que 90,00. Por isso não adicionamos o
        # frete.
        # premium1 = valorloja + 17.80
        premium3 = valorloja * 8 / 100
        premiumsoma2 = premium3 + valorloja
        diferencapremium1 = premiumsoma2 - valorloja
        print("\nO valor que deve ser adicionado é: {:.2f}. \nE o total do anúncio é: {:.2f}. \nPor se menor que "
              "R$90.00, não "
              "precisa de acionar o valor do frete.".format(diferencapremium1,premiumsoma2))
        print(50 * "=")

    if tipoanuncio == 1 and valorloja <= 89.00:
        print("\nAnúncio menor de R$90,00!")
        print(50 * "=")

    cont = input("\nPara continuar digite 1, ou para sair digite 2: ")
    if cont == "2":
        break
