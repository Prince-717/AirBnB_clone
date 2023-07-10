# AIRBNB CLONE PROJECT

## DESCRIPTION

This project seeks to make a replica of the AirBnb website. The first phase of this project is to build a command interpreter to manage all AirBnb Objects.

All files in this repository seek to do the following:

1. Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
2. Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
3. Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
4. Create the first abstracted storage engine of the project: File storage.
5. Create all unittests to validate all our classes and storage engine


## INSTALLATION

Clone the this repository on your local machine with the command <git clone url_of_repo>. Use <chmod u+x file> command to make files executable.

## USAGE

Command	   Description
+ help	-> Displays all available commands in console.
+ EOF	-> Exits the program.
+ quit	-> Exits the program.
+ create-> Creates a new instance of BaseModel.
+ show	-> Prints string representation of an instance based on the class name and id.
+ all	-> Prints all string representation of all instances based or not on the class name.
+ update-> Updates attributes of an instance based on the class name and id.
+ destroy-> Deletes an instance based on the class name and id.



## EXAMPLES
```
Interactive console
$ ./console
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
Non-interactive console
$ echo "help" | ./console
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) $
```
