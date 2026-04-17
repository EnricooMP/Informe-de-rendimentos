# Analisador de Desempenho e Variação de Rendimentos 📈

Este script automatiza o cálculo da variação percentual de rendimentos entre períodos anuais e classifica o desempenho da empresa ou setor para direcionar a tomada de decisão estratégica.

## 🧮 Lógica de Cálculo

O programa utiliza a fórmula de variação percentual para comparar o ano base (2022) com o ano atual (2023):

$$Variação \% = \frac{V_{2} - V_{1}}{V_{1}} \times 100$$

## 🚥 Categorização de Performance

Com base no resultado, o sistema classifica a situação em quatro níveis de ação:

| Variação (%) | Status | Ação Sugerida |
| :--- | :--- | :--- |
| **>= 20%** | Crescimento Alto | Bonificação Total |
| **Entre 2% e 20%** | Crescimento Estável | Pequena Bonificação |
| **Entre -10% e 2%** | Alerta / Estagnação | Planejamento de Políticas de Incentivo |
| **<= -10%** | Queda Crítica | Corte de Gastos |

## ✨ Destaques Técnicos

- **Cálculo de Precisão:** Utiliza arredondamento em uma casa decimal (`:.1f`) para facilitar a leitura de relatórios.
- **Robustez de Entrada:** Tratamento de erros com `try/except` para evitar falhas caso valores não numéricos sejam inseridos.
- **Interatividade:** Interface de linha de comando (CLI) que permite múltiplas consultas em uma única sessão.

## 🚀 Como Executar

1. Tenha o Python 3.x instalado.
2. Execute o arquivo:
   ```bash
   python main.py
