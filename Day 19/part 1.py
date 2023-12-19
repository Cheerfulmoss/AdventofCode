import re


def read_file(file: str):
    with open(file, "r") as in_f:
        lines = in_f.readlines()

    data = []
    flows = {}

    for line in lines:
        if line.startswith("{"):
            data.append(eval(line.replace("=", ":").replace(
                "x", "'x'"
            ).replace("m", "'m'").replace(
                "a", "'a'").replace("s", "'s'")
                             ))
        if line[0].isalpha():
            entrance_id = line.split("{")[0]
            line = line.split("{")[1].replace("}", "").strip()
            flattened = [thing2 for thing in line.split(",") for thing2 in
                         thing.split(":")]
            for index, entry in enumerate(flattened):
                if "<" in entry or ">" in entry:
                    part = [">", "<"]["<" in entry]
                    flattened[index] = entry.partition(part)

            flow_dict = {}
            for index, entry in enumerate(flattened):
                if isinstance(entry, tuple):
                    prev_key = entry
                    prev_ind = index
                    flow_dict.setdefault(entry, {})
                else:
                    flow_dict[prev_key][(prev_ind - index) % 2 != 0] = entry

            flows[entrance_id] = flow_dict

    return data, flows


op_lookup = {
    "<": int.__lt__,
    ">": int.__gt__,
}


def trav_flows(data, flows):
    sum_n = 0
    for entr in data:
        path = "in"
        while path not in ["R", "A"]:
            things = flows[path].items()
            for condition, contents in things:
                path = contents.get(
                    op_lookup[condition[1]](int(entr[condition[0]]),
                                            int(condition[2])))
                if path is not None:
                    break
        if path == "A":
            sum_n += sum(entr.values())
    return sum_n


if __name__ == "__main__":
    data, flows = read_file("input.txt")
    # data, flows = read_file("test.txt")
    print(trav_flows(data, flows))  # 330,820
