from requests import Response
from .Classes.LocalUser import LocalUser
from .Classes.User import User
from .Classes.Coin import Coin
from .Responses.ClaimResponse import ClaimResponse
from .Responses.CoinFlipResponse import CoinFlipResponse
from .Responses.SlotsResponse import SlotsResponse

class RugplayBot():
    TOKEN:str = None
    CLEARANCE:str = None
    LOCAL_USER:LocalUser = None

    def __init__(self, token:str, clearance:str):
        if token == None or clearance == None:
            raise Exception("Missing Token and/or Clearance")

        self.TOKEN = token
        self.CLEARANCE = clearance

        try:
            self.LOCAL_USER = LocalUser(self)
        except:
            print("Invalid Token or Clearance")
    
    def claimDaily(self) -> ClaimResponse:
        from .Utils import Utils
        resp:Response = Utils.makeRequest(self, Utils.URLS.daily)
        return ClaimResponse().fromJson(resp.json())

    def getUser(self, username:str) -> User:
        from .Utils import Utils
        resp:Response = Utils.makeRequest(self, Utils.URLS.user % username, get=True, use_cookies=False)
        return User(resp.json())

    def getCoin(self, symbol:str) -> Coin:
        return Coin(self, symbol)
    
    def coinFlip(self, side:str, amount:float):
        from .Utils import Utils
        side = side.lower()

        json = {
            "side": side,
            "amount": amount
        }

        resp:Response = Utils.makeRequest(self, Utils.URLS.coinFlip, json=json)
        return CoinFlipResponse().fromJson(resp.json())
    
    def playSlots(self, amount:float):
        from .Utils import Utils

        json = {
            "amount": amount
        }

        resp:Response = Utils.makeRequest(self, Utils.URLS.slots, json=json)
        return SlotsResponse().fromJson(resp.json())