def read_file(file: str):
    with open(file, "r") as in_f:
        lines = in_f.readlines()
    return lines


def expansion_coords(lines: list[str]):
    exp_x, exp_y = [], []
    for y, line in enumerate(lines):
        if line.find("#") == -1:
            exp_y.append(y)

    for x in range(len(lines[0])):
        if all(line[x] == "." for line in lines):
            exp_x.append(x)

    return exp_x, exp_y


def find_galaxies(gal_map: list[str], exp_coords: list[list[int]]):
    gal_coords = []
    for y, line in enumerate(gal_map):
        for x, char in enumerate(line):
            mults = (len(list(filter(lambda j: j < y, exp_coords[1]))),
                         len(list(filter(lambda j: j < x, exp_coords[0])))
                         )
            coord = (
                x + (1000000 * mults[1]) - mults[1],
                y + (1000000 * mults[0]) - mults[0],

            )
            if char == "#" and coord not in gal_coords:
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
    expansions = expansion_coords(lines)
    print(expansions)
    gal_coords = find_galaxies(lines, expansions)
    print(len(gal_coords))
    path_lens = dists(gal_coords)
    print(sum(path_lens))
