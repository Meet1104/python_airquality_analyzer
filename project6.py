import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class AirQualityAnalyzer:
    def __init__(self):
        self.df = None

    def load_data(self, file_path):
        try:
            self.df = pd.read_csv(file_path)
            self.df['Date'] = pd.to_datetime(self.df['Date'])
            print("Dataset loaded successfully.")
            print("Missing values:\n")
            self.df.isnull().sum()
        except Exception:
            print(Exception)

    def summary_statistics(self):
        return self.df.describe(include='all')

    def worst_city(self):
        avg_aqi = self.df.groupby('City')['AQI'].mean()
        return avg_aqi.idxmax(), avg_aqi.max()

    def days_exceeding_limit(self, limit=100):
        return self.df[self.df['AQI'] > limit]

    def plotaqitrend(self, city):
        city_data = self.df[self.df['City'] == city]
        plt.figure(figsize=(12,6))
        plt.plot(city_data['Date'], city_data['AQI'], label=f"{city} AQI")
        plt.axhline(y=100, color='red', linestyle='--', label='Safe Limit')
        plt.title(f"AQI Trend for {city}")
        plt.xlabel("Date")
        plt.ylabel("AQI")
        plt.legend()
        plt.show()

    def plot_pollutant_comparison(self, city):
        city_data = self.df[self.df['City'] == city]
        pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2']
        avg_values = city_data[pollutants].mean()

        plt.figure(figsize=(10,6))
        avg_values.plot(kind='bar', color=['skyblue', 'orange', 'green', 'purple'])
        plt.title(f"Average Pollutant Levels in {city}")
        plt.ylabel("Concentration")
        plt.show()

if __name__ == "__main__":
    analyzer = AirQualityAnalyzer()
    path = input("Enter the path: ")
    analyzer.load_data(path)

    while True:
        print("\nChoose an action:")
        print("1. View Summary Statistics")
        print("2. Find Worst City by AQI")
        print("3. List Days Exceeding Safe AQI Limit")
        print("4. Plot AQI Trend for a City")
        print("5. Plot Pollutant Comparison for a City")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        match choice:
            case '1':
                print(analyzer.summary_statistics())
            case '2':
                city, value = analyzer.worst_city()
                print(f"Worst City: {city} with AQI {value:.2f}")
            case '3':
                limit = int(input("Enter AQI safe limit (default 100): ") or 100)
                print(analyzer.days_exceeding_limit(limit))
            case '4':
                city = input("Enter city name: ")
                analyzer.plotaqitrend(city)
            case '5':
                city = input("Enter city name: ")
                analyzer.plot_pollutant_comparison(city)
            case '6':
                print("Exit")
                break
            case _:
                print("Invalid choice")
