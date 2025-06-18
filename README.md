# RugplayBot

## Examples:

### Project Setup Example
```py
import rugplay

BOT = rugplay.RugplayBot("TOKEN", "CF_CLEARANCE")

print("Logged in as:", BOT.LOCAL_USER.username)
```
#### Note:
The ``TOKEN`` and ``CF_CLEARANCE`` can be found in your browser's cookies for Rugplay.com. In the applications tab of inspect element (Applications.Storage.Cookies.Rugplay.com), ``TOKEN`` is found under ``__Secure-better-auth.session_token`` and ``CF_CLEARANCE`` is found under ``cf_clearance``.

<hr>

### Basic Daily Claim Bot Example
```py
import rugplay, time

BOT = rugplay.RugplayBot("TOKEN", "CF_CLEARANCE")

COIN = BOT.getCoin("SYMBOL")

while True:
    resp:rugplay.ClaimResponse = BOT.claimDaily()

    if resp.success:
        COIN.buy(resp.rewardAmount)

    time.sleep(resp.timeRemaining/1000)
```