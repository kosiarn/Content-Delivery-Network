from fastapi import FastAPI, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import config
import cache
from central_server_connection import fetchFromCentralServer


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = config.frontend_addresses,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/ping")
def ping():
    return "Pong!"

@app.get("/attachment/{attachment_name}",
         responses={
             200:{"content": {"image/png": {}}},
             404:{"description": "Resource not found",
                  "content": {"application/json": 
                              {"example": {
                                  "detail": "Resource not found"}}}}}
        )
def get_attachment(attachment_name: str):
    """
    Fetches attachment from CDN resources. 
    If not present on edge server's cache, it gets fetched from central server.
    """
    if cache.isInCache(attachment_name):
        attachment = cache.getFromCache(attachment_name)
    try:
        attachment = fetchFromCentralServer(attachment_name)
        cache.cacheAttachemnt(attachment, attachment_name)
    except FileNotFoundError:
        raise HTTPException(404, "File not found!")
    return Response(attachment, media_type="image/jpeg", headers={"Cache-Control": "no-cache"})