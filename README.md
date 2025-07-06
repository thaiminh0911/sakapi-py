# sakapi - /Authkit API for Python
A module for using **/Authkit API** with Python.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **sakapi**.

```bash
pip install sakapi
```

## Usage
```python
import sakapi

# Telegram OTP verification
sakapi.tg.otp("authkey", "chatid")

# Email OTP verification
sakapi.email.otp("authkey", "email")

# Check if the AVC Authkey exists
sakapi.authkeyExists("authkey")

# Get App's data from AVC Authkey
sakapi.getData("authkey")
```

## [MIT License](https://github.com/thaiminh0911/sakapi-py/tree/main/LICENSE)
<img src="https://cdn.jsdelivr.net/gh/thaiminh0911/sak-data@latest/image/sak-mdfooter.svg" alt="Alt text" style="max-width: 100%; height: auto;" />