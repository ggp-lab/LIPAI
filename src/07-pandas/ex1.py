"""Exercicio 01"""

import os
import pandas as pd

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "classification_results_trial_0001.csv")

#1
df = pd.read_csv(csv_path)

print("Distribuição de classes reais:")
class_counts = df["real_class"].value_counts()
print(class_counts)
print("\n")

# 2
erros = df[df["real_class"] != df["predicted_class"]]

print("Imagens com erro de predição:")
print(erros[["image_path", "real_class", "predicted_class"]])
print(f"\nTotal de erros: {len(erros)}\n")

# 3
erros_confiantes = erros[
    ((erros["predicted_class"] == "benign") & (erros["prob_benign"] >= 0.9)) |
    ((erros["predicted_class"] == "malign") & (erros["prob_malign"] >= 0.9))
]

print("Erros com alta confiança (>= 0.9):")
print(erros_confiantes[["image_path", "prob_benign", "prob_malign"]])
print(f"Total de erros confiantes: {len(erros_confiantes)}\n")

# 4
TP = len(df[(df["real_class"] == "malign") & (df["predicted_class"] == "malign")])
TN = len(df[(df["real_class"] == "benign") & (df["predicted_class"] == "benign")])
FP = len(df[(df["real_class"] == "benign") & (df["predicted_class"] == "malign")])
FN = len(df[(df["real_class"] == "malign") & (df["predicted_class"] == "benign")])

print("Matriz de Confusão:")
print(f"TP: {TP}")
print(f"TN: {TN}")
print(f"FP: {FP}")
print(f"FN: {FN}\n")

# 5
acuracia = (TP + TN) / (TP + TN + FP + FN)
precisao = TP / (TP + FP) if (TP + FP) != 0 else 0
recall = TP / (TP + FN) if (TP + FN) != 0 else 0
especificidade = TN / (TN + FP) if (TN + FP) != 0 else 0

print("Métricas:")
print(f"Acurácia: {acuracia:.4f}")
print(f"Precisão: {precisao:.4f}")
print(f"Recall: {recall:.4f}")
print(f"Especificidade: {especificidade:.4f}")
print("\n")

# 6
benign_menor_prob = df[df["real_class"] == "benign"] \
    .sort_values(by="prob_benign") \
    .head(5)

print("5 imagens benign com menor prob_benign:")
print(benign_menor_prob[["image_path", "prob_benign"]])
print("\n")

# 7
malign_maior_prob_benign = df[df["real_class"] == "malign"] \
    .sort_values(by="prob_benign", ascending=False) \
    .head(5)

print("5 imagens malign com maior prob_benign:")
print(malign_maior_prob_benign[["image_path", "prob_benign"]])
print("\n")