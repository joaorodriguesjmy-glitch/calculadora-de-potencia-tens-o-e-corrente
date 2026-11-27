# Calculadora de Potência Elétrica

Aplicação desktop em Python com interface gráfica (`tkinter`) para calcular a potência ativa e o fator de potência em circuitos **monofásicos** e **trifásicos**.

## Funcionalidades

- Cálculo de potência para circuitos **monofásicos** ($P_m = V \cdot I \cdot \cos(\delta)$) e **trifásicos** ($P_t = \sqrt{3} \cdot U \cdot I \cdot \cos(\delta)$).
- Conversão automática do ângulo de graus para radianos através de `math.radians()` e `math.cos()`.
- Exibição da potência em Watts (`W`) e do fator de potência ($\cos \delta$) com formatação decimal.
- Utiliza apenas módulos nativos do Python (`tkinter` e `math`), sem necessidade de instalar pacotes adicionais.

## Como executar

1. Garante que tens o **Python 3** instalado no computador.
2. Abre a pasta do projeto no **VS Code**.
3. Executa o ficheiro `calculadora_potencia.py` clicando em **Play** (`▷`) ou correndo no terminal:
   ```bash
   python calculadora_potencia.py