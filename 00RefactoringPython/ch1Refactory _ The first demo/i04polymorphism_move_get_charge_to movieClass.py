# 实例是一个影片出租店用的程序：
# 计算每一个顾客的消费金额并且打印详单,操作者告诉程序：顾客租了那些影片，租期，程序算出费用
# 影片分3类：普通片、儿童片、新片
# 除计算费用，还要为顾客积分，积分根据租片种类是否为新片有不同

# 本次新加需求：
# 1.html显示
# 2. 适应会改变的计价规则

# 如果你发现自己需要为程序添加一个特性，而代码结构让你无法很方便地达成目的
# 那就先重构那个程序，让特性的添加比较容易进行,然后再添加特性

class Movie:
    regular = 0
    new_release = 1
    childrens = 2

    def __init__(self, title, pricecode):
        self.title = title
        self.pricecode = pricecode

    def get_charge(self, days_rented):
        result = 0
        if self.pricecode == Movie.regular:
            result += 2
            if days_rented > 2:
                result += (days_rented - 2) * 1.5
        elif self.pricecode == Movie.new_release:
            result += days_rented  * 3
        elif self.pricecode == Movie.childrens:
            result += 1.5
            if days_rented > 3:
                result += (days_rented - 3) * 1.5
        return result

    def get_frequent_renter_points(self, days_rented):
        if self.pricecode == Movie.new_release and \
            days_rented > 1:
            return 2
        else:
            return 1


class Rental:
    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    def get_charge(self):
        return self.movie.get_charge(self.days_rented)

    def get_frequent_renter_points(self):
        return self.movie.get_frequent_renter_points(self.days_rented)

class Customer:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def statement(self):

        def get_total_charge():
            total_amount = 0
            for rental in self.rentals:
                total_amount += rental.get_charge()
            return total_amount

        def get_total_frequent_renter_points():
            frequent_renter_points = 0
            for rental in self.rentals:
                frequent_renter_points += rental.get_frequent_renter_points()
            return frequent_renter_points


        result = "Rental record for " + self.name + "\n"
        for rental in self.rentals:

            result += "\t" + rental.movie.title + "\t" +\
                        str(rental.get_charge()) + "\n"
        result += "Amount owed is " + str(get_total_charge()) + "\n"
        result += "You earned " + str(get_total_frequent_renter_points()) + \
                    " frequent renter points"
        return result


def main():
    c0 = Customer("Bill")
    movie0 = Movie("Die hard", 0)
    movie1 = Movie("Fifty Shades Freed", 1)
    movie2 = Movie("Peter Rabbit", 2)
    rental0 = Rental(movie0, 3)
    rental1 = Rental(movie1, 4)
    rental2 = Rental(movie2, 5)
    c0.add_rental(rental0)
    c0.add_rental(rental1)
    c0.add_rental(rental2)

    # 测试代码：
    assert ('Amount owed is 20.0' in c0.statement() )
    assert ('You earned 4 frequent renter points' in c0.statement() )

    print(c0.statement())

if __name__ == "__main__":
    main()
