
import os
import socket

from fastapi import FastAPI

app = FastAPI(
    title="EKS Delivery Platform",
    description="A Python application deployed on Amazon EKS",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "application": "EKS Delivery Platform",
        "version": os.getenv("APP_VERSION", "v1"),
        "message": os.getenv(
            "APP_MESSAGE",
            "Welcome to my EKS project!"
        ),
        "hostname": socket.gethostname()
    }


@app.get("/healthz")
def health():
    return {
        "status": "healthy"
    }


@app.get("/readyz")
def readiness():
    return {
        "status": "ready"
    }
