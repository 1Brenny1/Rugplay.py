class CoinFlipResponse:
    won:bool
    result:str
    newBalance:float
    payout:float
    amountWagered:float
    def __init__(self):
        pass
    def fromJson(self, json:dict):
        self.won = json["won"]
        self.result = json["result"]
        self.newBalance = json["newBalance"]
        self.payout = json["payout"]
        self.amountWagered = json["amountWagered"]
        return self