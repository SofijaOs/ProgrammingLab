class CSVFile():
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return 'CSVFile{}.'.format(self.name)

    def get_data(self):
        lista= []
        f=open(self.name, 'r')
        next(f)         #con next saltiamo la prima riga 
        for line in f:
            line = line.strip()  # Rimuovi eventuali spazi bianchi dai lati
            if line :  # Salta le righe vuote
                elementi = line.split(',')  # Dividi la riga usando la virgola come separatore
                lista.append(elementi)
        return lista



class NumericalCSVFile(CSVFile):

    def get_data(self):   #bisogna chiamare con lo stesso attributo della classe base per sovrascriverlo. controllare cosa vuol dire sovrascrivere 
        original=super().get_data()
        numerical_data=[]
        error_count = 0
        
        for line in original:
            try:
                numerical_line= [line[0]] + [float(x) for x in line[1:]]  #rappresenta il primo elemento della lista line
                numerical_data.append(numerical_line)  
            except ValueError as e :
                print(f'Errore nella linea {line}: {e}')
                error_count += 1

        print(f"Numero totale di errori di conversione: {error_count}")
        return numerical_data


#f=NumericalCSVFile('shampoo_sales.csv')
#numero=f.get_data()
#print(numero)

"""
Estendete l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in modo che 
converta automaticamente a numero float tutte le colonne tranne la prima (della data). 
Chiamate la get_data originale con super().get_data(), poi converite tutto a float.
A questo punto, aggiungete a mano questi due campi al file “shampoo_sales.csv”:
e gestite gli errori che verranno generati in modo che le linee vengano saltate senza 
bloccare il programma ma che venga stampato a schermo l’errore
"""
