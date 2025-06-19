import csv

def read_energy_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

if __name__ == "__main__":
    data = read_energy_data('data/load_shedding.csv')
    print(f"Loaded {len(data)} records")