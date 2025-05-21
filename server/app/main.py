from app.server import app
import uvicorn
from app.routers import health

app.include_router(
    health.router,
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not Found"}},
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)