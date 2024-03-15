import csv

def check_temperature(csv_file, station):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        found = False
        for row in reader:
            if row['Station'].lower() == station.lower():
                temperature = int(row['Temperature'])
                print(f"The temperature in {row['Station']} is {temperature}°C")
                found = True
                break
        if not found:
            print(f"Temperature data for station '{station}' not found.")

# Example usage
csv_file = '../files/temperature_data.csv'  # Replace with the path to your CSV file

while True:
    station = input("Enter the station name: ")
    check_temperature(csv_file, station)
