def get_quarter(month):
    """Retorna o trimestre do ano com base no mês fornecido."""
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12")
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4
