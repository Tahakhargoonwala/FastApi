# def userEntity(item) -> dict:
#     return {
#         "id": str(item["_id"]),
#         "name": item["name"],
#         "email": item["email"],
#         "password": item["password"]
#     }


# def usersEntity(entity) -> list:
#     return [userEntity(item) for item in entity]
 

def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "username": item["username"],
        "about": item["about"],
        "is_enable": item["is_enable"]
    }

