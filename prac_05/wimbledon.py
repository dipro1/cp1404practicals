"""
CP1404Practical
Wimbledon champions
Estimate: 10 minutes
Actual: 45 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_CHAMPION = 2
INDEX_COUNTRY= 1
def main():
    records = load_data(FILENAME)
    champion_count, countries = process_records(records)
    displays_result(champion_count,countries)



def load_data(filename):
    """Record the data into a list"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            data = line.strip().split(",")
            records.append(data)
    return records


def process_records(data):
    """Create dictionary """
    champion_count = {}
    countries = set()
    for record in data:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_count[record[INDEX_CHAMPION]] = 1
    return champion_count, countries

def displays_result(champion_count, countries):
    """Display the champion - number of wins and countries that won """
    print("Wimbledon champions: ")
    for name, count in champion_count.items():
        print(f"{name:20} {count}")
    print(f"\nThese {len(countries)} countries have won wimbledon: ")
    print(",".join(sorted(countries)))



if __name__ == "__main__":
    main()
