from fastapi import Query

def pagination(
        page:int=Query(1,ge=1),
        size:int=Query(2,ge=1,le=20)
):
    skip = (page-1)*size
    return {"page":page,"size":size,"skip":skip}
