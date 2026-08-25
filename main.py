from services.estoque_service import EstoqueService

def ler_inteiro(mensagem):
    valor = input(mensagem)
    return int(valor)

def ler_float(mensagem):
    valor = input(mensagem).replace(",", ".")
    return float(valor)

def pausar():
    input("\nPressione ENTER para continuar...")

def imprimir_registros(registros, mensagem_vazia):
    if len(registros) == 0:
        print(mensagem_vazia)
        return

    for registro in registros:
        print(registro)

def mostrar_menu():
    print("\n==============================")
    print("SISTEMA DE ESTOQUE E VENDAS")
    print("==============================")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Remover cliente")
    print("5 - Cadastrar produto")
    print("6 - Listar produtos")
    print("7 - Buscar produto")
    print("8 - Atualizar estoque")
    print("9 - Remover produto")
    print("10 - Listar produtos em ordem inversa")
    print("11 - Listar produtos ordenados por ID")
    print("12 - Buscar produto por ID usando Busca Binaria")
    print("13 - Realizar venda simples de exemplo")
    print("14 - Visualizar fila de vendas")
    print("15 - Visualizar primeira venda da fila")
    print("16 - Exibir valor total do estoque")
    print("17 - Exibir valor total das vendas")
    print("18 - Exibir clientes e valores totais gastos")
    print("19 - Exibir cliente que mais gastou")
    print("20 - Exibir produto mais vendido")
    print("21 - Desfazer ultima operacao")
    print("0 - Sair")


def executar_opcao(opcao, service):
    if opcao == 1:  
        nome = input("Digite o nome do cliente: ")
        cliente = service.cadastrar_cliente(nome)
        print(f"Cliente cadastrado com sucesso! Código: {cliente.codigo}, Nome: {cliente.nome}")
        

    elif opcao == 2:
        clientes = service.listar_clientes()
        imprimir_registros(clientes, "Nenhum cliente cadastrado.")

    elif opcao == 3:
        procurando = ler_inteiro("Digite o código do cliente que deseja buscar: ")
        cliente = service.buscar_cliente(procurando)
        if cliente:
            print(f"Cliente encontrado! Código: {cliente.codigo}, Nome: {cliente.nome}")
        else:
            print("Cliente não encontrado.")

    elif opcao == 4:
        codigo_removido = ler_inteiro("Digite o código do cliente que deseja remover: ")
        cliente_removido = service.remover_cliente(codigo_removido)
        if cliente_removido:
            print(f"Cliente removido com sucesso! Código: {cliente_removido.codigo}, Nome: {cliente_removido.nome}")
        else:
            print("Cliente não encontrado ou lista de clientes vazia.")

    elif opcao == 5:
        nome = input("Digite o nome do produto: ")
        preco = ler_float("Digite o preço do produto: ")
        quantidade = ler_inteiro("Digite a quantidade em estoque do produto: ")
        produto = service.cadastrar_produto(nome, preco, quantidade)
        print(f"Produto cadastrado com sucesso! Código: {produto.codigo}, Nome: {produto.nome}, Preço: {produto.preco}, Quantidade: {produto.quantidade}")
        

    elif opcao == 6:
        pass

    elif opcao == 7:
        pass

    elif opcao == 8:
        pass

    elif opcao == 9:
        pass

    elif opcao == 10:
        pass

    elif opcao == 11:
        pass

    elif opcao == 12:
        pass

    elif opcao == 13:
        pass

    elif opcao == 14:
        pass

    elif opcao == 15:
        pass

    elif opcao == 16:
        pass

    elif opcao == 17:
        pass

    elif opcao == 18:
        pass

    elif opcao == 19:
        pass

    elif opcao == 20:
        pass

    elif opcao == 21:
        pass

    else:
        print("Opcao invalida. Tente novamente.")

def main():
    service = EstoqueService()

    while True:
        mostrar_menu()

        try:
            opcao = ler_inteiro("Escolha uma opcao: ")

            if opcao == 0:
                print("Sistema encerrado.")
                break

            executar_opcao(opcao, service)

        except ValueError as erro:
            print(f"Erro: {erro}")
        except IndexError as erro:
            print(f"Erro: {erro}")
        except NotImplementedError as erro:
            print(f"Funcionalidade para completar: {erro}")

        pausar()

if __name__ == "__main__":
    main()
