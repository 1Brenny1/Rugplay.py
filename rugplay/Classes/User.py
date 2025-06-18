from datetime import datetime
class User:
    def __init__(self, data:dict):
        profile = data["profile"]

        self.id:int = profile["id"]
        self.displayName:str = profile["name"]
        self.username:str = profile["username"]
        self.bio:str = profile["bio"]
        self.image:str = profile["image"]
        self.createdAt:str = datetime.fromisoformat(profile["createdAt"].replace("Z", "+00:00"))
        self.baseCurrencyBalance:float = profile["baseCurrencyBalance"]
        self.isAdmin:bool = profile["isAdmin"]
        self.loginStreak:int = profile["loginStreak"]
        self.prestigeLevel:int = profile["prestigeLevel"]
        self.totalPortfolioValue:float = profile["totalPortfolioValue"]

        stats = data["stats"]

        self.baseCurrencyBalance:float = stats["baseCurrencyBalance"]
        self.holdingsValue:float = stats["holdingsValue"]

    def __str__(self):
        return f"<user: {self.displayName} ({self.username})>"
