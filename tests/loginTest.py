import simuserapi, time

BOT = simuserapi.rp_bot("TOKEN", "CF_CLEARANCE")

COIN = BOT.getCoin("SYMBOL")

while True:
    resp:simuserapi.ClaimResponse = BOT.claimDaily()

    if resp.success:
        COIN.buy(resp.rewardAmount)

    time.sleep(resp.timeRemaining/1000)
        