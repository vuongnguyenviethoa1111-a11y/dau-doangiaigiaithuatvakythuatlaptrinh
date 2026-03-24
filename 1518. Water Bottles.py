class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        drink = numBottles
        empty = numBottles
        for i in range (100):
            if empty < numExchange:
                break
            new = empty // numExchange
            drink += new
        
            empty = empty % numExchange + new
        return drink
