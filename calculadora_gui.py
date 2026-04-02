import tkinter as tk
from tkinter import font
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Variável para armazenar a expressão
        self.expressao = ""
        
        # Cria o display
        self.criar_display()
        
        # Cria os botões
        self.criar_botoes()
        
    def criar_display(self):
        """Cria o visor da calculadora"""
        frame_display = tk.Frame(self.root, bg="#f0f0f0")
        frame_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=False)
        
        self.display = tk.Entry(
            frame_display,
            font=("Arial", 28),
            justify=tk.RIGHT,
            bd=2,
            relief=tk.SUNKEN,
            bg="white"
        )
        self.display.pack(fill=tk.BOTH, expand=True, ipady=20)
        
    def criar_botoes(self):
        """Cria os botões da calculadora"""
        frame_botoes = tk.Frame(self.root, bg="#f0f0f0")
        frame_botoes.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Layout dos botões
        botoes = [
            ["C", "←", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "√"]
        ]
        
        for linha_idx, linha in enumerate(botoes):
            for col_idx, texto in enumerate(linha):
                self.criar_botao(frame_botoes, texto, linha_idx, col_idx)
    
    def criar_botao(self, frame, texto, linha, coluna):
        """Cria um botão individual"""
        # Cores diferentes para diferentes tipos de botão
        if texto in ["=", "√"]:
            cor_bg = "#4CAF50"
            cor_fg = "white"
        elif texto in ["C", "←"]:
            cor_bg = "#f44336"
            cor_fg = "white"
        elif texto in ["÷", "×", "-", "+"]:
            cor_bg = "#FF9800"
            cor_fg = "white"
        else:
            cor_bg = "#e0e0e0"
            cor_fg = "black"
        
        botao = tk.Button(
            frame,
            text=texto,
            font=("Arial", 20, "bold"),
            bg=cor_bg,
            fg=cor_fg,
            command=lambda: self.ao_clicar(texto),
            activebackground="#ddd",
            relief=tk.RAISED,
            bd=2
        )
        
        botao.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)
        
        # Define tamanho igual para todas as células
        frame.grid_rowconfigure(linha, weight=1)
        frame.grid_columnconfigure(coluna, weight=1)
    
    def ao_clicar(self, texto):
        """Processa o clique nos botões"""
        try:
            if texto == "C":
                # Limpar tela
                self.expressao = ""
                self.atualizar_display()
            
            elif texto == "←":
                # Deletar último caractere
                self.expressao = self.expressao[:-1]
                self.atualizar_display()
            
            elif texto == "=":
                # Calcular resultado
                self.expressao = str(eval(self.expressao))
                self.atualizar_display()
            
            elif texto == "√":
                # Raiz quadrada
                resultado = float(self.expressao) ** 0.5
                self.expressao = str(resultado)
                self.atualizar_display()
            
            elif texto == "÷":
                # Divisão
                self.expressao += "/"
                self.atualizar_display()
            
            elif texto == "×":
                # Multiplicação
                self.expressao += "*"
                self.atualizar_display()
            
            else:
                # Adicionar número ou operador
                self.expressao += texto
                self.atualizar_display()
        
        except:
            messagebox.showerror("Erro", "Expressão inválida!")
            self.expressao = ""
            self.atualizar_display()
    
    def atualizar_display(self):
        """Atualiza o visor da calculadora"""
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expressao)


def main():
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main()
