def scriptEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "script_name": item["script_name"],
        "script_description": item["script_description"],
        "ltp": item["ltp"],
        "is_enable": item["is_enable"]
    }

def scriptsEntity(entity) -> list:
    return [scriptEntity(item) for item in entity]
