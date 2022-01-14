# © its-leo-bitch
import os
import re
from pathlib import Path

class Config:
  API_ID = 16349774
  API_HASH = "fa09cf6cdfdc16a315cafca62909857e"
  TOKEN = os.environ.get("TOKEN", "")
  BOTUSERNAME = os.environ.get("BOTUSERNAME", "")
