"""Exercicio 01"""

import pandas as pd
import matplotlib.pyplot as plt


def main():
    #1
    df = pd.read_csv("src/07-matplotlib/exercicios/classification_results_trial_0001 (1).csv")

    #2
    plt.figure()
    df["real_class"].value_counts().plot(kind="bar")
    plt.title("Contagem por Classe Real")
    plt.xlabel("Classe")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.show()

    #3
    plt.figure()
    df["predicted_class"].value_counts().plot(kind="bar")
    plt.title("Contagem por Classe Predita")
    plt.xlabel("Classe")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.show()

    #4
    plt.figure()
    plt.hist(df["prob_benign"], bins=20)
    plt.title("Distribuição de prob_benign")
    plt.xlabel("Probabilidade")
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.show()

    #5
    plt.figure()
    plt.hist(df["prob_malign"], bins=20)
    plt.title("Distribuição de prob_malign")
    plt.xlabel("Probabilidade")
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.show()

    #6
    df["correct"] = df["real_class"] == df["predicted_class"]

    acertos = df[df["correct"] == True]
    erros = df[df["correct"] == False]

    plt.figure()
    plt.scatter(acertos["prob_benign"], acertos["prob_malign"], label="Acertos")
    plt.scatter(erros["prob_benign"], erros["prob_malign"], label="Erros")
    plt.xlabel("prob_benign")
    plt.ylabel("prob_malign")
    plt.title("Scatter: prob_benign vs prob_malign")
    plt.legend()
    plt.tight_layout()
    plt.show()

    #7
    fp = df[
        (df["real_class"] == "benign") &
        (df["predicted_class"] == "malign")
    ]

    fn = df[
        (df["real_class"] == "malign") &
        (df["predicted_class"] == "benign")
    ]

    print("False Positives:", len(fp))
    print("False Negatives:", len(fn))

    plt.figure()
    plt.bar(["False Positive", "False Negative"], [len(fp), len(fn)])
    plt.title("Comparação entre FP e FN")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.show()

    #8
    print("\nEm contexto médico:")
    print("False Negative é mais preocupante, pois o modelo indica benigno\nquando na verdade é maligno, podendo atrasar tratamento. ")


if __name__ == "__main__":
    main()





