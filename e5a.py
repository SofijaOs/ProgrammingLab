class CSVFile():
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return 'CSVFile{}.'.format(self.name)

    def get_data(self):
        lista= []
        try:
            f=open(self.name, 'r')
            next(f)         #con next saltiamo la prima riga 
            for line in f:
                line = line.strip()  # Rimuovi eventuali spazi bianchi dai lati
                if line  :  # Salta le righe vuote
                    elementi = line.split(',')  # Dividi la riga usando la virgola come separatore
                    lista.append(elementi)
            
             
        except Exception as e:
            
            print('Errore. Il file non può essere aperto')
            print('Tipo errore:{}.'.format(e))
        
        return lista


#f=NumericalCSVFile('shampoo_sales.csv')
#numero=f.original_get_data()
#print(numero)
