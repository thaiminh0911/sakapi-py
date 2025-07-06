import requests

def otp(authkey, chatid):
    return requests.post("https://avc.vercel.app/api/telegram/otpVerification", params={"authkey": authkey, "chatid": chatid}).json()