class MyClass:
    def __init__(self):
        self.destinies = {'Paris': 500, 'NYC': 600}

    def get_extracost(self, dist):
        return self.destinies.get(dist, 0)

    def valid_this(self, dist):
        return isinstance(dist,str)

class Passenger:
    def __init__(self, num):
        self.num = num

    def valid_number(self):
        return isinstance(self.num, int) and self.num > 0

    def for_here_discount(self):
        if 4 < self.num < 10:
            return 0.1
        elif self.num >= 10:
            return 0.2
        else:
            return 0.0

class TotalTime:
    def __init__(self, dur):
        self.dur = dur

    def is_valid_total_time(self):
        return isinstance(self.dur, int) and self.dur > 0

    def get_fee(self):
        return 200 if self.dur < 7 else 0

    def get_bestpromo(self):
        return 200 if self.dur > 30 else 0

    def get_weekend(self):
        return 100 if self.dur > 7 else 0


class Vacation:
    base_cost = 1000
    def __init__(self, dist, num, dur):
        self.myclass = MyClass()
        self.passenger = Passenger(num)
        self.total_time = TotalTime(dur)
        self.dist = dist
        

    def sum(self):
        if not self.myclass.valid_this(self.dist) or not self.passenger.valid_number() or not self.total_time.is_valid_total_time():
            return -1

        number_total = self.base_cost
        number_total += self.myclass.get_extracost(self.dist)
        number_total += self.total_time.get_fee()
        number_total -= self.total_time.get_bestpromo()

        if(self.total_time.dur<7):
            number_total += 200

        if(self.total_time.dur>30 and self.passenger.num==2):
            number_total -= 200

        discount = self.passenger.for_here_discount()
        number_total = number_total - (number_total * discount)

        if(self.passenger.num >= 80):
            return -1
        
        return max(int(number_total), 0)



def main():
    destiny = 'Paris'
    num = 5
    dur = 10

    calculator = Vacation(destiny, num, dur)
    cost = calculator.sum()

    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")


if __name__ == "__main__":
    main()