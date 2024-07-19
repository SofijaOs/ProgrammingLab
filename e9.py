#Estendete il modello della lezione precedente IncrementModel come 
#FitIncrementModel, andando ad implementare il metodo fit().
#Il fit deve, come appena descritto, calcolare l’incremento medio su tutto il 
#dataset e salvarlo da qualche parte (es: self.global_avg_increment).
#Poi sovrascrivete il metodo predict() in modo che usi l’incremento 
#medio su tutto il dataset come descritto nelle slides precedenti.


class Model():
    def fit(self,data):
        raise NotImplementedError ('Metodo non implementato')

    def predict (self,data):
        raise NotImplementedError ('Metodo non implementato')



class TrendModel(Model):
    def __init__(self,window=3):
        self.window=window

    def validate_data(self, data):
        if not isinstance(data, list):
            raise TypeError("I dati di input devono essere una lista.")
        if len(data) < self.window:
            raise ValueError(f"Il modello richiede almeno {self.window} dati.")

    
    def compute_avg_variation(self, data):
        variations=[]
        item_prev=None
        for item in data:
            if item_prev is not None:
                variations.append(item-item_prev)
            item_prev= item

        avg_variation=sum(variations)/len(variations)
        return avg_variation



    def predict (self,data):
        self.validate_data (data)
        prediction= data[-1]+self.compute_avg_variation(data)
        return prediction 


class FitTrendModel(TrendModel):

     def fit (self,data):
         self.historical_avg_variation=self.compute_avg_variation(data)

     def predict(self,data):
         try:
            self.historical_avg_variation
         except AttributeError:
            raise Exception('Il modello non è fittato')
            
        
         
         prediction= data[-1]+ ((self.historical_avg_variation + self.compute_avg_variation(data))/2)
         return prediction

#data = [8, 19, 31, 41, 50, 52, 60]
#prediction = 68

#from matplotlib import pyplot
#pyplot.plot(data+[prediction], color='tab:red')
#pyplot.plot(data,color='tab:blue')
#pyplot.show()