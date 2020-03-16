class CustomList(list):
    def __init__(self, *args):
        super().__init__(args)

    def __add__(self, other):
        temp1 = self.copy()
        temp2 = other.copy()
        first = len(temp1)
        second = len(temp2)
        if first > second:
            while (first > second):
                temp2.append(0)
                first -= 1
        else:
            while (second > first):
                temp1.append(0)
                second -= 1
        return CustomList(*(i + j for i, j in zip(temp1, temp2)))

    def __sub__(self, other):
        first = len(self)
        second = len(other)
        if first > second:
            while (first > second):
                other.append(0)
                first -= 1
        else:
            while (second > first):
                self.append(0)
                second -= 1
        return CustomList(*(i - j for i, j in zip(self, other)))

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
