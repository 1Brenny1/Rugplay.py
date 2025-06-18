from datetime import datetime
from requests import Response
class Coin():
    id:int
    name:str
    symbol:str
    icon:str
    currentPrice:float
    marketCap:float
    volume24h:float
    change24h:float
    poolCoinAmount:float
    poolBaseCurrencyAmount:float
    circulatingSupply:float
    initialSupply:float
    isListed:bool
    createdAt:datetime
    __creatorUsername__:str

    __bot__:object

    def __init__(self, bot, symbol:str):
        self.__bot__ = bot

        self.symbol = symbol.upper()
        self.__update__()
    
    def __update__(self):
        from ..Utils import Utils
        resp:Response = Utils.makeRequest(self, Utils.URLS.coin % (self.symbol, "1m"), get=True, use_cookies=False)
        self.fromJson(resp.json())
        
    
    from .User import User
    def getCreator(self) -> User:
        from ..Utils import Utils
        from .User import User
        resp:Response = Utils.makeRequest(self.__bot__, Utils.URLS.user % self.__creatorUsername__, get=True, use_cookies=False)
        return User(resp.json())
    
    def buy(self, amount:float):
        return self.__trade__("BUY", amount)
    
    def sell(self, amount:float):
        return self.__trade__("SELL", amount)

    def __trade__(self, action:str, amount:float):
        from ..Utils import Utils
        json = {
            "type": action,
            "amount": amount
        }
        resp = Utils.makeRequest(self.__bot__, Utils.URLS.trade % self.symbol, json=json)
        return resp.status_code == 200

    def fromJson(self, json:dict):
        
        coin:dict = json['coin']
        self.id = coin["id"]
        self.name = coin["name"]
        self.symbol = coin["symbol"]
        self.icon = coin["icon"]
        self.currentPrice = coin["currentPrice"]
        self.marketCap = coin["marketCap"]
        self.volume24h = coin["volume24h"]
        self.change24h = coin["change24h"]
        self.poolCoinAmount = coin["poolCoinAmount"]
        self.poolBaseCurrencyAmount = coin["poolBaseCurrencyAmount"]
        self.circulatingSupply = coin["circulatingSupply"]
        self.initialSupply = coin["initialSupply"]
        self.isListed = coin["isListed"]
        self.createdAt = datetime.fromisoformat(coin["createdAt"].replace("Z", "+00:00"))
        self.__creatorUsername__ = coin["creatorUsername"]
        
        return self