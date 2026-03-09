# LogIQ — Sistema de Análise de Logs

API REST para análise e gerenciamento de logs de sistema, construída com foco em estruturas de dados e algoritmos aplicados.

## Decisões Técnicas

**HashMap** para busca de logs em O(1)
**Merge Sort** para ordenação por timestamp em O(n log n)
**FastAPI** pela performance e documentação automática
**SQLite** para persistência dos dados

## Como Rodar
```bash
git clone https://github.com/fesynn/logiq.git
cd logiq
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
python3 main.py
```

Acesse a documentação em: http://localhost:8000/docs

## Rotas

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | /logs/seed | Gera 10 logs aleatórios |
| GET | /logs | Lista todos os logs |
| GET | /logs/sorted | Logs ordenados por timestamp |
| GET | /logs/errors | Contagem por level e service |

## Tecnologias

- Python 3.12
- FastAPI
- SQLite
- Git