from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse
from config import attachment_directory
from logger import log
from os.path import exists

app = FastAPI()

@app.get("/ping")
def ping():
    return "pong!"

@app.get("/attachment/{attachment_name}",
         responses={
             200:{"content": {"image/png": {}}},
             404:{"description": "Resource not found",
                  "content": {"application/json": 
                              {"example": {
                                  "detail": "Resource not found"}}}}}
        )
def send_attachment(attachment_name: str):
        attachment_path = f"{attachment_directory}\\{attachment_name}"
        log(f"Sending file {attachment_path}...")
        if not exists(attachment_path):
            log(f"Requested file {attachment_path} not found on server!")
            raise HTTPException(status_code=404)
        attachment = FileResponse(attachment_path)
        return attachment