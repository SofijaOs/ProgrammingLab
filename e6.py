class CSVFile():
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception('Errore: il nome del file deve essere una stringa!')
        self.name = name

    def __str__(self):
        return 'CSVFile({})'.format(self.name)

    def get_data(self, start=None, end=None):
        lista = []
        with open(self.name, 'r') as f:
            read = f.readlines()
        
        def sanitize_input(value):
            if isinstance(value, str):
                if value.isdigit():
                    return int(value)
                else:
                    raise ValueError(f"L'argomento {value} deve essere un numero intero positivo")
            return value

        start = sanitize_input(start)
        end = sanitize_input(end)

        if start is not None and (not isinstance(start, int) or start < 1):
            raise ValueError("L'argomento start deve essere un numero intero positivo")

        if end is not None and (not isinstance(end, int) or end < 1):
            raise ValueError("L'argomento end deve essere un numero intero positivo")

        if start is not None and end is not None and start > end:
            raise ValueError("Errore: start deve essere un valore minore o uguale a end!")

        # Numero totale di righe disponibili nel file (escludendo l'intestazione)
        total_lines = len(read) - 1

        if start is not None and start > total_lines:
            raise ValueError("Errore: start è maggiore del numero totale di righe nel file")

        if end is not None and end > total_lines:
            raise ValueError("Errore: end è maggiore del numero totale di righe nel file")

        start = start - 1 if start is not None else 0  # Converti da 1-based a 0-based
        end = end if end is not None else len(read)

        # Salta l'intestazione
        for i, line in enumerate(read):
            if i == 0:
                continue
            if i >= start and i < end:
                line = line.strip()  # Rimuovi eventuali spazi bianchi dai lati
                if line:  # Salta le righe vuote
                    elementi = line.split(',')  # Dividi la riga usando la virgola come separatore
                    lista.append(elementi)
            elif i >= end:
                break

        return lista




#f = CSVFile('shampoo_sales.csv')
#numero = f.get_data(start=5, end=4)  # Nota: start deve essere >= 1
#print(numero)
