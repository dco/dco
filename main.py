import sys
sys.path.append("./packages")

#外部包
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from enum import Enum


#自定义包
from build.dco import config 

conf = config.Settings()
print(conf.app_name)
index = Jinja2Templates("docs")

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

app.mount("/docs",StaticFiles(directory='docs'),name="docs")

# 路径操作装饰器，就是路由
@app.get("/")
# 路径操作函数
async def root(request: Request):
    return index.TemplateResponse("index.html",{"request": request})

# 使用路径参数
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# 预设值
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}







if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info",reload=True)

