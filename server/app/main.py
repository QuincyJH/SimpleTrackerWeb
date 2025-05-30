from app.server import app
import uvicorn
from app.routers import health, entrances, items, locations, regions, runs
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

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
app.include_router(
    regions.router,
    prefix="/regions",
    tags=["regions"],
    responses={404: {"description": "Not Found"}},
)
app.include_router(
    runs.router,
    prefix="/runs",
    tags=["runs"],
    responses={404: {"description": "Not Found"}},
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

app.include_router(
    runs.router,
    prefix="/runs",
    tags=["runs"],
    responses={404: {"description": "Not Found"}},
)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)