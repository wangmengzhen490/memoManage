from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import MemoCreate,MemoUpdate,MemoRead
from .service import Service
from .dependencies import pagination


router = APIRouter(prefix="/router")

@router.get("/")
def list_memos(
    db:Session = Depends(get_db),
    pages = Depends(pagination)
):
    return Service.get_memos(db,pages["page"],pages["size"])

@router.get("/{id}",response_model=MemoRead)
def one_memo(id:int,db:Session = Depends(get_db)):
    memo = Service.get_one_memo(db,id)
    if not memo:
        raise HTTPException(status_code=404,detail="找不到该条备忘录")
    return memo

@router.post("/",status_code=201,response_model=MemoRead)
def add_memo(obj:MemoCreate,db:Session = Depends(get_db)):
    return Service.create_memo(db,obj)

@router.put("/{id}",response_model=MemoRead)
def edit_memo(id:int,obj:MemoUpdate,db:Session = Depends(get_db)):
    memo = Service.update_memo(db,id,obj)
    if not memo:
        raise HTTPException(status_code=404,detail="找不到该条备忘录")
    return memo

@router.delete("/{id}")
def del_memo(id:int,db:Session = Depends(get_db)):
    ok = Service.delete_memo(db,id)
    if not ok:
        raise HTTPException(status_code=404,detail="找不到该条备忘录")
    return {"msg":"删除成功"}