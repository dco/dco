# APIRouter 跟fastapi一样使用
from fastapi import APIRouter

# 实例化，名字可以随便起，当然roter就挺好
router = APIRouter()

# 高级用法看items
@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
