def sum_list(my_list):
    # Controlla se la lista è vuota
    if not my_list:
        return None

    total = 0
    for element in my_list:
        total += element
    return total

# Esempio di utilizzo
lista1 = [1, 2, 3, 4, 5]
lista2 = []

somma1 = sum_list(lista1)
somma2 = sum_list(lista2)

print(f"La somma degli elementi della lista1 è: {somma1}")  # Output: La somma degli elementi della lista1 è: 15
print(f"La somma degli elementi della lista2 è: {somma2}")  # Output: La somma degli elementi della lista2 è: None
