#!/usr/bin/env python
"""
Server startup script that reads configuration from .env file
Usage: python run_server.py (make sure conda environment is activated)
"""
import os
from dotenv import load_dotenv
import uvicorn

# Load environment variables
load_dotenv()

# Get configuration from .env or use defaults
PORT = int(os.getenv('PORT', '8069'))
HOST = os.getenv('HOST', '0.0.0.0')

if __name__ == '__main__':
    print(f"Starting server on {HOST}:{PORT}")
    print(f"Make sure you're in the server directory and conda environment is activated")
    uvicorn.run(
        'main:app',
        host=HOST,
        port=PORT,
        reload=True
    )
