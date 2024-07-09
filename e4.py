#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#1) venga inizializzato sul nome del file csv, e
#2) abbia un attributo “name” che ne contenga il nome
#3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste, 
#ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]


class CsvFile():
    def __init__(self,nome):
        self.nome=nome

    def __str__(self):
        return 'CsvFile{}.'.format(self.nome)

    def get_data(self):
        lista= []
        f=open(self.nome, 'r')
        for line in f:
            line = line.strip()  # Rimuovi eventuali spazi bianchi dai lati
            if line:  # Salta le righe vuote
                elementi = line.split(',')  # Dividi la riga usando la virgola come separatore
                lista.append(elementi)
        return lista 
        
        
        
        
        


nomefile=CsvFile('shampoo_sales.csv')
nomefile.get_data()
print(nomefile.nome)
print(nomefile.get_data())