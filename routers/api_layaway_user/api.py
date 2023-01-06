from fastapi import APIRouter, HTTPException

from config.db import client as db

router = APIRouter()


async def list_layaway(data: dict) -> dict:
    return {
        "id": str(data.get("_id")),
        "idComic": data.get("id_comic"),
        "title": data.get("title"),
        "image": data.get("image"),
        "userId": data.get("user_id"),
        "onSaleDate": data.get("on_sale_date"),
    }


async def query_data_layaway_comics(my_db, user_id: str, title: str):
    my_collection_layaway_comics = my_db["layaway_comics"]
    myquery = {"user_id": user_id}

    if title:
        myquery["title"] = {"$regex": f"{title}"}

    mydoc = my_collection_layaway_comics.find(myquery).sort("title", 1)
    return [await list_layaway(row) for row in mydoc]


@router.get("/getLayawayList/")
async def layaway_list(user_id: str, title: str = None):
    my_db = db["comics"]
    my_collection_user_comics = my_db["user_comics"]
    user_db = my_collection_user_comics.find_one({"user_id": user_id})

    if not user_db:
        raise HTTPException(detail="Usuario no encontrado", status_code=400)
    elif not user_db.get("is_active"):
        raise HTTPException(detail="Usuario no activo", status_code=400)
    else:
        query = await query_data_layaway_comics(my_db, user_id, title)
        return {"status": query}
