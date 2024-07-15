class Model():
    def fit(self,data):
        raise NotImplementedError ('Metodo non implementato')

    def predict (self,data):
        raise NotImplementedError ('Metodo non implementato')


class IncrementModel(Model):
    def predict (self,data):
        if not isinstance(data, list)  or len(data)<2:
            raise TypeError("L'input dovrebbe essere una lista di almeno due elementi")

        prev_value= data[0]
        incremento=[] #lista vuota

        for i in range(1,len(data)):
            increment= data[i]-prev_value
            incremento.append(increment)
            prev_value=data[i]

        media= sum(incremento)/len(incremento)
        predizione= media + data[-1]

        return predizione 
        
    #Creiamo un oggetto IncrementModel che estenda Model e che implementi il 
    #metodo predict() come spiegato nelle slides precedenti.
    #L’input del metodo predict() e’ una lista di valori per gli n mesi passati
