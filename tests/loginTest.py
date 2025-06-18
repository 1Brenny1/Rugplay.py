import rugplay, time

BOT = rugplay.RugplayBot("TOKEN", "CF_CLEARANCE")

COIN = BOT.getCoin("SYMBOL")

while True:
    resp:rugplay.ClaimResponse = BOT.claimDaily()

    if resp.success:
        COIN.buy(resp.rewardAmount)

    time.sleep(resp.timeRemaining/1000)
        