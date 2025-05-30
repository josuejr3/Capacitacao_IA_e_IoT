# -*- coding: utf-8 -*-
"""Cópia de Código Aula 16 - IA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vB0UkvPfonpgVdnOch3_WiNu1HL7EqCX
"""

import pandas as pd
from seaborn import load_dataset

# Seaborn é uma biblioteca de visualização de dados baseada no matplotlib

# O seaborn possui vários datasets

df = load_dataset("penguins")
df.head(10)

df.info() # Dtype - são os tipos categóricos
df.shape # dimensões do dataset
df.describe() # fornece algumas informações à respeito do dataset

"""Tratamento de valores NaN"""

df = df.dropna() # exclui as linhas com valores NaN
# a atribuição é feita para que ele não crie uma cópia, mas altere o dataset original
df.shape

"""OneHotEncoder"""

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer

make_column_transformer = make_column_transformer((OneHotEncoder(), ['island', 'sex']), remainder="passthrough")
# atributo reminder mantém as colunas que não foram alterados
# se não for usado, ele deixará somente as colunas geradas por island e sex

# a coluna island virou as três primeiras colunas
# as últimas duas colunas viraram o sexo masculino e feminino

# consigo colocar o nome das colunas
df = make_column_transformer.fit_transform(df)
df = pd.DataFrame(data=df)

df

"""LabelEncoder"""

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
df[5] = label_encoder.fit_transform(df[5])

# O Y pode ser categorico, menos em redes neurais

df

"""Separando os dados"""

# escolhe o valor de Y - classes
y = df[5]

# remove ela do dataframe (o axis 1 significa que o drop será da coluna)
X = df.drop(5, axis=1) # copia (dataset está intacto)

"""Separando dados de treinamento e teste

"""

from sklearn.model_selection import train_test_split

# separa os conjuntos de teste e treino
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=None, stratify=y)

"""Algoritmos de Árvores de decisão e KNN - Treinamento"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

model1 = DecisionTreeClassifier(criterion="entropy")
model2 = KNeighborsClassifier(n_neighbors=3, metric="euclidean", algorithm="brute")
model3 = DecisionTreeClassifier(max_depth=1)

model1.fit(X_train, y_train)
model2.fit(X_train, y_train)
model3.fit(X_train, y_train)

"""Predição dos dados"""

from sklearn import metrics

result1 = model1.predict(X_test)
result2 = model2.predict(X_test)
result3 = model3.predict(X_test)

acc1 = metrics.accuracy_score(result1, y_test)
show1 = round(acc1 * 100)
print("{}%".format(show1))


acc2 = metrics.accuracy_score(result2, y_test)
show2 = round(acc2 * 100)
print("{}%".format(show2))

acc3 = metrics.accuracy_score(result3, y_test)
show3 = round(acc3 * 100)
print("{}%".format(show3))