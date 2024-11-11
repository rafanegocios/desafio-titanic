import pandas as pd

#classe para manipular arquivos csv
class CSVHandler:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)


    def get_summary(self):
        """Retorna um resumo estatístico da tabela de sobreviventes do titanic"""
        df = self.data.describe()
        return df.to_dict()
    

    def get_survival(self):
        """ Retorna a taxa de sobrevivência global (passageiro que sobreviveram em relação ao total) """
        total_passengers = len(self.data)
        survivors = self.data['Survived'].sum()
        survival_rate = (survivors / total_passengers) * 100
        return survival_rate
    

    def get_average_survival_rate(self, group_column):
        """
        Retorna a taxa de sobrevivência média agrupada por
        uma coluna especificada ou geral
        """
        columns_lower = {col.lower(): col for col in self.data.columns}
        if group_column.lower() != 'all' and group_column.lower() not in columns_lower:
            raise KeyError(f"A coluna '{group_column}' não existe na base de dados.")

        if group_column.lower() == 'all':
            categorical_columns = [col for col in self.data.columns if col != 'Survived']
            results = {}

            for column in categorical_columns:
                survival_rate_by_group = self.data.groupby(column)['Survived'].mean() * 100
                result = survival_rate_by_group.reset_index()
                result.columns = [column, 'TMS(%)'] 
                results[column] = result.to_dict(orient='records') 
            return results  

        else:
            group_column_correct = columns_lower[group_column.lower()]
            survival_rate_by_group = self.data.groupby(group_column_correct)['Survived'].mean() * 100
            result = survival_rate_by_group.reset_index()
            result.columns = [group_column_correct, 'Survival Rate (%)']
            return result.to_dict(orient='records')

 
    def post_clean_data(self,data):
        """
        Recebe um conjunto de dados em formato JSON e retorna o mesmo
        conjunto de dados com algumas limpezas realizadas
        """
        df = pd.DataFrame(data)
        df = df.dropna(subset=["Embarked"])

        Q1 = df["Fare"].quantile(0.25)
        Q3 = df["Fare"].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df["Fare"] >= lower_bound) & (df["Fare"] <= upper_bound)]
        df["Age"] = df["Age"].fillna(df["Age"].mean())
        return df.to_dict(orient='records')


        
    def get_correlation(self):
        """
        Retorna a matriz de correlação entre as variáveis
        numéricas, ajudando a entender quais variáveis podem ter uma
        relação forte entre si.
        """
        numeric_columns = self.data.select_dtypes(include=['number'])
        correlation_matrix = numeric_columns.corr()
        return correlation_matrix.to_dict()