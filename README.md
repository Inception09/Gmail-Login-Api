# 📧 Gmail Login Api

<div align="center">

![Gmail Login API Banner](banner.png)

<!-- Typing Animation -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=EA4335&center=true&vCenter=true&width=600&lines=Full+Google+Sign-in+Flow+%F0%9F%94%90;Edu+Mail+Support+%F0%9F%8E%93;Auto+Session+Cookie+Saver+%F0%9F%8D%AA;Smart+Error+Detection+%E2%9C%85" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Badges Row 1 -->
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge&logo=statuspage&logoColor=white)
![Maintained](https://img.shields.io/badge/Maintained-Yes-green?style=for-the-badge&logo=github&logoColor=white)

<!-- Badges Row 2 -->
![Platform](https://img.shields.io/badge/Platform-Google-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Auth](https://img.shields.io/badge/Auth-Session%20Cookies-red?style=for-the-badge&logo=firefoxbrowser&logoColor=white)
![Telegram](https://img.shields.io/badge/Contact-Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![EDU](https://img.shields.io/badge/Edu%20Mail-Supported-blueviolet?style=for-the-badge&logo=googleclassroom&logoColor=white)

<!-- New API Badges -->
![API](https://img.shields.io/badge/REST-API-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Base URL](https://img.shields.io/badge/Base%20URL-gmail--api.catmmo.com-blue?style=for-the-badge&logo=googlechrome&logoColor=white)

</div>

---

## ✨ Features

<div align="center">

| Feature | Description |
|:-------:|:-----------|
| 🔐 | **Full Google Sign-in Flow** via internal API |
| 🎓 | **Edu Mail Support** — handles Google Workspace Terms of Service speedbump |
| 🍪 | **Saves Session Cookies** automatically after login |
| 🚨 | **Smart Error Detection** — invalid email, wrong password, edu mail |

</div>

---

## 🌐 Public API

> **Base URL:** `http://gmail-api.catmmo.com`

> 🚧 **This is a preview API** — shared freely for testing purposes.  
> ❌ **Do not abuse it.** Excessive requests, automation at scale, or malicious use will get you blocked.  
> If you need the full version or higher limits, contact me on [Telegram](https://t.me/inception00007).

### `POST /login`

Authenticates a Workspace/Edu email and returns session cookies.

#### 📥 Request

```http
POST /login HTTP/1.1
Host: gmail-api.catmmo.com
Content-Type: application/json
```

```json
{
  "email": "your_email@edu_or_workspace.com",
  "password": "your_password"
}
```

> ⚠️ **Note:** `@gmail.com` accounts are **not supported**. Only **Edu / Workspace** emails work.Contact me if you want gmail.com login.

---

#### 📤 Responses

**✅ Success — `200 OK`**

```json
{
  "status": "success",
  "cookies": {
    "SID": "...",
    "HSID": "...",
    "__Secure-1PSID": "...",
    "__Secure-3PSID": "...",
    "...": "other cookies"
  }
}
```

> Status can also be `"edu_success"` for Google Workspace/Edu accounts.

**❌ Error — `400 Bad Request`** *(gmail.com used)*

```json
{
  "error": "gmail.com not supported in this api contact me if you need. Use edu mail/workspace mail"
}
```

**❌ Error — `401 Unauthorized`** *(wrong credentials or blocked)*

```json
{
  "status": "wrong_password"
}
```

| Status Value | Meaning |
|:---:|:---|
| `wrong_password` | Incorrect password |
| `invalid_email` | Email does not exist |
| `botguard` | Google bot protection triggered |
| `error` | Unknown / unexpected error |

---

## 🐍 Client Script

Use the included `gmail-login-api.py` to call the API directly from Python.

```python
import requests

API_URL = "https://gmail-api.catmmo.com/login"

def login_and_get_cookies(email, password):
    payload = {"email": email, "password": password}
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") in ("success", "edu_success"):
                return data.get("cookies")
        else:
            print(f"API Error ({response.status_code}): {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
    return None

if __name__ == "__main__":
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    cookies = login_and_get_cookies(email, password)
    if cookies:
        print("Login successful! Cookies:", cookies)
    else:
        print("Login failed.")
```

**Install dependency & run:**

```bash
pip install requests
python gmail-login-api.py
```

---

## 📸 Preview of Source

<div align="center">
  <img src="edumail.jpg" width="500" alt="Edu Mail" />
  <img src="Screenshot%202026-05-08%20103548.png" width="500" alt="Screenshot 1" />
  <img src="Screenshot%202026-05-08%20103640.png" width="500" alt="Screenshot 2" />
  <img src="Screenshot%202026-05-08%20103731.png" width="500" alt="Screenshot 3" />
</div>

---

## 🔄 Flow of Source

```
accounts.google.com → identifier → password → (edu: accept ToS) → session saved
```

<div align="center">

```mermaid
graph LR
    A[🌐 accounts.google.com] --> B[📧 Identifier]
    B --> C[🔑 Password]
    C --> D{Edu Mail?}
    D -- Yes --> E[📜 Accept ToS]
    D -- No --> F[✅ Session Saved]
    E --> F
    style A fill:#4285F4,color:#fff
    style F fill:#34A853,color:#fff
    style D fill:#FBBC05,color:#000
```

</div>

---

## 📤 Output

```bash
[step 2] account found: user@example.com
[step 3] edu mail detected: user@example.com
[step 4] login success: user@example.com
  cookies saved → user_at_example_com.json
```

---

## 📖 Full Source

> This repository contains a **demo version**.  
> For the full source, contact me on Telegram:

<div align="center">

[![Telegram](https://img.shields.io/badge/Telegram-%40inception00007-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/inception00007)

</div>

---

## ⚖️ Disclaimer

> ⚠️ **For educational purposes only.**  
> Use responsibly and **only on accounts you own**. Do not abuse the public API.

---

<div align="center">

<!-- Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

*Made with ❤️ by [@inception00007](https://t.me/inception00007)*

</div>
