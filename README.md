# desafio-titanic

## Summary Endpoint

### Endpoint
`GET /api/summary/`

### Descrição
Este endpoint retorna um resumo estatístico de diferentes variáveis analisadas.

---

### Métodos Permitidos
- `GET`
- `HEAD`
- `OPTIONS`

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


## Survival Rate Endpoint

### Endpoint
`GET /api/survival_rate`

### Descrição
Este endpoint retorna a taxa de sobrevivência dos dados analisados.

---

### Métodos Permitidos
- `GET`
- `HEAD`
- `OPTIONS`

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
