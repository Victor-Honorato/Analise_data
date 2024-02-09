import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def criar_dataframe_exemplo():
    dados = {'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
             'Idade': [25, 30, 35, 40],
             'Salário': [50000, 60000, 75000, 90000]}
    return pd.DataFrame(dados)

def exibir_dados(dataframe, text_widget):
    text_widget.insert(tk.END, "\nDataFrame:\n")
    text_widget.insert(tk.END, str(dataframe) + "\n")

def calcular_estatisticas_descritivas(dataframe, text_widget):
    estatisticas_descritivas = dataframe.describe()
    text_widget.insert(tk.END, "\nEstatísticas Descritivas:\n")
    text_widget.insert(tk.END, str(estatisticas_descritivas) + "\n")

def filtrar_dados(dataframe, coluna, valor, text_widget):
    filtro = dataframe[coluna] == valor
    dados_filtrados = dataframe[filtro]
    text_widget.insert(tk.END, f"\nDados com {coluna} igual a {valor}:\n")
    text_widget.insert(tk.END, str(dados_filtrados) + "\n")
    return dados_filtrados

def visualizacao_grafica(dataframe):
    sns.set(style='whitegrid')
    plt.figure(figsize=(10, 6))

    sns.scatterplot(data=dataframe, x='Idade', y='Salário', hue='Nome', s=100, palette='viridis', edgecolor='w', linewidth=0.5)

    plt.title('Relação entre Idade e Salário', fontsize=16)
    plt.xlabel('Idade', fontsize=14)
    plt.ylabel('Salário', fontsize=14)
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.show()

def adicionar_funcionario(dataframe, nome, idade, salario, text_widget):
    novo_funcionario = pd.DataFrame({'Nome': [nome], 'Idade': [idade], 'Salário': [salario]})
    dataframe = pd.concat([dataframe, novo_funcionario], ignore_index=True)
    text_widget.insert(tk.END, f"\nNovo funcionário adicionado:\n{str(novo_funcionario)}\n")
    return dataframe

def construir_interface_grafica(df):
    root = tk.Tk()
    root.title("Gerenciador de Funcionários")

    text_widget = tk.Text(root, height=20, width=60)
    text_widget.pack(pady=10)

    button_frame = ttk.Frame(root)
    button_frame.pack()

    exibir_button = ttk.Button(button_frame, text="Exibir Dados", command=lambda: exibir_dados(df, text_widget))
    exibir_button.grid(row=0, column=0, padx=5)

    estatisticas_button = ttk.Button(button_frame, text="Estatísticas Descritivas",
                                     command=lambda: calcular_estatisticas_descritivas(df, text_widget))
    estatisticas_button.grid(row=0, column=1, padx=5)

    filtrar_button = ttk.Button(button_frame, text="Filtrar Dados",
                                command=lambda: filtrar_dados(df, 'Salário', 70000, text_widget))
    filtrar_button.grid(row=0, column=2, padx=5)

    grafico_button = ttk.Button(button_frame, text="Visualizar Gráfico", command=lambda: visualizacao_grafica(df))
    grafico_button.grid(row=0, column=3, padx=5)

    adicionar_button = ttk.Button(button_frame, text="Adicionar Funcionário",
                                  command=lambda: adicionar_funcionario(df, 'Novo', 25, 80000, text_widget))
    adicionar_button.grid(row=1, column=0, padx=5, pady=10)

    root.mainloop()

def main():
    df = criar_dataframe_exemplo()
    construir_interface_grafica(df)

if __name__ == "__main__":
    main()
