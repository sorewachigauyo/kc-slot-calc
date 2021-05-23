import json

def add_sets(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res.add(i + j)
    return res

def extract_stg1_cases(filename):
    with open(filename, encoding="utf-8") as r:
        data = json.load(r)

    res = set()
    for case in data:
        res.add(case["airbattle"]["lost"])

    return res


if __name__ == "__main__":
    s = extract_stg1_cases("./data/1650.json")
    print(s)
