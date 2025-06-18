import requests

class Utils:
    from .rp_bot import RugplayBot

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "Referer": "https://outpoot.com/star",
        "Accept": "*/*"
    }
    
    class URLS:
        daily = "https://rugplay.com/api/rewards/claim"
        total = "https://rugplay.com/api/portfolio/total"
        user = "https://rugplay.com/api/user/%s"
        localUserData = "https://rugplay.com/portfolio/__data.json"
        trade = "https://rugplay.com/api/coin/%s/trade"
        coin = "https://rugplay.com/api/coin/%s?timeframe=%s"
        comment = "https://rugplay.com/api/coin/%s/comments"
        coinFlip = "https://rugplay.com/api/gambling/coinflip"
        slots = "https://rugplay.com/api/gambling/slots"
    
    def makeRequest(bot:RugplayBot, url:str, json=None, get:bool=False, use_cookies:bool=True) -> requests.Response:
        
    
        cookies = {}
        if use_cookies:
            cookies["__Secure-better-auth.session_token"] = bot.TOKEN
            cookies["cf_clearance"] = bot.CLEARANCE
    
        if not get:
            resp = requests.post(url, json=json, cookies=cookies, headers=Utils.HEADERS)
        else:
            resp = requests.get(url, json=json, cookies=cookies, headers=Utils.HEADERS)
    
        del cookies
    
        return resp