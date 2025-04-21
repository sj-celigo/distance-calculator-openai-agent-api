from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from distance_agent import distance_agent, Runner

app = FastAPI(title="Distance Calculator API")

class DistanceRequest(BaseModel):
    query: str

@app.post("/calculate-distance")
async def calculate_distance(request: DistanceRequest):
    try:
        result = await Runner.run(distance_agent, request.query)
        return {"response": result.final_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 