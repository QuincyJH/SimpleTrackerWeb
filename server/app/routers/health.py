from datetime import datetime
from fastapi import Response, APIRouter

router = APIRouter()

@router.get("")
async def health_check():
    print("Health Request")
    current_time = datetime.now()
    return Response(content=f"Services up and running\n{current_time}", media_type="text/plain")