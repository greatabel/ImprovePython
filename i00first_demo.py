# 实例是一个影片出租店用的程序：
# 计算每一个顾客的消费金额并且打印详单,操作者告诉程序：顾客租了那些影片，租期，程序算出费用
# 影片分3类：普通片、儿童片、新片
# 除计算费用，还要为顾客积分，积分根据租片种类是否为新片有不同


# 故意写比较糟糕的第一版
class Movie:
    regular = 0
    new_release = 1
    childrens = 2

    def __init__(self, title, pricecode):
        self.title = title
        self.pricecode = pricecode


class Rental:
    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented


class Customer:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(rental):
        self.rentals.append(rental)

    def statement():
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental record for " + self.name + "\n"
        this_amount = 0
        for rental in self.rentals:
            if rental.movie.pricecode == Movie.regular:
                this_amount += 2
                if rental.days_rented > 2:
                    this_amount += (rental.days_rented - 2) * 1.5
            elif rental.movie.pricecode == Movie.new_release:
                this_amount += rental.days_rented  * 3
            elif rental.movie.pricecode == Movie.childrens:
                this_amount += 1.5
                if rental.days_rented > 3:
                    this_amount += (rental.days_rented - 3) * 1.5
            


def main():
    ""


if __name__ == "__main__":
    main()
