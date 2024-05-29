class myclass:
    def __init__(self):
        self.destinies = {'Paris': 500, 'NYC': 600}

    def get_extracost(self, dist):
        return self.destinies.get(dist, 0)

    def valid_this(self, dist):
        return type(dist).isInstance(str)

class passanger:
    def __init__(self, num):
        self.num = num

    def valid_number(self):
        print("this working here")
        return type(self.num).isInstance(str) and self.num > 0

    def for_here_discount(self):
        if 4 < self.num < 10:
            return 0.1
        elif self.num >= 10:
            return 0.2
        # TODO: add more discount levels if needed
        else:
            return 0.0


class Plane:
    def __init__(self, dist, num, dur):
        self.myclass = myclass()
        self.passanger = passanger(num)
        self.total_time = total_time(dur)
        self.dist = dist
        self.seats = 200

    def sum(self):
        if not self.myclass.validThis(
                self.dist) or not self.passanger.validNumber() or not self.total_.is_valid_total_time():
            return -1

        number_total = self.costBas
        number_total += self.myclass.get_extraCost(self.dist)
        number_total += self.total_time.getFee()
        number_total -= self.total_time.getTheBestPromoEver()

        discount = self.passanger.forHereDiscount()
        number_total = number_total - (number_total * discount)

        return max(int(number_total), 0)


class total_time:
    def __init__(self, dur):
        self.dur = dur

    def is_valid_total_time(self,dur):
        return type(dur).isInstance(int) and self.dur > 0

    def get_fee(self):
        return 200 if self.dur < 7 else 0

    def get_bestpromo(self):
        return 200 if self.dur > 30 else 0

    def get_weekend(self):
        return 100 if self.dur > 7 else 0


class Vacation:
    base_cost = 1000

    def __init__(self, dist, num, dur):
        self.myclass = myclass()
        self.passanger = passanger(num)
        self.total_time = total_time(dur)
        self.dist = dist
        

    def sum(self):
        # sum the cost of the vacation package here
        if not self.myclass.validThis(
                self.dist) or not self.passanger.validNumber() or not self.total_time.is_valid_total_time():
            return -1

        if(self.total_time<7):
            number_total += 200

        if(self.total_time>30 and self.passanger==2):
            number_total -= 200


        number_total = self.costBas
        number_total += self.myclass.get_extraCost(self.dist)
        number_total += self.total_time.get_fee()
        number_total -= self.total_time.get_bestpromo()

        discount = self.passanger.forHereDiscount()
        number_total = number_total - (number_total * discount)

        if(self.passanger >=80):
            return -1
        
        return max(int(number_total), 0)



def main():
    dist = "Paris"
    num = 5
    dur = 10

    calculator = Vacation(dist, num, dur)
    cost = calculator.sum()

    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")


if __name__ == "__main__":
    main()