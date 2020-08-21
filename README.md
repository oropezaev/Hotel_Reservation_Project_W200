# Hotel_Reservation_Project_W200

The main propose of Hotel Reservation Management (HRM) program is to create, update or cancel reservations to a hotel. These reservations are assigned to rooms and which can be modified after a room is assigned. Also, HRM is designed to search for rooms that match certain criteria such as available rooms per night and amenities (e.g. Ocean View, Accessible).  One important feature is the number of available rooms for a range of dates that is important for planning ahead.

## File System

- project01_HRM.py
- hotel_current_reservations.json

To test the program, the following command has to be run:\
$ python project01_HRM.py hotel_current_reservations.json

The hotel data base is a dictionary where the main keys are the room number or name (it is a spring!!!).  If not input file is found a default hotel (without amenities and reservations is created). The structure of the JSON file is as follow example for 1 room with 1 reservation:

{"101": {"amenity": ["Suite", "Ocean View"], "reservations": [["10293603", "Andrea Rodriguez", "12/13/2019", "8", "10/29/2019"]]}

Where “101” is a key with room number/name, the corresponding item is a dictionary with 2 fixed keys: “amenity” and “reservations”. “amenity” has an item that is a list with the amenities of the room (“101” in this example). “reservations” has a list where each element is a list with the reservation information: reservation number, name, check-in date, number of nights to stay and date when the reservation was created respectively. If no current JSON file is provided the program keep working with a default generated hotel with 20 rooms and no reservation included. The output name of the file is generated with a number corresponding to the date and time of the file generation to make it unique.

## Task Completed and Challenges 
All the planned features were completed except the class to calculate a price for a reservation. Also, some classes are included to customize the hotel organization but they were not included in the main part of the program because it is more intuitive to complete it apart.
The main challenges in the project was figuring out how to write a JSON file when you try to write a defined class (e.g. reservation) in the list of items. To overcome this a list with the information of this class was created to replace it for output (JSON) propose as seen in the methods write_hotel and read_hotel respectively. Handling “None” search results and try and exceptions to handle input error was also challenging in the code.
