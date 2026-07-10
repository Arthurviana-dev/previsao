# 📊 Previsão de Score de Crédito com Machine Learning

Este projeto de Inteligência Artificial foi desenvolvido com base nos ensinamentos da Hashtag Programação. O objetivo principal é analisar uma base histórica de clientes e criar um modelo preditivo capaz de classificar e prever o **Score de Crédito** dos clientes (Classificação entre categorias como *Good*, *Standard* ou *Poor*).

## 🧠 O que o projeto faz?
A partir de dados demográficos, financeiros e comportamentais dos clientes, o modelo identifica padrões ocultos que definem o risco de crédito. O script realiza o pré-processamento dos dados, treina algoritmos de Machine Learning e avalia qual inteligência artificial oferece a maior precisão (acurácia) para o negócio.

## 💾 Sobre a Base de Dados (`clientes.csv`)
A base contém registros detalhidos de clientes com as seguintes características fundamentais para a previsão:
* **Profissão** (Cientista, Professor, Engenheiro, etc.)
* **Informações Financeiras:** Salário anual, saldo final do mês, dívida total, investimentos mensais.
* **Histórico de Crédito:** Número de cartões, número de contas, dias de atraso, número de empréstimos.
* **Variável Alvo:** `score_credito` (O que a IA precisa aprender a prever).

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python** (Linguagem de programação principal)
* **Pandas**: Para a importação, limpeza e manipulação da base de dados.
* **Scikit-Learn (Sklearn)**:
  * `LabelEncoder`: Para transformar as variáveis de texto (como as profissões e o comportamento de pagamento) em valores numéricos compreensíveis para os modelos.
  * `train_test_split`: Para dividir os dados de forma justa entre treino (para a IA aprender) e teste (para validar a acurácia).
  * `RandomForestClassifier` e `KNeighborsClassifier`: Algoritmos de Machine Learning robustos utilizados para realizar os testes de classificação.

## 📊 Modelos de Machine Learning Testados
Durante o desenvolvimento, duas abordagens distintas foram testadas e comparadas:
1. **Random Forest (Floresta Aleatória)**
2. **K-Nearest Neighbors (KNN)**

*[Dica: Após rodar o seu código, verifique qual dos dois modelos teve a maior acurácia e adicione aqui qual foi o vencedor e a sua percentagem de acerto, ex: "O modelo Random Forest obteve o melhor desempenho com X% de acurácia!"]*

## 🚀 Como Executar o Projeto

1. Clone o repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/Arthurviana-dev/previsao.git](https://github.com/Arthurviana-dev/previsao.git)
