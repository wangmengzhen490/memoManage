from sqlalchemy.orm import Session
from .models import Memo
from .schemas import MemoCreate,MemoUpdate,MemoRead

class Service:
    # 获取备忘录列表
    @staticmethod
    def get_memos(db:Session,page:int=1,size:int=2):
        q = db.query(Memo)
        skip = (page-1)*size
        total = q.count()
        data = q.offset(skip).limit(size).all()
        return {"data":data,"total":total}

    # 获取单条备忘录
    @staticmethod
    def get_one_memo(db:Session,id:int):
        memo = db.query(Memo).filter(Memo.id == id).first()
        if not memo:
            return None
        return memo

    # 新增
    @staticmethod
    def create_memo(db:Session,obj:MemoCreate):
        memo = Memo(**obj.model_dump())
        db.add(memo)
        db.commit()
        db.refresh(memo)
        return memo

    # 修改
    @staticmethod
    def update_memo(db:Session,id:int,obj:MemoUpdate):
        memo = db.query(Memo).filter(Memo.id == id).first()
        if not memo:
            return None
        for k,v in obj.model_dump(exclude_none=True).items():
            setattr(memo,k,v)
        db.commit()
        db.refresh(memo)
        return memo

    # 删除
    @staticmethod
    def delete_memo(db:Session,id:int):
        memo = db.query(Memo).filter(Memo.id == id).first()
        if not memo:
            return None
        db.delete(memo)
        db.commit()
        return True
    
