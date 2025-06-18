from .User import User
from requests import Response

class LocalUser(User):
    def __init__(self, bot):
        from ..Utils import Utils
        resp = Utils.makeRequest(bot, Utils.URLS.localUserData, get=True)

        data = resp.json()

        values = data["nodes"][0]["data"][1]
        for item in values:
            val = data["nodes"][0]["data"][values[item]]
            if item == "id":
                self.id:int = val
            elif item == "name":
                self.displayName:str = val
            elif item == "username":
                self.username:str = val
            elif item == "email":
                self.email:str = val
            elif item == "isAdmin":
                self.isAdmin:bool = val
            elif item == "image":
                self.image:str = val
            elif item == "isBanned":
                self.isBanned:bool = val
            elif item == "banReason":
                self.banReason:str|None = val
            elif item == "avatarUrl":
                self.avatarUrl:str = val
            elif item == "baseCurrencyBalance":
                self.baseCurrencyBalance:float = val
            elif item == "bio":
                self.bio:str = val
            elif item == "volumeMaster":
                self.volumeMaster:float = val
            elif item == "volumeMuted":
                self.volumeMuted:bool = val

        resp:Response = Utils.makeRequest(bot, Utils.URLS.user % self.username, get=True, use_cookies=False)
        super().__init__(resp.json())

    def __str__(self):
        return f"<localUser: {self.displayName} ({self.username})>"
