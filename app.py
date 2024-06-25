from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def con_asc_home():
    return "Hello from WAS"
