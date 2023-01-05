from fastapi import APIRouter, Depends, HTTPException

from dependencies import get_token_header

#你可以将 APIRouter 视为一个「迷你 FastAPI」类
#定义roter通用的一些信息，后面就不用全都写了
router = APIRouter(
    prefix="/items", #定义api前缀
    tags=["items"], 
    dependencies=[Depends(get_token_header)],  #每个api都会执行依赖项，认证很有用
    responses={404: {"description": "Not found"}}, # 定义自定义通用响应
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}


@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
     #每个请求也可以再次定义，但会有两个响应
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}
