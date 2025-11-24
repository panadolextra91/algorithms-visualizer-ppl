from typing import Any, Dict, List, Optional
import os
import re
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from dsl_interpreter import AlgorithmSessionManager

# Load environment variables from .env file
load_dotenv()


app = FastAPI(title="Algorithms Visualizer Server")


class CommandRequest(BaseModel):
    sessionId: str
    command: str


session_manager = AlgorithmSessionManager()


@app.post("/command")
def handle_command(req: CommandRequest) -> Dict[str, Any]:
    try:
        result = session_manager.handle_command(req.sessionId, req.command)
        return result
    except ValueError as e:
        return {"status": "error", "message": str(e)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def root() -> Dict[str, str]:
    return {"status": "ok", "message": "Algorithms Visualizer Server is running"}


@app.get("/greeting")
def greeting() -> Dict[str, Any]:
    return {
        "status": "success",
        "type": "greeting",
        "message": (
            "Hello, what are we going to do today, developer?\n"
            "1. Sorting algorithms.\n"
            "2. Pathfinding algorithms.\n"
            "3. Data structures"
        ),
    }



