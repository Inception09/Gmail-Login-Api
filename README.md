# Gmail Login Api

Automates Google account sign-in and get session cookies.

## Features

- Full Google sign-in flow via internal API
- **Edu mail support** — automatically handles Google Workspace Terms of Service speedbump
- Saves session cookies
- Detects invalid email, wrong password, and edu mail automatically

## Preview

<div align="center">
  <style>
    @keyframes slideIn {
      from {
        opacity: 0;
        transform: translateY(20px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
    
    @keyframes fadeInScale {
      from {
        opacity: 0;
        transform: scale(0.9);
      }
      to {
        opacity: 1;
        transform: scale(1);
      }
    }
    
    @keyframes pulse {
      0%, 100% {
        opacity: 1;
      }
      50% {
        opacity: 0.7;
      }
    }
    
    .screenshot-container {
      animation: slideIn 0.6s ease-out;
      margin: 10px 0;
    }
    
    .screenshot-container:nth-child(1) {
      animation-delay: 0.1s;
    }
    
    .screenshot-container:nth-child(2) {
      animation-delay: 0.2s;
    }
    
    .screenshot-container:nth-child(3) {
      animation-delay: 0.3s;
    }
    
    .screenshot-container:nth-child(4) {
      animation-delay: 0.4s;
    }
    
    .screenshot-container:nth-child(5) {
      animation-delay: 0.5s;
    }
    
    .screenshot-container img {
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .screenshot-container img:hover {
      transform: scale(1.05);
      box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
    }
  </style>
  
  <div class="screenshot-container">
    <img src="Screenshot%202026-05-08%20103548.png" width="500" alt="Screenshot 1" />
  </div>
  <div class="screenshot-container">
    <img src="Screenshot%202026-05-08%20103640.png" width="500" alt="Screenshot 2" />
  </div>
  <div class="screenshot-container">
    <img src="Screenshot%202026-05-08%20103716.png" width="500" alt="Screenshot 3" />
  </div>
  <div class="screenshot-container">
    <img src="Screenshot%202026-05-08%20103731.png" width="500" alt="Screenshot 4" />
  </div>
  <div class="screenshot-container">
    <img src="edumail.jpg" width="500" alt="Edu Mail" />
  </div>
</div>

## Flow

```
accounts.google.com → identifier → password → (edu: accept ToS) → session saved
```

## Output

```
[step 2] account found: user@example.com
[step 3] edu mail detected: user@example.com
[step 4] login success: user@example.com
  cookies saved → user_at_example_com.json
```

## Full Source

This repository contains a demo version.  
For the full source contact me on Telegram:

**[@inception00007](https://t.me/inception00007)**

## Disclaimer

For educational purposes only. Use responsibly and only on accounts you own.
