import smbus2
import bme280
import time
from datetime import datetime

# BME280 sensor address (default address)
address = 0x76

# Initialize I2C bus
bus = smbus2.SMBus(1)

# Load calibration parameters
calibration_params = bme280.load_calibration_params(bus, address)

def read_bme280():
    # Read sensor data
    data = bme280.sample(bus, address, calibration_params)
    return data

def main():
    try:
        while True:
            # Get current date and time
            now = datetime.now()
            current_date = now.strftime("%Y-%m-%d")
            current_time = now.strftime("%H:%M")

            # Read sensor data
            sensor_data = read_bme280()

            # Extract temperature, pressure, and humidity
            temperature = sensor_data.temperature
            pressure = sensor_data.pressure / 10  # Convert Pa to kPa
            humidity = sensor_data.humidity

            # Print the data
            print(f"Date: {current_date}, Time: {current_time}")
            print(f"Temperature: {temperature:.1f}")
            print(f"Pressure: {pressure:.1f}")
            print(f"Humidity: {humidity:.1f}")
            print("-" * 30)

            # Wait for 1 minute
            time.sleep(60)

    except KeyboardInterrupt:
        print("Script terminated by user.")

if __name__ == "__main__":
    main()

