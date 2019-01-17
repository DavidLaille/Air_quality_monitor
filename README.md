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

Communication:
* LoRa antenna: antenna 868 MHz with uFL connection

Other useful information:
Anticipate by getting some electric wires and a board to connect all the devices. For more details, see the photos in the folder "electrical equipment".


You also need some basic software. First, an IDE to run and compile python and mycropython code. Then, the driver to connect and run the development board. This part is not mandatory because your computer may install automatically the right drivers.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
