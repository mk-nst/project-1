from fastapi import FastAPI, HTTPException
import os
from utils.task_handlers import handle_task
from utils.file_utils import read_file

app = FastAPI()

@app.post("/run")
async def run_task(task: str):
    try:
        result = handle_task(task)
        return {"status": "success", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_file_endpoint(path: str):
    try:
        content = read_file(path)
        return {"content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)