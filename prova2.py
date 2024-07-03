def EstacaoAno(dia, mes):
    if mes in (1, 2):
        return 'VERAO'
    elif mes == 3:
        if dia < 21:
            return 'VERAO'
        else:
            return 'OUTONO'
    elif mes in (4, 5):
        return 'OUTONO'
    elif mes == 6:
        if dia < 21:
            return 'OUTONO'
        else:
            return 'INVERNO'
    elif mes in (7, 8):
        return 'INVERNO'
    elif mes == 9:
        if dia < 21:
            return 'INVERNO'
        else:
            return 'PRIMAVERA'
    elif mes in (10, 11):
        return 'PRIMAVERA'
    elif mes == 12:
        if dia < 21:
            return 'PRIMAVERA'
        else:
            return 'VERAO'


try:
    dia = int(input("Digite o dia (1-31): "))
    mes = int(input("Digite o mês (1-12): "))
    
    
    if 1 <= dia <= 31 and 1 <= mes <= 12:
        estacao = EstacaoAno(dia, mes)
        print(f"A estação para {dia}/{mes} é {estacao}.")
    else:
        print("Por favor, digite valores válidos para dia (1-31) e mês (1-12).")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números inteiros para dia e mês.")