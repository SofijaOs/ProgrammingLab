


def sum_csv(my_file):
    f=open('shampoo_sales.csv','r')
    for line in f:
        elementi= line.split(',')
        if elementi[0] !='Date':
            date = elementi[0]
            value= elementi[1]
            valori.append(value)
    lista=[float(i) for i in valori] #trasformo la lista valori in float per poter effettuare la somma 
    somma=0
    for numero in lista:
        somma +=numero
    return somma
        


#import csv
#valori =[]
#totale=sum_csv('shampoo_sales.csv')
#print(f'Il totale è: {totale}' )