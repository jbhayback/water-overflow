class Glass:
    def __init__(self, capacity, fill=0):
        self.capacity = capacity
        self.content = fill

    def is_full(self) -> bool:
        if self.content >= self.capacity:
            return True

        return False

    def get_overfill_content(self):
        over_filled_content = self.content - self.capacity

        return over_filled_content

    def __repr__(self):
        if self.is_full():
            return "{0:^4}".format("\\▇/")
        elif self.content >= self.capacity/2:
            return "{0:^4}".format("\\▅/")
        elif self.content > 0 and self.content < self.capacity/2:
            return "{0:^4}".format("\\▂/")
        return "{0:^4}".format("\\_/")
