from fastapi import FastAPI
import os

app=FastAPI()

@app.get('/')
async def con_asc_home():
    return f"Hello from {os.environ['HOSTNAME']}"
