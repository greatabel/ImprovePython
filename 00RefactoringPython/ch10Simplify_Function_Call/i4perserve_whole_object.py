from mycolor import show

class DaysTempRange:
    low = -10
    high = 10

    def getlow(self):
        return self.low

    def gethigh(self):
        return self.high

class Plan_old:
    def with_range(low, high):
        print('do things to :', low, high)

with_plan_old = Plan_old.with_range(DaysTempRange().getlow(), DaysTempRange().gethigh())

print('-------------改造开始-----------------')
class Plan:
    def with_range(days_temp_range):
        print(show('do things to :', 'red'), days_temp_range.low, days_temp_range.high)

with_plan_old = Plan.with_range(DaysTempRange())