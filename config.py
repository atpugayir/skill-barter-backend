import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    DEBUG = True
    PORT = int(os.getenv("PORT", 5000))
