from fastapi import APIRouter, HTTPException, Body
from services.cs_service import send_downlink_to_device
from database.database import get_device_by_id

router = APIRouter()


@router.post("/downlink")
async def send_downlink(device_id: str, payload: str):
    """
    Endpoint to send a downlink message.

    Args:
        device_id (str): ID of the target device.
        payload (str): Hexadecimal string representing the payload.

    Returns:
        dict: Response indicating success or failure.
    """
    # Fetch device details from mock database
    device = get_device_by_id(device_id)

    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    try:
        # Convert hexadecimal payload to bytes
        payload_bytes = bytes.fromhex(payload)

        # Call service layer to send downlink message via ChirpStack gRPC API
        result = await send_downlink_to_device(device["dev_eui"], payload_bytes)

        if result["status"] == "error":
            raise HTTPException(status_code=500, detail=result["message"])

        return result

    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid hexadecimal payload")
