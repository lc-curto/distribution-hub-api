# Visão da arquitetura

## Estilo

Monólito modular com frontend React e API FastAPI.

```text
React + TypeScript
        │ HTTP/JSON
        ▼
FastAPI + Python
        │
        ▼
PostgreSQL
```

O desenvolvimento é por fatias verticais: especificação → banco → API → interface → testes.
