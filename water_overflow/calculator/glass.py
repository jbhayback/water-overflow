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
