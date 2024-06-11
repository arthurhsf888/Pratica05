import os
import random
from cod import is_first_semester

def clear_screen():
    if os.name == 'nt':  #Window
        os.system('cls')
    else:  #Unix/Linux/Mac
        os.system('clear')

def main():
    # Testes com meses aleatórios
    random_months = [random.randint(1, 12) for _ in range(5)]
    
    for month in random_months:
        result = is_first_semester(month)
        print(f"Month: {month}, is_first_semester: {result}")

if __name__ == '__main__':
    main()
