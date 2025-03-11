import grpc
from chirpstack_api import api
from config import CHIRPSTACK_GRPC_SERVER, CHIRPSTACK_API_TOKEN


async def send_downlink_to_device(dev_eui: str, payload: bytes, f_port: int = 10):
    """
    Sends a downlink message to a LoRaWAN device using the ChirpStack gRPC API.

    Args:
        dev_eui (str): Device EUI of the target device.
        payload (bytes): Payload as a byte array.
        f_port (int): LoRaWAN port number.

    Returns:
        dict: Response from the ChirpStack API.
    """
    try:
        # Connect to the gRPC server without TLS
        channel = grpc.insecure_channel(CHIRPSTACK_GRPC_SERVER)

        # Create a client for the DeviceServiceStub
        client = api.DeviceServiceStub(channel)

        # Define metadata with authorization token
        metadata = [("authorization", f"Bearer {CHIRPSTACK_API_TOKEN}")]

        # Construct request for enqueueing downlink message
        req = api.EnqueueDeviceQueueItemRequest()
        req.queue_item.dev_eui = dev_eui  # Target device's DevEUI
        req.queue_item.f_port = f_port  # LoRaWAN port number
        req.queue_item.confirmed = False  # Whether confirmation is required from the device
        req.queue_item.data = payload  # Payload as bytes

        # Perform the API call via gRPC and return response ID
        resp = client.Enqueue(req, metadata=metadata)

        return {"status": "success", "downlink_id": resp.id}

    except grpc.RpcError as e:
        return {"status": "error", "message": str(e)}
