from flask import jsonify

class StationItem:
    def __init__(self, sname, scity, savailableBikeNumber, sfreeSlotNumber):
        self.name = sname
        self.city = scity
        self.availableBikeNumber = savailableBikeNumber
        self.freeSlotNumber = sfreeSlotNumber

    def toJson(self):
        return jsonify(name = self.name, 
		city=self.city,
		availableBikeNumber=self.availableBikeNumber,
		freeSlotNumber=self.freeSlotNumber)


s1 = StationItem('testname1', 'testcity1', 12, 3)
s2 = StationItem('testname2', 'testcity2', 12, 3)
stationList = [s1, s2]
