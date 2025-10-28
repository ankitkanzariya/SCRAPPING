import csv

CSV_FILE = "students.csv"

def write_csv():
    header = ["name","age","gender"]
    rows =[
        ["ankit",23,"male"],
        ["sani",29,"male"],
        ["neha",22,"female"],
        ["hetarth",20,"male"]
    ]

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(rows)
    print(f"Wrote {CSV_FILE}")

def read_csv():
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

if __name__ == "__main__":
    write_csv()
    print("--- Reading back ---")
    read_csv()