Projeto de Análise de Dados – Titanic
Sobre o projeto

Este projeto foi desenvolvido como atividade final da disciplina de Python, com o objetivo de aplicar conceitos de Engenharia de Dados e Programação Orientada a Objetos.

O sistema realiza a leitura, limpeza, processamento e análise de dados de passageiros do Titanic, utilizando Python e bibliotecas de análise de dados.

Objetivos
Ler arquivos CSV utilizando Pandas.
Realizar limpeza e tratamento de dados.
Aplicar conceitos de Orientação a Objetos.
Calcular estatísticas e médias.
Realizar agrupamentos com groupby().
Criar gráficos para visualizar informações.
Desenvolver um menu interativo utilizando Python.
Base de dados

Dataset: Titanic – Machine Learning from Disaster.

Fonte: Kaggle.

Link: https://www.kaggle.com/competitions/titanic/data

O arquivo utilizado no projeto é titanic.csv, armazenado na pasta data/.

Tecnologias utilizadas
Python
Pandas
Matplotlib
Seaborn
Git e GitHub
Estrutura do projeto
text
ProjetoPython-2-2026/
│
├── data/
│   └── titanic.csv
│
├── src/
│   ├── __init__.py
│   └── analisador.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

Mostrar estatísticas gerais.
Gráfico de sobreviventes por sexo.
Histograma de distribuição de idades.
Gráfico de relação entre idade e tarifa.
Gráfico de sobreviventes por classe.
Encerrar o programa.
Análises realizadas
Média de idade dos passageiros.
Média das tarifas.
Quantidade de sobreviventes.
Sobreviventes por sexo.
Distribuição das idades.
Relação entre idade e tarifa.
Percentual de sobrevivência por classe.
Como executar o projeto
1. Instalar as dependências
bash
pip install -r requirements.txt

2. Executar o programa
bash
python main.py

Organização e desenvolvimento

O projeto utiliza Programação Orientada a Objetos, concentrando a lógica de leitura, limpeza e análise dos dados na classe AnalisadorDeDados, localizada em src/analisador.py.

O arquivo main.py é responsável pelo menu interativo e pela chamada dos métodos de análise.

Integrantes do grupo
João Gabriel Ribeiro
Airton 
Rodrigo
Ronald
Ricardo
Matheus
Disciplina ADS 2B

Projeto Final de Python – 2026.