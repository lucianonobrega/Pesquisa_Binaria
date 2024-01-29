from time import sleep

def pesquisa_binaria(lista, numero_itens_lista):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == numero:
            print(f"{numero} = {lista[meio]} ?")
            sleep(1)
            print("Sim!")
            sleep(1)
            print(f"Seu número: {numero} -> índice: {meio}")
            sleep(1)
            break
        elif lista[meio] > numero:
            print(f"{numero} = {lista[meio]} ?")
            sleep(1)
            print("Não.")
            fim = meio - 1
        else:
            print(f"{numero} = {lista[meio]} ?")
            sleep(1)
            print("Não.")
            inicio = meio + 1
    return None

if __name__ == "__main__":
    while True:
        try:
            numero_itens_lista = int(input("Digite o número de itens que deseja ter na sua lista: "))
            lista = [x for x in range(1, numero_itens_lista + 1)]
            numero = int(input("Digite o número que deseja saber a posição[índice]: "))
            pesquisa_binaria(lista, numero)
            input("Pressione ENTER para sair do programa.")
            break
        except ValueError as V:
            print(f"Ocorreu um erro: {V}.")