from . import email
from . import tg
import requests

def authkeyExists(authkey):
    if requests.get("https://avc.vercel.app/api/getData", params={"authkey": authkey}).status_code == 200:
        return True
    else:
        return requests.get("https://avc.vercel.app/api/getData", params={"authkey": authkey}).status_code

def getData(authkey):
    return requests.get("https://avc.vercel.app/api/getData", params={"authkey": authkey}).json()