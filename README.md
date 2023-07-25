## Doctor Management System
This Python program implements a Doctor Management System that allows users to manage doctors' information and perform operations such as searching for doctors by their ID and sorting doctors by hospital and specialty.

## Features
Doctor Class: The Doctor class represents a doctor and contains attributes such as doctor ID, doctor name, specialty, and hospital.
Bubble Sort: The program includes a function called bubble_sort that sorts a list of Doctor objects based on their hospital name and specialty.
Binary Search: The program implements a recursive function called binary_search to search for a doctor in the sorted list by their ID.
Read Data: The program reads doctors' information from an input file (doctors.txt) and creates a list of Doctor objects from the data in the file.
User Interaction: The program interacts with the user by asking for input and displaying the search results or the sorted list of doctors.
Getting Started
## Prerequisites
Python 3.x
## How to Use
Clone the repository or download the doctor.py file.

Prepare the input data file doctors.txt in the following format:
doctorId;doctorName;specialty;hospital
123;Dr. Smith;Cardiologist;City Hospital
456;Dr. Johnson;Neurologist;General Hospital
... (Add more doctors)

Run the Python script doctor.py.

Follow the on-screen instructions to perform various operations:

Sort doctors by hospital and specialty.
Search for a doctor by their ID.

## License
This project is licensed under the MIT License.
