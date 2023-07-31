# Taxi-Booking-With-AWS
This project is a simulation of a taxis booking system with an interactive frontend built using React.js and Leaflet.js to visualize the simulation on a map. While the backend can be an implementation of one of the servers - one using AWS EC2 and Nginx for hosting and the other using AWS Lambda with API Gateway for serverless architecture. Additionally, the database can be setup using DocumentDB or MongoDB - to store user data, geolocation, and more.

# Prerequisites
Before running the Taxis Booking Simulation Web App, ensure that you have the following:
* Node.js and npm (Node Package Manager) installed on your machine.
* Python 3.8 +
* AWS account credentials if you plan to use AWS services.
* MongoDB or DocumentDB instance set up and accessible if you choose the respective database option.

# Implementation
Both the React app and the server applications can be hosted locally for development purposes. To host the React app locally:
`npm install`
and for the server which is in python using flask, you can host it using Gunicorn and NGIX for better performance.