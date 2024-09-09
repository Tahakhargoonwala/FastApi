from pydantic import BaseModel

class Script(BaseModel):
    script_name: str
    script_description: str
    ltp: float  # Last Traded Price
    is_enable: bool = True
