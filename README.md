                                          PROGRAMMING LAB 2024  PYTHON
                                          
Sito web del corso di Laboratorio di Programmazione per Intelligenza Artificiale e per Statistica dell'Università degli studi di Trieste.

                                                   INFORMAZIONI
Proprietario: Sofija Osmani.

Repository  esercizi proposti durante il corso di Programmazione Python condotto dal prof. Russo

                                                  INDICE DEGLI ESERCIZI
e1. Scrivete una funzione sum_list(my_list) che sommi tutti gli elementi di una lista.

e2. Scrivete una funzione sum_csv(file_name) che sommi tutti i valori delle vendite degli shampoo del file passato come argomento

e3.Create un oggetto CSVFile che rappresenti un file CSV, e che:

1) venga inizializzato sul nome del file csv, e
2) abbia un attributo “name” che ne contenga il nome
3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste, 
ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]

e4. Estendete l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in modo che converta automaticamente a numero float tutte le colonne tranne la prima (della data). 
Chiamate la get_data originale con super().get_data(), poi converite tutto a float.
A questo punto, aggiungete a mano questi due campi al file “shampoo_sales.csv" e gestite gli errori che verranno generati in modo che le linee vengano saltate senza 
bloccare il programma ma che venga stampato a schermo l’errore

e5.Modificate l’oggetto CSVFile della lezione precedente in modo che alzi un'eccezione se il nome del file non è una stringa (nell’ __init__() ).
Poi, modificate la funzione get_data() di CSVFile in modo da leggere solo un’ intervallo di righe del file*, aggiungendo gli argomenti start ed end
opzionali, controllandone la correttezza e sanitizzandoli se serve.     *inclusa l’intestazione, estremi inclusi, e partendo da “1”

e6.Creiamo un oggetto IncrementModel che estenda Model e che implementi il metodo predict() come spiegato nelle slides precedenti.
L’input del metodo predict() e’ una lista di valori per gli n mesi passati

e7.Estendete il modello della lezione precedente IncrementModel come FitIncrementModel, andando ad implementare il metodo fit().
Il fit deve, come appena descritto, calcolare l’incremento medio su tutto il dataset e salvarlo da qualche parte (es: self.global_avg_increment).
Poi sovrascrivete il metodo predict() in modo che usi l’incremento medio su tutto il dataset come descritto nelle slides precedenti.
                 
