#analisando clientes
#passo a passo do projeto
#passo 0: entender o desafio da empresa
#passo 1: importar a base de dados
#passo 2: tratar e preparar a base de dados para a inteligencia aritificial
#passo 3: criar o modelo de previsão ou modelo de IA
#passo 4: avaliar e escolher o melhor modelo
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
#importando a IA
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
tabela = pd.read_csv("clientes.csv")
#modificando as profissões da tabela as atribuindo por numeros
codificador_profissão = LabelEncoder()

tabela["profissao"] = codificador_profissão.fit_transform(tabela["profissao"])

codificador_mix = LabelEncoder()
tabela["mix_credito"] = codificador_mix.fit_tranform(tabela["mix_credito"])

codificador_comportamento = LabelEncoder()
tabela["comportamento_pagamento"] = codificador_comportamento.fit_transform(tabela["comportamento_pagamento"])


#como funciona a criação de uma IA
# Y é quem eu vou prever e X é quem eu vou usar para fazer a previsão
y = tabela["score_credito"]
x = tabela.drop(columns = "score_credito")
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3)
#criar a IA (modelo)
modelo_arvoredecisão = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

#treinar a IA (modelo)
modelo_arvoredecisão.fit(x_treino,y_treino)
modelo_knn.fit(x_treino,y_treino)

display(tabela)
