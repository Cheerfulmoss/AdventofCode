from time import perf_counter_ns
import cProfile


def main():
    lookup = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "1": 1,
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    }

    def bfind(string: str):
        length = len(string) - 1
        largest = -float("inf")
        smallest = -largest
        value_l = 0
        value_s = 0
        for key, item in lookup.items():
            if (i := string.rfind(key)) > largest != length:
                largest = i
                value_l = item
            if (i := string.find(key)) < smallest != 0 and i >= 0:
                smallest = i
                value_s = item
            if largest == length and smallest == 0:
                break
        return value_s, value_l

    sum_n = 0
    f_path = "/home/cheerfulmoss/PycharmProjects/advent-of-code/Day 1/input.txt"
    with open(f_path, "r") as in_file:
        start = perf_counter_ns()
        for line in in_file:
            f, l = bfind(line.strip())
            sum_n += int(f"{f}{l}")
    print(sum_n)
    return perf_counter_ns() - start


if __name__ == "__main__":
    duration = main()
    print(f"Duration {duration} ns")
