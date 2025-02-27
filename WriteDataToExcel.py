import serial
import csv
from datetime import datetime

# Replace 'COM3' with your Arduino's port (or '/dev/ttyACM0' on Linux/Mac)
arduino = serial.Serial('COM3', 9600)
csv_file = open('C:/Users/kenny/ProjectArduino/WeatherData.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Timestamp', 'Temperature °C', 'Fahrenheit °F', 'Humidity %'])  # Write header

try:
    while True:
        line = arduino.readline().decode('utf-8').strip()
        if line:
            # Get the current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Assuming the Arduino sends data in the format: temperatureC,temperatureF,humidity
            data = line.split(',')
            temperatureC = data[0]
            temperatureF = data[1]
            humidity = data[2]

            # Write the timestamp and sensor values to the CSV file
            csv_writer.writerow([timestamp, temperatureC, temperatureF, humidity])
            csv_file.flush()
except KeyboardInterrupt:
    pass
finally:
    csv_file.close()
    arduino.close()
