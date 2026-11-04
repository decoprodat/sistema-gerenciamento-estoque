import os

#---------------------------------------------------------------------------ESTOQUE-----------------------------------------------------------#

def cadastrar_produto ():

    cadastro = {}

    cadastro["produto"] = input("Produto: ")
    cadastro["codigo"] = int(input("Codigo: "))
    cadastro["preco"] = float(input("Valor: "))
    cadastro["categoria"] = input("Categoria: ")
    cadastro["quantidade"] = int(input("Quantidade: "))
    cadastro["disponibilidade"] = True
    cadastro["vendas"] = 0


    return cadastro

def busca_produto (produtos):

    busca = input("Buscar Produto: ")

    encontrado = False

    for produto in produtos.values():

        if busca == produto["produto"]:

            encontrado = True
            print(produto)

            print("Produto encontrado!")


    if not encontrado:

        print("Produto indisponível")
    print("========================================================")


def listar_produtos (produtos):

    print("Os produtos disponivéis são: ")

    for produto in produtos.values():

        print(produto)
    print("========================================================")


def repor_estoque(produtos):

    busca = input("Produto que deseja repor: ")
    encontrado = False

    for produto in produtos.values():

        if busca == produto["produto"]:

            encontrado = True

            quantidade = int(input("Insira a qunantidade desejada:"))

            produto["quantidade"]+=quantidade

            print("Reposição feita com sucesso!")

    if not encontrado:

        print("Produto não encontrado!")

    print("========================================================")


def mais_vendido(produtos):

    maior = 0

    for produto in produtos.values():

        if produto["vendas"] > maior:

            maior = produto["vendas"]

            mais_vendido = produto

    if maior == 0:

        print("Nenhuma venda registrada ainda!")

    else:

        print("O produto mais vendido é : ", mais_vendido)
    print("========================================================")



# ----------------------------------------------------------------------------CLIENTE-------------------------------------------------------- #

def cadastrar_cliente ():

    cliente = {}


    cliente["nome"] = input("Nome: ")
    cliente["cpf"] = input("CPF: ")
    cliente["telefone"] = int(input("Telefone: "))

    return cliente


def listar_cliente(clientes):

    for cliente in clientes.values():

        print(cliente)
    print("========================================================")


def buscar_cliente(clientes):

    encontrado = False

    pesquisa = input("Insira o nome do cliente: ")

    for cliente in clientes.values():


        if pesquisa == cliente["nome"]:

            encontrado = True

            print("Cliente encontrado com sucesso!")
            print(cliente)

    if not encontrado:

        print("Cliente não encontrado!")

    print("========================================================")


# ----------------------------------------------------------------------------PEDIDOS----------------------------------------------------------------------------------------------------------- #
def realizar_pedido ():



        compra = {}

        compra["produto"] = input("Produto: ")
        compra["codigo"] = int(input("Código: "))
        compra["valor"] = float(input("Valor: "))
        compra["quantidade"] = int(input("Quantidade: "))

        return compra


def listar_pedidos(pedidos):

    for numero, pedido in pedidos.items():

        print("Pedido", numero, ":", pedido)
    print("========================================================")


def valor_total(produtos):

    sm_total = 0

    for produto in produtos.values():

        sm_total+= produto["valor"] * produto["quantidade"]

    print(f"A soma total a se pagar é : {sm_total:.2f}")

    print("========================================================")



def disponibilidade (produtos):

    buscar = input("Nome do produto: ")
    encontrado = False

    for produto in produtos.values():

        if buscar == produto["produto"] and produto["disponibilidade"] == True:

            encontrado = True

            print("Produto disponivél!")

            quantidade = int(input("Quantidade desejada: "))

            if quantidade <= produto["quantidade"]:

                produto["quantidade"] -= quantidade

            elif produto ["quantidade"] == 0:

                print("Produto indisponível no momento!")

    if not encontrado:

        print("Produto não encontrado!")




# ----------------------------------------------------------------------------ARQUIVOS------------------------------------------------------------------------------------------------------------ #


def arq_w_produto (estoque):

    with open ("arquivo.txt","w", encoding="utf-8") as arquivo:


        for produto in estoque.values():

            arquivo.write(

                str(produto["produto"]) + ";" +
                str(produto["codigo"]) + ";" +
                str(produto["preco"]) + ";" +
                str(produto["quantidade"]) + ";" +
                str(produto["disponibilidade"]) + ";" +
                str(produto["vendas"]) + ";" +
                str(produto["categoria"]) + "\n"

            )

    print("Estoque salvo com sucesso!")


def arq_w_cliente(clientes):

    with open ("clientes.txt", "w" , encoding="utf-8") as arquivo:

        for cliente in clientes.values():

            arquivo.write(

            str(cliente["nome"]) + ";" +
            str(cliente["cpf"]) + ";" +
            str(cliente["telefone"]) + "\n"

            )

        print("cliente")

def arq_a_produto (estoque):

    with open ("arquivo.txt","a",encoding="utf-8") as arquivo:

        for produto in estoque.values():


            arquivo.write(

                str(produto["produto"]) + ";" +
                str(produto["codigo"]) + ";" +
                str(produto["preco"]) + ";" +
                str(produto["quantidade"]) + ";" +
                str(produto["disponibilidade"]) + ";" +
                str(produto["vendas"]) + ";" +
                str(produto["categoria"]) + "\n"

            )

def arq_a_cliente (clientes):

    with open ("clientes.txt","a",encoding="utf-8") as arquivo:

        for cliente in clientes.values():


            arquivo.write(

                str(cliente["nome"]) + ";" +
                str(cliente["cpf"]) + ";" +
                str(cliente["telefone"]) + "\n"

                )

        print(cliente)

def arq_r_produto(estoque):

    if not os.path.exists("arquivo.txt"):

        print("Nenhum estoque salvo ainda!")
        return

    with open ("arquivo.txt","r",encoding="utf-8") as arquivo:

        for dados in arquivo:

            dados = dados.strip().split(";")

            produto = {}

            produto["produto"] = str(dados[0])
            produto["codigo"] = int(dados[1])
            produto["preco"] = float(dados[2])
            produto["quantidade"] = int(dados[3])
            produto["disponibilidade"] = (dados[4]) == "True"
            produto["vendas"] = int(dados[5])
            produto["categoria"] = str(dados[6])

            estoque[produto["codigo"]] = produto



    print("Estoque recarregado com sucesso!")

def arq_r_cliente(clientes):

        with open("clientes.txt","r", encoding= "utf-8") as arquivo:

            for dados in arquivo:


                dados = dados.strip().split(";")

                cliente = {}

                cliente["nome"] = str(dados[0])
                cliente["cpf"] = str(dados[1])
                cliente["telefone"] = int(dados[2])

                clientes[cliente["cpf"]] = cliente


            print(clientes)



clientes = {}
estoque = {}
pedidos = {}



while True:

    print("============================MENU==================================")

    print("============================SISTEMA==================================")



    print("\n"

        "1 - Cadastrar Produto \n"
        "2 - Listar Produtos \n"
        "3 - Buscar Produto \n"
        "4 - Repor estoque \n"
        "5 - Produto mais vendido \n"
        )

    print("============================CLIENTES==================================\n" \
        "6 - Cadastrar Cliente \n"
        "7 - Listar Clientes \n"
        "8 - Buscar Cliente \n"
    )


    print("============================PEDIDOS==================================\n"
        "9 - Realizar Pedido \n"
        "10 - Listar Pedidos \n"
        "11 - Calcular valor total dos pedidos \n"
    )

    print("============================ARQUIVOS==================================\n" \
        "12 - Salvar Estoque \n"
        "13 - Recarregar Estoque \n"
        "14 - Encerrar Programa \n"
    "========================================================================"
    )

    print("Escolha uma opção : ")

    menu = int(input(""))


    if menu == 1:

        produto = cadastrar_produto()

        estoque[produto["codigo"]] = produto

        print("Produto cadastrado com sucesso!")

    elif menu == 2:

        listar_produtos(estoque)

    elif menu == 3:

        busca_produto(estoque)

    elif menu == 4:

        repor_estoque(estoque)

    elif menu == 5:

        mais_vendido(estoque)

    elif menu == 6:

        cliente = cadastrar_cliente()

        clientes[cliente["cpf"]] = cliente

        print("Cliente cadastrado com sucesso!")

    elif menu == 7:

        listar_cliente(clientes)

    elif menu == 8:

        buscar_cliente(clientes)

    elif menu == 9:

        compra = realizar_pedido()

        codigo = compra["codigo"]

        if codigo in estoque and estoque[codigo]["quantidade"] >= compra["quantidade"]:

            estoque[codigo]["quantidade"] -= compra["quantidade"]
            estoque[codigo]["vendas"] += compra["quantidade"]

            pedidos[len(pedidos) + 1] = compra

            print("Pedido realizado com sucesso!")

        else:

            print("Produto não encontrado ou estoque insuficiente!")

    elif menu == 10:

        listar_pedidos(pedidos)

    elif menu == 11:

        valor_total(pedidos)

    elif menu == 12:

        arq_w_produto(estoque)

    elif menu == 13:

        arq_r_produto(estoque)

    elif menu == 14:

        print("Programa encerrado!")

        break

    else:

        print("Opção inválida!")