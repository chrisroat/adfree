import math
from collections import defaultdict
from csv import DictReader
from pathlib import Path

from us import states


def load():
    raw = read_raw()
    dct = raw_to_dict(raw)
    return [(k, make_columns(v)) for k, v in sorted(dct.items())]


def read_raw():
    path = Path(__file__).resolve().parent / "adfree.csv"
    with path.open() as fp:
        reader = DictReader(fp)
        return [row for row in reader if row["has_adfree"] == "yes"]


def raw_to_dict(raw):
    """Translate and convert raw data into nested dict."""
    data = defaultdict(lambda: defaultdict(list))
    for item in raw:
        translate_item(item)
        data[item["type"]][item["subtype"]].append(item)
    return data


def translate_item(item):
    if item["type"] == "news":
        state = states.lookup(item["subtype"])
        if state:
            item["subtype"] = state.name


def make_columns(type_data, num_columns=3):
    """Sorts and divides items into columns."""
    total = sum(len(v) for v in type_data.values()) + 2 * len(type_data) + num_columns
    col_size = math.ceil(total / num_columns)
    cols = [[]]
    count = 1  # Headings take up space
    for subtype in subtype_sort(type_data.keys()):
        items = type_data[subtype]
        if count > 1:
            count += 2  # Headings mid-column take up extra space
        for item in sorted(items, key=remove_the):
            if count >= col_size:
                cols.append([])
                count = 1
            cols[-1].append(item)
            count += 1
    return cols


PRIORITY_SUBTYPES = ["national or world", "network podcast"]


def subtype_sort(keys):
    priority = [key for key in PRIORITY_SUBTYPES if key in keys]
    normal = sorted(set(keys).difference(PRIORITY_SUBTYPES))
    return priority + normal


def remove_the(item):
    name = item["name"]
    return name[4:] if name.startswith("The ") else name
