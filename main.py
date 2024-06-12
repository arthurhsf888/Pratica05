from quarter import get_quarter

def main():
    try:
        month = int(input("Digite o mês (1-12): "))
        quarter = get_quarter(month)
        print(f"O mês {month} está no {quarter}º trimestre.")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()
