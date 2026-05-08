<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Gmail%20Login%20API&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Automate%20Google%20Sign-in%20%7C%20Session%20Cookies&descAlignY=55&descSize=18" width="100%"/>

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

## 📸 Preview

<div align="center">
  <img src="edumail.jpg" width="500" alt="Edu Mail" />
  <img src="Screenshot%202026-05-08%20103548.png" width="500" alt="Screenshot 1" />
  <img src="Screenshot%202026-05-08%20103640.png" width="500" alt="Screenshot 2" />
  <img src="Screenshot%202026-05-08%20103731.png" width="500" alt="Screenshot 3" />
</div>

---

## 🔄 Flow

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
> Use responsibly and **only on accounts you own**.

---

<div align="center">

<!-- Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=Inception09.Gmail-Login-Api&style=for-the-badge)
![Stars](https://img.shields.io/github/stars/Inception09/Gmail-Login-Api?style=for-the-badge&logo=github&color=gold)

*Made with ❤️ by [@inception00007](https://t.me/inception00007)*

</div>
