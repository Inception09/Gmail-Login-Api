# 📧 Gmail Login Api

<div align="center">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-blue" />
  <img alt="Status" src="https://img.shields.io/badge/Status-Active-brightgreen" />
  <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
</div>

Automates Google account sign-in and get session cookies.

## ✨ Features

- 🔐 Full Google sign-in flow via internal API
- 🎓 **Edu mail support** — automatically handles Google Workspace Terms of Service speedbump
- 💾 Saves session cookies
- ⚠️ Detects invalid email, wrong password, and edu mail automatically

## 📸 Preview

<div align="center">
  <img src="Screenshot%202026-05-08%20103548.png" width="500" alt="Screenshot 1" />
  <img src="Screenshot%202026-05-08%20103640.png" width="500" alt="Screenshot 2" />
  <img src="Screenshot%202026-05-08%20103731.png" width="500" alt="Screenshot 3" />
  <img src="edumail.jpg" width="500" alt="Edu Mail" />
</div>

## 🔄 Flow

```
accounts.google.com → identifier → password → (edu: accept ToS) → session saved
```

## 📤 Output

```
[step 2] account found: user@example.com
[step 3] edu mail detected: user@example.com
[step 4] login success: user@example.com
  cookies saved → user_at_example_com.json
```

## 📖 Full Source

This repository contains a demo version.  
For the full source contact me on Telegram:

**[@inception00007](https://t.me/inception00007)**

## ⚖️ Disclaimer

For educational purposes only. Use responsibly and only on accounts you own.
