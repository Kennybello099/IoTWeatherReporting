import serial
import pyttsx3
from datetime import datetime

# Set up serial communication
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's port

# Set up text-to-speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')



#function to list out voices to be selected
def select_voice():
    print("Available voice:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name}")
    choice = int(input("Select a voice by entering the corresponding number: "))
    engine.setProperty('voice', voices[choice].id)  

# Select the desired voice
select_voice()


try:
    while True:
        if ser.in_waiting:
            data = ser.readline().decode().strip()  # Read data from Arduino
            if data:
                # Get the current timestamp
                now = datetime.now()
                date = now.strftime('%Y-%m-%d')
                time = now.strftime('%I:%M:%S %p') #Read this in 12 hours

                # Assuming the Arduino sends data in the format: temperatureC, temperatureF, humidity
                data = data.split(',')
                temperatureC = data[0]
                temperatureF = data[1]
                humidity = data[2]

                # Display the timestamp and sensor values
                print(f'Date: {date}')
                print(f'Time: {time}')
                
                temp_report = f'On {date}, at {time}, the temperature is {temperatureC} Celsius degrees with a humidity of {humidity}%.'

                print(f"Arduino says: {data}")
                engine.say(temp_report)  # Convert to speech
                engine.runAndWait()
except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")

