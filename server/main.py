from typing import Any, Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

try:
    from .dsl_interpreter import AlgorithmSessionManager
except ImportError:
    from dsl_interpreter import AlgorithmSessionManager  # type: ignore


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
    """
    Return the main menu so the client can display it immediately.
    """
    return AlgorithmSessionManager._menu_payload()



