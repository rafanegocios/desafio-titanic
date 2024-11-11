# desafio-titanic

## Summary Endpoint

### Endpoint
`GET /api/summary/`

### Descrição
Este endpoint retorna um resumo estatístico de diferentes variáveis analisadas.

---

### Métodos Permitidos
- `GET`

---

### Resposta de Sucesso
#### Código de Status
`200 OK`

#### Cabeçalhos
- `Content-Type: application/json`
- `Vary: Accept`

#### Corpo da Resposta
```json
{
    "status": "success",
    "data": {
        "PassengerId": {
            "count": 891.0,
            "mean": 446.0,
            "std": 257.3538420152301,
            "min": 1.0,
            "25%": 223.5,
            "50%": 446.0,
            "75%": 668.5,
            "max": 891.0
        },
        "Survived": {
            "count": 891.0,
            "mean": 0.3838383838383838,
            "std": 0.4865924542648575,
            "min": 0.0,
            "25%": 0.0,
            "50%": 0.0,
            "75%": 1.0,
            "max": 1.0
        },
        "Pclass": {
            "count": 891.0,
            "mean": 2.308641975308642,
            "std": 0.836071240977049,
            "min": 1.0,
            "25%": 2.0,
            "50%": 3.0,
            "75%": 3.0,
            "max": 3.0
        },
        "Age": {
            "count": 714.0,
            "mean": 29.69911764705882,
            "std": 14.526497332334042,
            "min": 0.42,
            "25%": 20.125,
            "50%": 28.0,
            "75%": 38.0,
            "max": 80.0
        },
        "SibSp": {
            "count": 891.0,
            "mean": 0.5230078563411896,
            "std": 1.1027434322934317,
            "min": 0.0,
            "25%": 0.0,
            "50%": 0.0,
            "75%": 1.0,
            "max": 8.0
        },
        "Parch": {
            "count": 891.0,
            "mean": 0.38159371492704824,
            "std": 0.8060572211299483,
            "min": 0.0,
            "25%": 0.0,
            "50%": 0.0,
            "75%": 0.0,
            "max": 6.0
        },
        "Fare": {
            "count": 891.0,
            "mean": 32.204207968574636,
            "std": 49.6934285971809,
            "min": 0.0,
            "25%": 7.9104,
            "50%": 14.4542,
            "75%": 31.0,
            "max": 512.3292
        }
    }
}
```


## Survival Rate Endpoint

### Endpoint
`GET /api/survival_rate`

### Descrição
Este endpoint retorna a taxa de sobrevivência dos dados analisados.

---

### Métodos Permitidos
- `GET`

---

### Resposta de Sucesso
#### Código de Status
`200 OK`

#### Cabeçalhos
- `Content-Type: application/json`
- `Vary: Accept`

#### Corpo da Resposta
```json
{
    "status": "sucess",
    "data": {
        "survival_rate": 38.38383838383838
    }
}
```


## Average Survival Rate by Sex Endpoint

### Endpoint
`GET api/grouped/<str:column>/`

### Descrição
Este endpoint retorna a taxa média de sobrevivência agrupada por uma coluna específica ou todas.

---

### Métodos Permitidos
- `GET`

---

### Resposta de Sucesso
#### Código de Status
`200 OK`

#### Cabeçalhos
- `Content-Type: application/json`
- `Vary: Accept`

#### Corpo da Resposta
```json
{
    "status": "success",
    "column": "column",
    "taxa média de sobrevivencia": [ ]
}
```


#### Exemplo de Corpo da Resposta
`GET api/grouped/sex/`
```json
{
    "status": "success",
    "column": "sex",
    "taxa média de sobrevivencia": [
        {
            "Sex": "female",
            "Survival Rate (%)": 74.20382165605095
        },
        {
            "Sex": "male",
            "Survival Rate (%)": 18.890814558058924
        }
    ]
}
```


## Clean Data Endpoint

### Endpoint
`POST /api/clean_data/`

### Descrição
Este endpoint retorna os dados limpos após o processamento, com informações completas sobre os passageiros.

---

### Métodos Permitidos
- `POST`

---

### Resposta de Sucesso
#### Código de Status
`200 OK`

#### Cabeçalhos
- `Content-Type: application/json`
- `Vary: Accept`

#### Corpo da Requisição 
```json
[
  {
    "PassengerId": 1,
    "Survived": true,
    "Pclass": 1,
    "Name": "John Doe",
    "Sex": "male",
    "Age":23,
    "SibSp": 0,
    "Parch": 0,
    "Ticket": "PC 17599",
    "Fare": 71.2833,
    "Cabin": "C85",
    "Embarked": "S"
  },
  {
    "PassengerId": 2,
    "Survived": false,
    "Pclass": 3,
    "Name": "Jane Smith",
    "Sex": "female",
    "Age": 24,
    "SibSp": 1,
    "Parch": 0,
    "Ticket": "A/5 21171",
    "Fare": 7.25,
    "Cabin": "F31",
    "Embarked": "S"
  },
  {
    "PassengerId": 3,
    "Survived": true,
    "Pclass": 2,
    "Name": "Emily Brown",
    "Sex": "female",
    "Age": 32,
    "SibSp": 0,
    "Parch": 2,
    "Ticket": "248738",
    "Fare": 13,
    "Cabin": "F33",
    "Embarked": "Q"
  }
]

```
#### Corpo da Resposta
```json
{
    "status": "success",
    "data": [
        {
            "PassengerId": 1,
            "Survived": true,
            "Pclass": 1,
            "Name": "John Doe",
            "Sex": "male",
            "Age": 23.0,
            "SibSp": 0,
            "Parch": 0,
            "Ticket": "PC 17599",
            "Fare": 71.2833,
            "Cabin": "C85",
            "Embarked": "S"
        },
        {
            "PassengerId": 2,
            "Survived": false,
            "Pclass": 3,
            "Name": "Jane Smith",
            "Sex": "female",
            "Age": 24.0,
            "SibSp": 1,
            "Parch": 0,
            "Ticket": "A/5 21171",
            "Fare": 7.25,
            "Cabin": "F31",
            "Embarked": "S"
        },
        {
            "PassengerId": 3,
            "Survived": true,
            "Pclass": 2,
            "Name": "Emily Brown",
            "Sex": "female",
            "Age": 32.0,
            "SibSp": 0,
            "Parch": 2,
            "Ticket": "248738",
            "Fare": 13.0,
            "Cabin": "F33",
            "Embarked": "Q"
        }
    ]
}
```


## Correlation Endpoint

### Endpoint
`GET /api/correlation/`

### Descrição
Este endpoint retorna uma matriz de correlação entre as variáveis do conjunto de dados, medindo a força e a direção das relações lineares entre elas.

---

### Métodos Permitidos
- `GET`

---

### Resposta de Sucesso
#### Código de Status
`200 OK`

#### Cabeçalhos
- `Content-Type: application/json`
- `Vary: Accept`

#### Corpo da Resposta
A resposta contém uma matriz de correlação no formato JSON. Exemplo:
```json
{
    "status": "success",
    "matrix": {
        "PassengerId": {
            "PassengerId": 1.0,
            "Survived": -0.0050066607670665175,
            "Pclass": -0.03514399403038102,
            "Age": 0.036847197861327674,
            "SibSp": -0.0575268337844415,
            "Parch": -0.0016520124027188366,
            "Fare": 0.012658219287491099
        },
        "Survived": {
            "PassengerId": -0.0050066607670665175,
            "Survived": 1.0,
            "Pclass": -0.33848103596101514,
            "Age": -0.07722109457217756,
            "SibSp": -0.035322498885735576,
            "Parch": 0.08162940708348335,
            "Fare": 0.2573065223849626
        },
        ...
    }
}
```

