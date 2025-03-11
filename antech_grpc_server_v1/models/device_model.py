from pydantic import BaseModel

class Device(BaseModel):
    device_id: str
    dev_eui: str
