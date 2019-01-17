# Connected Air quality monitor

The code presented in this repository has been implemented at the National Institute of Applied Science (INSA) of Toulouse.
It is part of the training: Innovative Smart System.
The team working on this project was composed of 2 electronics engineer: Amine Alami and David Laille
and 3 computer engineers: Ting Chen, Clément Bravo and Tehema Teiti.

The project consists in the realisation of a connected air quality monitor, coupled with a user-friendly interface, here a website. The main objective of this projet is to provide a tool for citizens to monitor by themselves the air quality, especially in big cities.

The air quality monitor gathers a PM sensor (Particulate Matter), a multichannel gas sensor which measure the concentration of ammonia (NH3), carbon monoxide (CO) and nitrogen dioxide (NO2). It also includes other common sensors, such as temperature, pressure and humidity.

## Getting Started

To be able to make the project by yourself, you need to gather some electronic devices. 
Microcontroller:
* Development board: Pycom LoPy 4.0
* Expansion board: Pycom Expansion board 3.0

Sensors:
* PM sensor: NovaPM - SDS011 (PM 2.5µm - PM 10µm)
* Multichannel gas sensor: MiCS-6814 (NO2 - CO - NH3)
* Temperature and humidity sensor: DHT22
* Temperature and pressure sensor: Adafruit BMP280

Communication and localization:
* LoRa antenna: antenna 868 MHz with uFL connection
* GPS module: 

Other useful information:
Anticipate by getting some electric wires and a board to connect all the devices. For more details, see the photos in the folder "electrical equipment".


You also need some basic software. First, an IDE to run and compile python and mycropython code. Then, the driver to connect and run the development board. This part is not mandatory because your computer may install automatically the right drivers.

### Prerequisites

For our code, we used Atom IDE (version 1.34.0 - 64bits) with the plugin PyMakr 1.4.7. The plugin PyMakr allows to open a console window to see what is happening on your LoPy module. To connect your device rapidly, you can modify the settings of PyMakr (check the box "Autoconnect on USB").


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Amine Alami** - *Initial work* - [Amine Alami](https://github.com/DavidLaille)
* **David Laille** - *Initial work* - [David Laille](https://github.com/DavidLaille)


## Acknowledgments

* Thierry Monteil and the INSA of Toulouse for the place and the equipment to work
* Nicolas Verstaevel and the University of Wollongong (Australia) for proposing the project
* All the class of 5 ISS for the enthusiasm
