
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisadorDeDados:

    def __init__(self, caminho_arquivo):
        try:
            self.df = pd.read_csv(caminho_arquivo)

            # Limpeza dos dados
            self.df["Age"] = self.df["Age"].fillna(
                self.df["Age"].median()
            )

            self.df["Embarked"] = self.df["Embarked"].fillna(
                self.df["Embarked"].mode()[0]
            )

            self.df["Fare"] = self.df["Fare"].fillna(
                self.df["Fare"].median()
            )

            self.df = self.df.dropna()

            print("\nBase de dados carregada com sucesso!")
            print(f"Registros disponíveis: {len(self.df)}")

        except FileNotFoundError:
            print("Erro: arquivo CSV não encontrado.")
            self.df = None

        except Exception as erro:
            print(f"Erro ao carregar os dados: {erro}")
            self.df = None

    def mostrar_estatisticas(self):
        if self.df is None:
            return

        print("\n===== ESTATÍSTICAS GERAIS =====")
        print(self.df.describe())

        print("\nTotal de passageiros:")
        print(len(self.df))

        print("\nTotal de sobreviventes:")
        print(self.df["Survived"].sum())

        print("\nMédia de idade:")
        print(round(self.df["Age"].mean(), 2))

        print("\nMédia das tarifas:")
        print(round(self.df["Fare"].mean(), 2))

    def sobreviventes_por_sexo(self):
        if self.df is None:
            return

        dados = self.df.groupby("Sex")["Survived"].sum()

        plt.figure(figsize=(8, 5))
        dados.plot(kind="bar", color=["steelblue", "salmon"])

        plt.title("Quantidade de Sobreviventes por Sexo")
        plt.xlabel("Sexo")
        plt.ylabel("Quantidade de sobreviventes")

        plt.tight_layout()
        plt.show()

    def distribuicao_idades(self):
        if self.df is None:
            return

        plt.figure(figsize=(8, 5))

        sns.histplot(
            data=self.df,
            x="Age",
            bins=20,
            color="royalblue",
            kde=True
        )

        plt.title("Distribuição das Idades dos Passageiros")
        plt.xlabel("Idade")
        plt.ylabel("Quantidade de passageiros")

        plt.tight_layout()
        plt.show()

    def idade_e_tarifa(self):
        if self.df is None:
            return

        plt.figure(figsize=(8, 5))

        sns.scatterplot(
            data=self.df,
            x="Age",
            y="Fare",
            hue="Survived",
            palette="Set1"
        )

        plt.title("Relação entre Idade e Tarifa")
        plt.xlabel("Idade dos passageiros")
        plt.ylabel("Tarifa paga")

        plt.tight_layout()
        plt.show()

    def sobreviventes_por_classe(self):
        if self.df is None:
            return

        dados = self.df.groupby("Pclass")["Survived"].mean() * 100

        plt.figure(figsize=(8, 5))

        plt.plot(
            dados.index,
            dados.values,
            marker="o",
            color="green"
        )

        plt.title("Percentual de Sobreviventes por Classe")
        plt.xlabel("Classe do passageiro")
        plt.ylabel("Sobreviventes (%)")

        plt.xticks([1, 2, 3])
        plt.tight_layout()
        plt.show()
