class SlotsResponse:
    won:bool
    symbols:list[str,str,str]
    newBalance:float
    payout:float
    amountWagered:float
    def __init__(self):
        pass

    def fromJson(self, json:dict):
        self.won = json["won"]
        self.symbols = json['symbols']
        self.newBalance = json['newBalance']
        self.payout = json["payout"]
        self.amountWagered = json['amountWagered']

        return self