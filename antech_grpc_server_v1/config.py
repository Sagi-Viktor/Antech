# Configuration for ChirpStack gRPC server and authentication

CHIRPSTACK_GRPC_SERVER = "localhost:8080"  # Address of the ChirpStack gRPC server
CHIRPSTACK_API_TOKEN = "your_api_token_here"  # Replace with your ChirpStack API token

MOCK_DATABASE = {
    "devices": [
        {"device_id": "device_1", "dev_eui": "0101010101010101"},
        {"device_id": "device_2", "dev_eui": "0202020202020202"}
    ]
}
