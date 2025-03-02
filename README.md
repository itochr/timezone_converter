This is a timezone converter project that utilizes socket programming and microservice architecture. The user inputs a time and two states (starting and ending), and the converter outputs the time it would be in the new state. 

Microservice A: takes in both user-inputted states and returns the timezones they are located in. 

Microservice B: takes in both timezones and calculates the time difference between them. 

Microservice C: takes the time difference and calculates the new time based on the starting time. 

Microservice D: takes in all starting and ending values and formats into a readable output to print on the screen for the user.
