from setuptools import setup, find_packages

setup(
    name="antech_grpc_server_v1",  # Replace with your project name
    version="0.1",
    packages=find_packages(),  # Automatically find all packages in the project
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    install_requires=[
        "fastapi",
        "uvicorn",
        "chirpstack-api",
        "grpcio"
    ],
)
