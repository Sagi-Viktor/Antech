from fastapi import FastAPI
from controllers.cs_controller import router as cs_router

import chirpstack_api
print(dir(chirpstack_api))


app = FastAPI()

# Include the ChirpStack router
app.include_router(cs_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the ChirpStack Demo API"}
