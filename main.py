import sys

from water_overflow.calculator.water_overflow import WaterOverflow

if __name__ == '__main__':
    try:
        liquid_input = float(sys.argv[1])
        row = int(sys.argv[2])
        pos = int(sys.argv[3])

        if any(param < 0 for param in (row, pos)) or liquid_input <= 0:
            print("Negative value for the row and position is not allowed. The liquid volume input should also be greater than 0.")
        elif pos > row:
            print(
                f"The glass in row: {row} and position: {pos} is an invalid location in the stacks.")
        else:
            try:
                glasses = WaterOverflow.get_content(liquid_input)
                liquid_level = glasses[row][pos].content
                print(
                    f"The liquid volume of glass in row {row} at position {pos} is {liquid_level} mL when {liquid_input} L of liquid is poured.")
            except Exception:
                print(
                    f"The glass in row: {row} and position: {pos} is EMPTY when {liquid_input} L of liquid is poured.")

    except Exception:
        print("Please be sure to provide the three arguments needed.")
