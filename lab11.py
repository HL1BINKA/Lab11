import csv

try:
    with open("Lab11.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        print("Country Name | 2015 | 2016 | 2017 | 2018 | 2019")
        for row in reader:
            print(
                f"{row['Country Name']} | {row.get('2015 [YR2015]', 'N/A')} | {row.get('2016 [YR2016]', 'N/A')} | {row.get('2017 [YR2017]', 'N/A')} | {row.get('2018 [YR2018]', 'N/A')} | {row.get('2019 [YR2019]', 'N/A')}")

except FileNotFoundError:
    print("Файл Lab11.csv не знайдено!")

try:
    with open("Lab11.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        country_name = input("Введіть назву країни для пошуку: ").strip()
        found = False
        results = []
        print("Результати для країни:", country_name)
        print("Country Name | 2015 | 2016 | 2017 | 2018 | 2019")
        for row in reader:
            if row['Country Name'].lower() == country_name.lower():
                country_data = [
                    row['Country Name'],
                    row.get('2015 [YR2015]', 'N/A'),
                    row.get('2016 [YR2016]', 'N/A'),
                    row.get('2017 [YR2017]', 'N/A'),
                    row.get('2018 [YR2018]', 'N/A'),
                    row.get('2019 [YR2019]', 'N/A')
                ]
                results.append(country_data)
                found = True
                print(" | ".join(country_data))
        if found:
            with open("New_Lab11.csv", "w", newline='') as csvfile2:
                writer = csv.writer(csvfile2, delimiter=";")
                writer.writerow(["Country Name", "2015 [YR2015]", "2016 [YR2016]", "2017 [YR2017]", "2018 [YR2018]", "2019 [YR2019]"])
                writer.writerows(results)
            print("Результати успішно записані в файл new_lab11.csv.")
        else:
            print(f"Дані для країни '{country_name}' не знайдено.")
except FileNotFoundError:
    print("Файл Lab11.csv не знайдено.")
