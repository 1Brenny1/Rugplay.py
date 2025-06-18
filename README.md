# SimUserAPI

> ⚠️ **Disclaimer:** This project is for educational and research purposes only. It is not affiliated with, endorsed by, or supported by any specific platform. Use at your own risk. Violating a platform’s Terms of Service may lead to account suspension or bans.

## 🎮 Overview

SimUserAPI is a lightweight Python interface that allows automated interaction with a **browser-based crypto trading simulation game**. It emulates user actions such as:

- Trading virtual tokens
- Participating in simulated liquidity pools
- Executing coinflips and slots using virtual currency
- Monitoring portfolio performance
- Performing automated decisions based on virtual market data

The platform has no real-world monetary system — all trading and gambling mechanics are **purely virtual and educational**.

---

## 🧠 Key Features

- 🪙 Coinflip & slot machine interface
- 💸 Trade virtual tokens programmatically
- 📊 Track simulated portfolio data
- 🛠️ Session-based user emulation
- 📦 Easy integration into bots, agents, or AI decision engines

---

## 🚀 Installation

```sh
python3 -m pip install simuserapi
```

## Examples:

### Project Setup Example
```py
import simuserapi

BOT = simuserapi.rp_bot("TOKEN", "CF_CLEARANCE")

print("Logged in as:", BOT.LOCAL_USER.username)
```
#### Note:
The ``TOKEN`` and ``CF_CLEARANCE`` can be found in your browser's cookies. In the applications tab of inspect element (Applications.Storage.Cookies), ``TOKEN`` is found under ``__Secure-better-auth.session_token`` and ``CF_CLEARANCE`` is found under ``cf_clearance``.

<hr>

### Basic Daily Claim Bot Example
```py
import simuserapi, time

BOT = simuserapi.rp_bot("TOKEN", "CF_CLEARANCE")

COIN = BOT.getCoin("SYMBOL")

while True:
    resp:simuserapi.ClaimResponse = BOT.claimDaily()

    if resp.success:
        COIN.buy(resp.rewardAmount)

    time.sleep(resp.timeRemaining/1000)
```