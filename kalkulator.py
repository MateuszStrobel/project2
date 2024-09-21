def calculator():
    print("Witaj w prostym kalkulatorze (zakres: 0-10)!")

    # Pobranie pierwszej liczby od użytkownika
    try:
        num1 = int(input("Podaj pierwszą liczbę (0-10): "))
        if num1 < 0 or num1 > 10:
            raise ValueError("Liczba poza zakresem")
    except ValueError as e:
        print("Niepoprawna liczba! Wprowadź liczbę z zakresu 0-10.")
        return

    # Pobranie operacji (+ lub -)
    operation = input("Podaj operację (+ lub -): ")
    if operation not in ['+', '-']:
        print("Niepoprawna operacja! Użyj tylko '+' lub '-'.")
        return

    # Pobranie drugiej liczby od użytkownika
    try:
        num2 = int(input("Podaj drugą liczbę (0-10): "))
        if num2 < 0 or num2 > 10:
            raise ValueError("Liczba poza zakresem")
    except ValueError:
        print("Niepoprawna liczba! Wprowadź liczbę z zakresu 0-10.")
        return

    # Obliczenie wyniku
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2

    # Wyświetlenie wyniku, jeśli znajduje się w zakresie
    if result < 0 or result > 10:
        print("Wynik poza zakresem (0-10):", result)
    else:
        print(f"Wynik: {num1} {operation} {num2} = {result}")


# Uruchomienie kalkulatora
calculator()
