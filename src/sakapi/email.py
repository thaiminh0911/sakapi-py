import requests

def otp(authkey, email):
    return requests.post("https://avc.vercel.app/api/email/otpVerification", params={"authkey": authkey, "email": email}).json()