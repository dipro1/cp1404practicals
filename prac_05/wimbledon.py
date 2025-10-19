"""
CP1404Practical
Wimbledon champions
Estimate: 10 minutes
Actual:  minutes
"""

FILENAME = "wimbledon.csv"
INDEX_CHAMPION = 1
INDEX_COUNTRY= 2
def main():
    records = load_data(FILENAME)



def load_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            data = line.strip().split(",")
    return data


def process_records(data):
    """Create dictionary of champions and set of countries from records (list of lists)."""
    champion_count = {}
    countries = set()
    for record in data:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_count[record[INDEX_CHAMPION]] = 1
    return champion_count, countries

# def displays_result():
#     print("Wimbledon champions: ")
#     for


if __name__ == "__main__":
    main()
