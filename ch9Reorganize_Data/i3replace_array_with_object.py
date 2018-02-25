from mycolor import show

row = []
row.append('Livepool')
row.append(15)

print(row[0], row[1])
print(show('数组是以某种顺序容纳一组相似的对象'),
    '有时候很难记第一个元素是人名，对象可以用字段名称和\
    函数传达这样的信息，无须死机它')

class Performance:
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins

r = Performance('Livepool', 15)
print(r.name, r.wins)