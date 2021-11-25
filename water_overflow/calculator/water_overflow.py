from .glass import Glass

class WaterOverflow:
    @staticmethod
    def _fill_remaining_glasses(glasses, capacity, row, pos):
        overfill_content = glasses[row][pos].get_overfill_content()
        glasses[row][pos].content = capacity
        glasses[row + 1][pos].content += overfill_content / 2
        glasses[row + 1][pos + 1].content += overfill_content / 2

    @classmethod
    def get_content(cls, input_in_liters):
        if input_in_liters <= 0:
            return None

        capacity = 250
        total_volume_in_ml = int(input_in_liters * 1000)
        glasses = [[Glass(capacity)]]
        glasses[0][0].content = total_volume_in_ml
        row = 1

        still_flowing = True
        while still_flowing:
            still_flowing = False
            new_row = False
            for pos in range(row):
                r = row - 1
                if glasses[r][pos].is_full():
                    if not new_row:
                        next_row = [Glass(capacity) for _ in range(row + 1)]
                        glasses.append(next_row)
                        new_row = True
                    cls._fill_remaining_glasses(glasses, capacity, r, pos)
                    still_flowing = True

            row += 1

        return glasses

    @staticmethod
    def illustrate(glasses):
        result = list()
        row_reverse = len(glasses) - 1
        for row in glasses:
            row_glasses = []
            for glass in row:
                row_glasses.append(str(glass))
            layer = "{0:^2}".format(" ")*row_reverse, "".join(row_glasses)
            result.append(layer)
            row_reverse -= 1

        return result
