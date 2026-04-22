while True:
    try:
        v1 = float(input("\nInforme os rendimentos de 2022: "))
        v2 = float(input("\nInforme os rendimentos de 2023: "))
        if v1 == 0:
          print("Erro: O rendimento de 2022 não pode ser zero para calcular a variação.")
          continue
    except ValueError:
        print("Erro: insira apenas numeros!")
        continue

    variação_percentual = ((v2 - v1) / v1) * 100

    if variação_percentual >= 20:
        print(f"\nO rendimento foi de {variação_percentual:.1f}%, Bonificação total")
    elif 2 <= variação_percentual <= 20:
        print(f"\nO rendimento foi de {variação_percentual:.1f}%, Pequena bonificação")
    elif -10 <= variação_percentual <= 2:
         print(f"\nO rendimento foi de {variação_percentual:.1f}%, Planejamento de politicas de incentivo de vendas")
    elif variação_percentual <= -10:
        print(f"\nO rendimento foi de {variação_percentual:.1f}%, Corte de gastos")
    else:
        print("Valor inválido")
    
    pergunta = input("\nDeseja informar outra variação de rendimento? (s/n): ").lower().strip()
    if pergunta != 's':
        print("Encerrando relatório. Até logo!")
        break
       
