
from src.analisador import AnalisadorDeDados


def menu():
    print("\n" + "=" * 45)
    print("       SISTEMA DE ANÁLISE DE DADOS")
    print("                TITANIC")
    print("=" * 45)

    print("[1] Mostrar estatísticas gerais")
    print("[2] Gráfico de sobreviventes por sexo")
    print("[3] Histograma de distribuição de idades")
    print("[4] Gráfico de idade e tarifa")
    print("[5] Gráfico de sobreviventes por classe")
    print("[0] Sair")

    print("=" * 45)


def main():
    analisador = AnalisadorDeDados("data/titanic.csv")

    if analisador.df is None:
        print("Não foi possível iniciar o sistema.")
        return

    while True:
        menu()

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                analisador.mostrar_estatisticas()

            elif opcao == 2:
                analisador.sobreviventes_por_sexo()

            elif opcao == 3:
                analisador.distribuicao_idades()

            elif opcao == 4:
                analisador.idade_e_tarifa()

            elif opcao == 5:
                analisador.sobreviventes_por_classe()

            elif opcao == 0:
                print("\nSistema encerrado. Até mais!")
                break

            else:
                print("\nOpção inválida! Escolha entre 0 e 5.")

        except ValueError:
            print("\nErro! Digite somente números.")

        except Exception as erro:
            print(f"\nOcorreu um erro: {erro}")


if __name__ == "__main__":
    main()
