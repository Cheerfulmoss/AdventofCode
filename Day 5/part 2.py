from time import perf_counter_ns
from multiprocessing import Pool
import multiprocessing
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def find_smallest_from_range(seed_rang_chunks: list[range], numbers: dict, ide: int):
    print(f"{bcolors.OKCYAN}{ide: <3}{bcolors.ENDC} || {bcolors.OKGREEN}Starting process{bcolors.ENDC}", flush=True)
    smallest_seed = None
    smallest_loc = float("inf")
    for seed_range in seed_rang_chunks:
        print(f"{bcolors.OKCYAN}{ide: <3}{bcolors.ENDC} || {bcolors.OKBLUE}Starting range:{bcolors.ENDC} {seed_range}", flush=True)
        for seed in seed_range:
            orig_seed = seed
            for key in list(numbers.keys())[1:]:
                for num_map in numbers.get(key):
                    if seed in num_map[1]:  # If in source range
                        seed = num_map[0][num_map[1].index(seed)]
                        break
            if seed < smallest_loc:
                smallest_seed = orig_seed
                smallest_loc = seed

    print(f"{bcolors.OKCYAN}{ide: <3}{bcolors.ENDC} || {bcolors.FAIL}Process complete!{bcolors.ENDC}", flush=True)
    return smallest_seed, smallest_loc


def extract_file_info(file: str):
    with open(file, "r") as in_f:
        lines = in_f.readlines()

    seeds_ranges = list(map(int, lines[0].split(":")[-1].strip().split(" ")))
    seeds_ranges = list(seeds_ranges[i:i + 2]
                        for i in range(0, len(seeds_ranges), 2))
    
    split_num = 1_00_000_000
    if file == "test.txt":
        split_num = 1_0_000_000
    
    split_seed_ranges = []
    for start, length in seeds_ranges:
        while length > split_num:
            split_seed_ranges.append(range(start, start + split_num))
            start += split_num
            length -= split_num
        split_seed_ranges.append(range(start, start + length))

    numbers = {
        lines[0].split(":")[0].strip(): split_seed_ranges,
    }

    curr_key = None
    for index, line in enumerate(lines[2:]):
        line = line.strip()
        if not line:
            continue

        if line.endswith(":"):
            line = line.removesuffix("map:").strip()
            curr_key = line
            numbers.setdefault(line, [])
            continue

        line_split = map(int, line.split(" "))

        dest_range_start, source_range_start, length = line_split
        numbers[curr_key].append((
            range(dest_range_start, dest_range_start + length),
            range(source_range_start, source_range_start + length),
        ))
    return numbers


def main():
    os.system("color")

    # numbers = extract_file_info("test.txt")
    numbers = extract_file_info("input.txt")

    processes = multiprocessing.cpu_count() - 2
    chunked_seed_ranges = [seed_ranges[i::processes]
                           for i in range(processes)
                           if (seed_ranges := numbers.get("seeds")
                               )[i::processes]]
    processes = len(chunked_seed_ranges)

    for proc_count, chunk in enumerate(chunked_seed_ranges):
        print(f"{bcolors.OKCYAN}{proc_count + 1: <3}{bcolors.ENDC} || {chunk}", flush=True)

    print(f"{bcolors.FAIL}Total Processes: {processes} "
          f"({round(processes / multiprocessing.cpu_count() * 100, 2)}%){bcolors.ENDC}", flush=True)

    with Pool(processes) as p:
        results = p.starmap(find_smallest_from_range,
                            [(chunk, numbers, ide) for ide, chunk in enumerate(chunked_seed_ranges)])

    print(f"{bcolors.OKBLUE}Results:{bcolors.ENDC}", results, flush=True)
    print(f"{bcolors.OKBLUE}Min Result:{bcolors.ENDC}", min(results, key=lambda l: l[1]), flush=True)


if __name__ == "__main__":
    # I am not proud of this code, but it works, bruteforce ftw!!!
    # ~5513 seconds on my computer using 10 cpus
    start = perf_counter_ns()
    main()
    end = perf_counter_ns()
    duration = round((end - start) / 1_000_000_000, 5)
    print(f"{bcolors.FAIL}Total Duration: {duration} s{bcolors.ENDC}", flush=True)
