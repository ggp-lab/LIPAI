"""Exercicio 02"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def main():

    #1
    caminho_script = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(caminho_script, "metrics.csv")

    df = pd.read_csv(caminho_csv)

    #2
    plt.figure()
    plt.plot(df.index, df["train_loss"], label="Train Loss")
    plt.plot(df.index, df["val_loss"], label="Validation Loss")
    plt.xlabel("Épocas")
    plt.ylabel("Loss")
    plt.title("Curvas de Loss (Treino vs Validação)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    #3
    plt.figure()
    plt.plot(df.index, df["train_acc"], label="Train Accuracy")
    plt.plot(df.index, df["val_acc"], label="Validation Accuracy")
    plt.xlabel("Épocas")
    plt.ylabel("Accuracy")
    plt.title("Curvas de Accuracy (Treino vs Validação)")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()