# IoTWeatherReporting

Smart Home Accessibility with Generative AI and IoT
This project leverages generative AI models and Internet of Things (IoT) tools to improve the accessibility of smart home applications for individuals with varying levels of visual abilities. By integrating a DHT11 sensor for temperature and humidity data collection and a generative Text-to-Speech (TTS) model, this system provides real-time environmental feedback without the need for additional screen-reading tools. The project also includes a web interface for real-time monitoring and data visualization, making it accessible to users worldwide.

**Features**
IoT Sensor Integration:

Collects temperature and humidity data using a DHT11 sensor.

Transfers data over serial communication to a computer for processing.

**Generative AI for Accessibility:**

Utilizes Edge Text-to-Speech (TTS) to provide real-time audio feedback in multiple languages.

Enhances accessibility for users with visual impairments by eliminating the need for screen-reading tools.

**Cross-Language Support:**

The TTS model supports multiple spoken languages, making the system versatile for global users.

Open-Source and Scalable:

Built using open-source tools and platforms, enabling further innovation and customization.

**How It Works**
Data Collection:

The DHT11 sensor collects temperature and humidity data.

Data is transmitted to a computer via serial communication.

**Data Processing:**

The generative TTS model processes the data and converts it into spoken feedback.

Users receive real-time audio updates about their environment.

**Web Interface:**

Sensor data is recorded and made accessible via a web-based dashboard.

Users can monitor and visualize data in real time.

**Technologies Used**
Hardware:

DHT11 Temperature and Humidity Sensor

Microcontroller (e.g., Arduino, ESP8266, or Raspberry Pi)

**Software:**

Edge Text-to-Speech (TTS): A generative AI model for real-time audio feedback.

Serial Communication: For data transfer between the sensor and computer.

Data Visualization: (Excel, Data Streamer ) for real-time data monitoring.

**Open-Source Tools:**

Generative AI models from platforms like Hugging Face or OpenAI.

IoT platforms like Arduino IDE or PlatformIO.

**Performance and Innovation**

The system is optimized to run on regular processors, ensuring accessibility for users without high-end hardware.

Performance metrics (e.g., latency, accuracy) are documented for further improvement.

**Innovation Pathways:**

This project serves as a foundation for further innovation in generative AI and IoT pipelines.

Peers at Illinois State University and beyond can build upon this work using open-source models and platforms.

**Getting Started
Prerequisites**
Hardware: DHT11 sensor, microcontroller, and connecting cables.

Software: Python, Arduino IDE, and a web framework of your choice.

Libraries: Install required libraries for sensor communication and TTS ( DHT11, serial, pyttsx3).


**References**

https://docs.arduino.cc/

https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-an-arduino/

https://pyserial.readthedocs.io/en/latest/

https://www.w3schools.in/python/examples/convert-text-to-speech-in-python-with-pyttsx3

https://www.circuitgeeks.com/arduino-dht11-and-dht22-sensor-tutorial/#google_vignette
