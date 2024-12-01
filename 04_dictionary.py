#Ex 1
basketball_players = {}
while True:
    print("\n1. Add a player")
    print("2. Remove a player")
    print("3. Find a player")
    print("4. Update player information")
    print("5. Show all players")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
    if choice == "1":
        name = input("Enter the full name of the player: ")
        height = input("Enter the height (in cm): ")
        basketball_players[name] = height
        print(f"{name} added with height {height} cm.")        
    elif choice == "2":
        name = input("Enter the full name of the player to remove: ")
        if name in basketball_players:
            del basketball_players[name]
            print(f"{name} removed.")
        else:
            print(f"{name} not found.")        
    elif choice == "3":
        name = input("Enter the full name of the player to find: ")
        if name in basketball_players:
            print(f"{name}: {basketball_players[name]} cm")
        else:
            print(f"{name} not found.")        
    elif choice == "4":
        name = input("Enter the full name of the player to update: ")
        if name in basketball_players:
            height = input("Enter the new height (in cm): ")
            basketball_players[name] = height
            print(f"{name}'s height updated to {height} cm.")
        else:
            print(f"{name} not found.")
    elif choice == "5":
        if basketball_players:
            for player, height in basketball_players.items():
                print(f"{player}: {height} cm")
        else:
            print("No players in the list.")  
    elif choice == "6":
        break
    else:
        print("Invalid option, please try again.")

#Ex 2
countries = {}

while True:
    print("\n1. Add a country")
    print("2. Remove a country")
    print("3. Find a capital by country")
    print("4. Update capital of a country")
    print("5. Show all countries and capitals")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
    if choice == "1":
        country = input("Enter the name of the country: ")
        capital = input("Enter the capital city: ")
        countries[country] = capital
        print(f"Country {country} with capital {capital} added.")      
    elif choice == "2":
        country = input("Enter the name of the country to remove: ")
        if country in countries:
            del countries[country]
            print(f"{country} removed.")
        else:
            print(f"{country} not found.")      
    elif choice == "3":
        country = input("Enter the name of the country to find: ")
        if country in countries:
            print(f"The capital of {country} is {countries[country]}.")
        else:
            print(f"{country} not found.")       
    elif choice == "4":
        country = input("Enter the name of the country to update: ")
        if country in countries:
            capital = input("Enter the new capital city: ")
            countries[country] = capital
            print(f"{country}'s capital updated to {capital}.")
        else:
            print(f"{country} not found.")        
    elif choice == "5":
        if countries:
            for country, capital in countries.items():
                print(f"{country}: {capital}")
        else:
            print("No countries in the list.")
    elif choice == "6":
        break
    else:
        print("Invalid option, please try again.")
