import os

def exibir_menu():
    print("Menu de Seleção:")
    print("1. Executar Script 1")
    print("2. Executar Script 2")
    print("3. Sair")

def executar_script(nome_script):
    try:
        # Importa o módulo do script
        modulo = __import__(f'urnas.{nome_script}', fromlist=['main'])
        # Chama a função main() do módulo
        modulo.main()
    except ImportError:
        print(f"Erro: O script {nome_script} não foi encontrado.")
    except AttributeError:
        print(f"Erro: O script {nome_script} não possui uma função main().")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            executar_script("aval")
        elif opcao == "2":
            executar_script("godfather")
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
else :
    main()