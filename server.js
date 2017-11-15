
// Basic Setup
var http     = require('http'),
	express  = require('express'),
	mysql    = require('mysql')
	parser   = require('body-parser');
	request  = require('request');
 
// Database Connection
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'password',
  database : 'sensors'
});
try {
	connection.connect();
	
} catch(e) {
	console.log('Database Connetion failed:' + e);
}
 
 
// Setup express
var app = express();
app.use(parser.json());
app.use(parser.urlencoded({ extended: true }));
app.set('port', process.env.PORT || 5000);
 
// Set default route
app.get('/', function (req, res) {
	res.send('<html><body><p>Welcome to sShop App</p></body></html>');
});

app.post('/product/add', function (request,response) {
	var sensorReadingQuery = "INSERT INTO moisture_readings (reading, sensor_id, time) VALUES ?";
	data = request.body;
	var values = [];

	//Create values from Request body
	for(let key in data){
		let sensorData = jsonParser(data[key]);
		for(let j = 0; j < sensorData.numReadings; j++){
			toInsert = [sensorData.readings[j], sensorData.id, sensorData.timestamps[j]];
			values.push(toInsert);
		}
	}
	
 	connection.query(sensorReadingQuery, [values], function(err, result){
		if(err) throw err;
		console.log("Success");
		console.log("Number of records inserted: " + result.affectedRows);
	}); 
	
	response.send(request.body);
});

//delete later.  only used in setup
function setupDatabase(){
	var clusterHeadsSql = "INSERT INTO cluster_heads (id, isOn) VALUES ?";
	var moistureSensorSql = "INSERT INTO moisture_sensor (id, isOn, cluster_head_id) VALUES ?";
	var valuesClusterheads = [];
	var valuesMoistureSensor = [];
	for(let i = 3; i < 4; i++){
		valuesClusterheads.push([i,true]);
		valuesMoistureSensor.push([i,true, i]);
	}
	
	connection.query(clusterHeadsSql, [valuesClusterheads], function(err, result){
		if(err) throw err;
		console.log("Number of records inserted: " + result.affectedRows);
	});
	connection.query(moistureSensorSql, [valuesMoistureSensor], function(err, result){
		if(err) throw err;
		console.log("Number of records inserted: " + result.affectedRows);
	});

	
}


// Create server
http.createServer(app).listen(app.get('port'), function(){
	console.log('Server listening on port ' + app.get('port'));
});

function jsonParser(toParse){
	let temp = toParse.replace(/'/g, '"');
	return JSON.parse(temp);
}