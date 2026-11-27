import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraPotencia:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Potência - Monofásica e Trifásica")
        master.geometry("380x480")
        master.config(padx=20, pady=20)
        
        # Título
        tk.Label(master, text="Calculadora de Potência Elétrica", font=("Arial", 14, "bold")).pack(pady=(0, 15))
        
        # Seleção do Tipo de Circuito (Monofásico ou Trifásico)
        tk.Label(master, text="Tipo de Circuito:", font=("Arial", 10)).pack(anchor="w")
        self.tipo_circuito = tk.StringVar(value="Monofásico")
        
        frame_radio = tk.Frame(master)
        frame_radio.pack(anchor="w", pady=5)
        tk.Radiobutton(frame_radio, text="Monofásico", variable=self.tipo_circuito, value="Monofásico", font=("Arial", 10)).pack(side=tk.LEFT, padx=(0, 15))
        tk.Radiobutton(frame_radio, text="Trifásico", variable=self.tipo_circuito, value="Trifásico", font=("Arial", 10)).pack(side=tk.LEFT)
        
        # Campo Tensão (V ou U)
        tk.Label(master, text="Tensão (Volts - V / U):", font=("Arial", 10)).pack(anchor="w", pady=(10, 0))
        self.entry_tensao = tk.Entry(master, font=("Arial", 12), width=25)
        self.entry_tensao.pack(pady=5)
        
        # Campo Corrente (I)
        tk.Label(master, text="Corrente (Ampères - I):", font=("Arial", 10)).pack(anchor="w", pady=(5, 0))
        self.entry_corrente = tk.Entry(master, font=("Arial", 12), width=25)
        self.entry_corrente.pack(pady=5)
        
        # Campo Ângulo (δ em graus)
        tk.Label(master, text="Ângulo do Fator de Potência (δ em graus):", font=("Arial", 10)).pack(anchor="w", pady=(5, 0))
        self.entry_angulo = tk.Entry(master, font=("Arial", 12), width=25)
        self.entry_angulo.pack(pady=5)
        
        # Botão Calcular
        self.btn_calcular = tk.Button(master, text="Calcular Potência", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.calcular)
        self.btn_calcular.pack(fill=tk.X, pady=(15, 10), ipady=5)
        
        # Rótulo de Resultado
        self.lbl_resultado = tk.Label(master, text="Resultado: ", font=("Arial", 12, "bold"), fg="#333333")
        self.lbl_resultado.pack(pady=10)

    def calcular(self):
        try:
            # Capturando os valores e convertendo para float
            tensao = float(self.entry_tensao.get())
            corrente = float(self.entry_corrente.get())
            angulo_graus = float(self.entry_angulo.get())
            
            # Cálculo do Fator de Potência: FP = cos(δ)
            # A função math.cos do Python espera o valor em radianos, por isso usamos math.radians()
            angulo_radianos = math.radians(angulo_graus)
            fp = math.cos(angulo_radianos)
            
            tipo = self.tipo_circuito.get()
            
            if tipo == "Monofásico":
                # Pm = V * I * FP
                potencia = tensao * corrente * fp
                nome_potencia = "Pm (Monofásica)"
            else:
                # Pt = √3 * U * I * FP
                potencia = math.sqrt(3) * tensao * corrente * fp
                nome_potencia = "Pt (Trifásica)"
                
            # Exibindo os resultados formatados
            resultado_texto = f"{nome_potencia}: {potencia:.2f} W\nFP (cos δ): {fp:.4f}"
            self.lbl_resultado.config(text=resultado_texto)
            
        except ValueError:
            messagebox.showerror("Erro de Entrada", "Por favor, preencha todos os campos com números válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraPotencia(root)
    root.mainloop()