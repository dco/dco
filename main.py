
import sys
sys.path.append("./packages")

import uvicorn
from fastapi import FastAPI
import config 
import index
from fastapi.responses import HTMLResponse


conf = config.Settings()


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return index.index_html












if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info",reload=True)

