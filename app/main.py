from fastapi import FastAPI

from app.modules.customers.router import router as customers_router

app = FastAPI(title="Distribution Hub API", version="0.1.0")

app.include_router(customers_router)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}
