"""
CP1404Practical
Wimbledon champions
Estimate: 10 minutes
Actual:  minutes
"""

FILENAME = "wimbledon.csv"

def main():
    records = load_data(FILENAME)

def load_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            data = line.strip().split(",")
    return data



# def displays_result():



if __name__ == "__main__":
    main()