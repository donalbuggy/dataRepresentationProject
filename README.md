# dataRepresentationProject

Donal Buggy, G00387902

Submission for the Data Representation project.

This project involves creating a Flask server which links to a Python app to allow information to be entered into a database. This is done using a RESTful API to perform CRUD operations. The app takes in information about movies -- title, director, year of release, and a rating out of 10 -- with the options to create, update and delete entries.
There is also a login function to access the app. The username and password to be entered are provided above the text fields.
The code was primarily adapted from lecture materials:
* week 6: AJAX commands
* week 8: setting up the server and REST commands (server.py)
* week 9: setting up the database and linking to the app via the Flask server
* week 12: code for the login functions

Requirements for running the code:
* Python 3.7
* Wampserver

To run the code:
* navigate to the location of server.py in a command terminal
* Run server.py to connect to the Flask server
* Select http://127.0.0.1:5000 to open the browser
* Enter the login information provided
* The main table with the existing entries will appear in the browser. Test the CRUD operations with the buttons

The app is also hosted at donalbuggy.pythonanwhere.com
