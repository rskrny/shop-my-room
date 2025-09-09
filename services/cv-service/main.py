from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ProcessRequest(BaseModel):
    image_urls: List[str]
    known_scale_cm: Optional[float] = None


@app.post("/cv/rooms/{room_id}/process")
async def process_room(room_id: str, payload: ProcessRequest):
    return {
        "layout_json": {"slots": [], "dimensions": [400, 300]},
        "topdown_png_url": "https://dummy.com/layout.png",
    }
