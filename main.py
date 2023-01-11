import sys
sys.path.append("./packages")

#外部包
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

#自定义包
from build.dco import config 

conf = config.Settings()
print(conf.app_name)
index = Jinja2Templates("docs")

app = FastAPI()
app.mount("/docs",StaticFiles(directory='docs'),name="docs")

@app.get("/")
async def root(request: Request):
    return index.TemplateResponse("index.html",{"request": request})











if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info",reload=True)

