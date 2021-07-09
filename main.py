#!venv/bin/python3

import sys
import os

from dotenv import load_dotenv
from application import Application

sys.path.append(os.getcwd())
load_dotenv()

if __name__ == "__main__":
    Application()