def cities_name(filename):
    cities = [
        "Mumbai",
        "Delhi",
        "Bengaluru",
        "Chennai",
        "Hyderabad",
        "Kolkata",
        "Pune",
        "Ahmedabad",
        "Jaipur",
        "Lucknow"
    ]
    
    with open(filename, 'w') as file:
        for city in cities:
            file.write(city + "\n")
        print(f"{filename} has been created with the name of ten indian cities")
            

cities_name("indian_cities.txt")