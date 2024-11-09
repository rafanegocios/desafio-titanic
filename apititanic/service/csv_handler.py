import pandas as pd

#classe para manipular arquivos csv
class CSVHandler:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    # endpoint 1
    def get_summary(self):
        #a função describe no pandas retorna a media, variança, max, min, desvio padrao, os dados estatisticos de valores numericos
        df = self.data.describe()
        return df.to_dict()
    
    #endpoint 2 
    def get_survival(self):
        total_passengers = len(self.data)
        survivors = self.data['Survived'].sum()
        # Calcular a taxa de sobrevivência global
        survival_rate = (survivors / total_passengers) * 100
        return survival_rate
    

