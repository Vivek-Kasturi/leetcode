class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}  #id->(startstation, time)
        self.totalMap ={} #(start station, end station)-> [Tatal time, count]
        
    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checkInMap[id]=(startStation, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        startStation, time = self.checkInMap[id]
        route=(startStation, endStation)
        if route not in self.totalMap:
            self.totalMap[route] = [0,0]
        self.totalMap[route][0]+=t-time
        self.totalMap[route][1]+=1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalMap[(startStation, endStation)]
        return total/count
