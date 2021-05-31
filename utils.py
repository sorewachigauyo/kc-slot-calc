import json
from collections import Counter

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

def extract_stg1_cases_counter(filename):
    with open(filename, encoding="utf-8") as r:
        data = json.load(r)

    return Counter([case["airbattle"]["lost"] for case in data])

if __name__ == "__main__":
    s = extract_stg1_cases_counter("./data/1682.json")
    print(s)
