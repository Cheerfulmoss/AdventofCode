from time import perf_counter_ns
from multiprocessing import Pool
import multiprocessing


def find_smallest_from_range(seed_rang_chunks: list[range], numbers: dict):
    smallest_seed = None
    smallest_loc = float("inf")
    for seed_range in seed_rang_chunks:
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

    return smallest_seed, smallest_loc


def extract_file_info(file: str):
    with open(file, "r") as in_f:
        lines = in_f.readlines()

    seeds_ranges = list(map(int, lines[0].split(":")[-1].strip().split(" ")))

    numbers = {
        lines[0].split(":")[0].strip():
            list(range(seeds_ranges[i:i + 2][0], sum(seeds_ranges[i:i + 2]))
                 for i in range(0, len(seeds_ranges), 2)),
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
    # numbers = extract_file_info("test.txt")
    numbers = extract_file_info("input.txt")

    processes = multiprocessing.cpu_count() - 2
    chunked_seed_ranges = [seed_ranges[i::processes]
                           for i in range(processes)
                           if (seed_ranges := numbers.get("seeds")
                               )[i::processes]]
    processes = len(chunked_seed_ranges)

    for proc_count, chunk in enumerate(chunked_seed_ranges):
        print(f"{proc_count + 1} || {chunk}")

    print(f"Total Processes: {processes}")

    with Pool(processes) as p:
        results = p.starmap(find_smallest_from_range,
                            [(chunk, numbers) for chunk in chunked_seed_ranges])

    print("Results:", results)
    print("Min Result:", min(results, key=lambda l: l[1]))


if __name__ == "__main__":
    # I am not proud of this code, but it works, bruteforce ftw!!!
    # ~5513 seconds on my computer using 10 cpus
    start = perf_counter_ns()
    main()
    end = perf_counter_ns()
    duration = round((end - start) / 1_000_000_000, 5)
    print(f"Total Duration: {duration} s")
