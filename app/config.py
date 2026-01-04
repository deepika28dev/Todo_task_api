import os

"""
Flask configuration file.

This file contains configuration classes for different environments.
For now, we define only DevelopmentConfig for local development.
"""

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
  
    SQLALCHEMY_TRACK_MODIFICATIONS = False