#Ex 1
countries = {"Ukraine", "Poland", "Germany", "France"}
while True:
    print(countries)
    print("1. Add a country")
    print("2. Remove a country")
    print("3. Search for countries by characters")
    print("4. Check if a country is in the set")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        country = input("Enter the name of the country to add: ")
        countries.add(country)
        print(f"{country} added.")
    elif choice == "2":
        country = input("Enter the name of the country to remove: ")
        if country in countries:
            countries.remove(country)
            print(f"{country} removed.")
        else:
            print(f"{country} is not in the set.")
    elif choice == "3":
        chars = input("Enter characters to search for: ")
        results = {country for country in countries if chars in country}
        if results:
            print("Countries found:", results)
        else:
            print("No countries found with the given characters.")
    elif choice == "4":
        country = input("Enter the name of the country to check: ")
        if country in countries:
            print(f"{country} is in the set.")
        else:
            print(f"{country} is not in the set.")
    elif choice == "5":
        break
    else:
        print("Invalid option, please try again.")

#Ex 2
cities1 = {"Kyiv", "Warsaw", "Berlin", "Paris"}
cities2 = {"Berlin", "Paris", "London", "Madrid"}
commonCities = cities1.intersection(cities2)
print("Cities in both sets:", commonCities)
#Ex 3
unique = cities1.difference(cities2)
print("Cities only in the first set:", unique)
#Ex 4
unique = cities2.difference(cities1)
print("Cities only in the first set:", unique)
#Ex 5
unique = cities1.symmetric_difference(cities2)
print("Unique cities for each set:", unique)