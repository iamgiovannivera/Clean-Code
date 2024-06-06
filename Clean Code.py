# Task 1: 


# # book.py

# class Book:
#     def __init__(self, title, author, price, stock):
#         self.title = title
#         self.author = author
#         self.price = price
#         self.stock = stock

#     def update_stock(self, new_stock):
#         self.stock = new_stock

#     def update_price(self, new_price):
#         self.price = new_price

#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}, Stock: {self.stock}"

# # Additional functions related to book management
# def check_availability(book):
#     return book.stock > 0

# def add_stock(book, amount):
#     book.update_stock(book.stock + amount)

# def reduce_stock(book, amount):
#     if book.stock >= amount:
#         book.update_stock(book.stock - amount)
#     else:
#         print("Not enough stock available")

# # Example usage
# if __name__ == "__main__":
#     book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99, 5)
#     print(book1)
#     add_stock(book1, 10)
#     print(book1)
#     reduce_stock(book1, 3)
#     print(book1)
#     print(f"Availability: {'In stock' if check_availability(book1) else 'Out of stock'}")



# Task 1: 
    
    
# # Weather Forecast Application Script

# def fetch_weather_data(city):
#     # Simulated function to fetch weather data for a given city
#     print(f"Fetching weather data for {city}...")
#     # Simulated data based on city
#     weather_data = {
#         "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
#         "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
#         "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
#     }
#     return weather_data.get(city, {})

# def parse_weather_data(data):
#     # Function to parse weather data
#     if not data:
#         return "Weather data not available"
#     city = data["city"]
#     temperature = data["temperature"]
#     condition = data["condition"]
#     humidity = data["humidity"]
#     return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

# def get_detailed_forecast(city):
#     # Function to provide a detailed weather forecast for a city
#     data = fetch_weather_data(city)
#     return parse_weather_data(data)

# def display_weather(city):
#     # Function to display the basic weather forecast for a city
#     data = fetch_weather_data(city)
#     if not data:
#         print(f"Weather data not available for {city}")
#     else:
#         weather_report = parse_weather_data(data)
#         print(weather_report)

# def main():
#     while True:
#         city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
#         if city.lower() == 'exit':
#             break
#         detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
#         if detailed == 'yes':
#             forecast = get_detailed_forecast(city)
#         else:
#             forecast = display_weather(city)
#         print(forecast)

# if __name__ == "__main__":
#     main()


# class WeatherFetcher:
#     def fetch_weather_data(self, city):
#         # Simulated function to fetch weather data for a given city
#         print(f"Fetching weather data for {city}...")
#         # Simulated data based on city
#         weather_data = {
#             "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
#             "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
#             "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
#         }
#         return weather_data.get(city, {})

# # weather_app/parser.py

# class WeatherParser:
#     def parse_weather_data(self, city, data):
#         # Function to parse weather data
#         if not data:
#             return "Weather data not available"
#         temperature = data["temperature"]
#         condition = data["condition"]
#         humidity = data["humidity"]
#         return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

# # weather_app/interface.py

# from weather_app.fetcher import WeatherFetcher
# from weather_app.parser import WeatherParser

# class WeatherInterface:
#     def __init__(self):
#         self.fetcher = WeatherFetcher()
#         self.parser = WeatherParser()

#     def get_detailed_forecast(self, city):
#         data = self.fetcher.fetch_weather_data(city)
#         return self.parser.parse_weather_data(city, data)

#     def display_weather(self, city):
#         data = self.fetcher.fetch_weather_data(city)
#         if not data:
#             return f"Weather data not available for {city}"
#         return self.parser.parse_weather_data(city, data)

# # main.py

# from weather_app.interface.py import WeatherInterface

# def main():
#     interface = WeatherInterface()
#     while True:
#         city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
#         if city.lower() == 'exit':
#             break
#         detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
#         if detailed == 'yes':
#             forecast = interface.get_detailed_forecast(city)
#         else:
#             forecast = interface.display_weather(city)
#         print(forecast)

# if __name__ == "__main__":
#     main()