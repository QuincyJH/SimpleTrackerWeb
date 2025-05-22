from app.server import app
import uvicorn
from app.routers import health, entrances, items, locations

app.include_router(
    health.router,
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not Found"}},
)

app.include_router(
    entrances.router,
    prefix="/entrances",
    tags=["entrances"],
    responses={404: {"description": "Not Found"}},
)

app.include_router(
    items.router,
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not Found"}},
)

app.include_router(
    locations.router,
    prefix="/locations",
    tags=["locations"],
    responses={404: {"description": "Not Found"}},
)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)