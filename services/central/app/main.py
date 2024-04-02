from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse
from .config import attachment_directory
from .logger import log, logMemoryHit
from os.path import exists
from time import sleep

app = FastAPI(use_cache = False)

@app.get("/ping")
def ping():
    return "pong!"

simulateExpensiveLookup = lambda: sleep(2)

@app.get("/attachment/{attachment_name}",
         responses={
             200:{"content": {"image/png": {}}},
             404:{"description": "Resource not found",
                  "content": {"application/json": 
                              {"example": {
                                  "detail": "Resource not found"}}}}}
        )
def send_attachment(attachment_name: str):
        attachment_path = f"app/{attachment_directory}{attachment_name}"
        if not exists(attachment_path):
            log(f"Requested file {attachment_path} not found on server!")
            raise HTTPException(status_code=404)
        with open(attachment_path, "rb") as attachment_file:
            attachment = attachment_file.read()
        logMemoryHit()
        simulateExpensiveLookup()
        return Response(attachment, media_type="image/jpeg", headers={"Cache-Control": "no-cache"})