from datetime import datetime, timedelta
class ClaimResponse:
    canClaim:bool
    timeRemaining:int
    success:bool
    rewardAmount:float = -1
    baseReward:float = -1
    newBalance:float = -1
    totalRewardsClaimed:float = -1
    loginStreak:int = -1
    nextClaimTime:datetime
    def __init__(self):
        pass

    def fromJson(self, json:dict):
        if not json.get("canClaim", True):
            self.canClaim = json["canClaim"]
            self.success = False
            self.timeRemaining = json["timeRemaining"]
            self.nextClaimTime = datetime.now() + timedelta(seconds=json["timeRemaining"]/1000)
            return self

        self.success = json["success"]
        self.rewardAmount = json["rewardAmount"]
        self.baseReward = json["baseReward"]
        self.newBalance = json["newBalance"]
        self.totalRewardsClaimed = json["totalRewardsClaimed"]
        self.loginStreak = json["loginStreak"]
        self.nextClaimTime = datetime.fromisoformat(json["nextClaimTime"].replace("Z", "+00:00"))
        return self