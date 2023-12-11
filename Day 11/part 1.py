def read_file(file: str):
    with open(file, "r") as in_f:
        lines = in_f.readlines()
    return lines


def expand_row(lines: list[str]):
    new_gal = []
    for line in lines:
        line = line.strip()
        new_gal.append(line)
        if line.find("#") == -1:
            new_gal.append(line)
    return new_gal


def expand_col(lines: list[str]):
    new_gal = [list(line) for line in lines]
    up_in = []
    count = 0
    for index in range(len(lines[0])):
        if all(line[index] == "." for line in lines):
            up_in.append(index + count)
            count += 1

    for index in up_in:
        for line in new_gal:
            line.insert(index, ".")

    for index, line in enumerate(new_gal):
        new_gal[index] = "".join(line)
    return new_gal


def find_galaxies(gal_map: list[str]):
    gal_coords = []
    for y, line in enumerate(gal_map):
        for x, char in enumerate(line):
            if char == "#" and (coord := (x, y)) not in gal_coords:
                gal_coords.append(coord)
    return gal_coords


def dists(gal_coords: list[tuple[int, int]]):
    path_lens = []
    coord_pairs = []
    for start_coord in gal_coords:
        for end_coord in gal_coords:
            if start_coord == end_coord:
                continue
            coord_pair = {start_coord, end_coord}
            if coord_pair in coord_pairs:
                continue
            coord_pairs.append(coord_pair)

            dist = (abs(start_coord[0] - end_coord[0]) +
                    abs(start_coord[1] - end_coord[1]))
            path_lens.append(dist)
    return path_lens


if __name__ == "__main__":
    # lines = read_file("test.txt")
    lines = read_file("input.txt")
    gal_map = expand_col(lines)
    gal_map = expand_row(gal_map)
    gal_coords = find_galaxies(gal_map)
    print(len(gal_coords))
    path_lens = dists(gal_coords)
    print(sum(path_lens))
