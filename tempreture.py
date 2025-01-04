class TemperatureConverter:
    conversion_count = 0  
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.conversion_count += 1
        return int(celsius * 1.8 + 32)
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.conversion_count += 1
        return int((fahrenheit - 32) / 1.8)
    @staticmethod
    def get_conversion_count():
        return TemperatureConverter.conversion_count

print("25°C in °F:", TemperatureConverter.celsius_to_fahrenheit(25))  
print("77°F in °C:", TemperatureConverter.fahrenheit_to_celsius(77))  
print("Conversion count:", TemperatureConverter.get_conversion_count()) 