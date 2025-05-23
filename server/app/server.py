from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {
        "name": "health",
        "description": "Checks service health"
    },
    {
        "name": "entrances",
        "description": "Handles entrance operations"
    },
    {
        "name": "items",
        "description": "Handles item operations"
    },
    {
        "name": "locations",
        "description": "Handles location operations"
    },
    {
        "name": "regions",
        "description": "Handles region operations"
    }
]

def __create_fastapi_server() -> FastAPI:
    server = FastAPI(
        title="Test",
        version="1.0.0",
        openapi_tags=tags_metadata
    )
    return server

app = __create_fastapi_server()