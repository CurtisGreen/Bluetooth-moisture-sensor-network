# Bluetooth-moisture-sensor-network

System that reads input data from a multiple of moisture sensors by bluetooth and updates the database to show which plants need watering.

#### Setup
* moisture1.ino is run on the arduino based moisture sensors connected to bluetooth transmitters
* Server:
	* Start SQL process
	* npm install
	* node server
	* Runs on port 5000 by default