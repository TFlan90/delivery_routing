# Parcel Delivery Service

This project is a simulation of a package delivery system for a local parcel service. It uses a greedy algorithm based on the nearest neighbor approach to efficiently route three trucks to deliver 40 packages. 
The application provides a command-line interface to view the status of all packages at any given time throughout the day.

## Features

* **Data Loading:** Loads package information and a distance matrix from CSV files.
* **Custom Hash Table:** Utilizes a custom-built hash table for efficient O(1) average time complexity for package lookups, insertions, and removals.
* **Nearest Neighbor Algorithm:** Implements a greedy algorithm to determine the optimal delivery route for each truck, minimizing the total mileage.
* **Constraint Handling:** Manages various delivery constraints, including:
    * Packages that must be delivered together.
    * Packages restricted to a specific truck.
    * Packages that are delayed and arrive at the hub at a later time.
    * Address corrections that occur mid-day.
* **Time Simulation:** Simulates the passage of time as trucks travel their routes, updating package statuses from "At the hub" to "In transit" to "Delivered".
* **Status Reporting:** Allows the user to input a specific time to see the status of all 40 packages at that moment.

## How It Works

1.  **Data Initialization:** The application starts by loading package data from `Package File.csv` and distance data from `Distance Table.csv`. Packages are stored in a custom hash table (`HashTable`) using their package ID as the key.
2.  **Truck Loading:**
    * Three truck objects are created.
    * Packages are strategically loaded onto the trucks based on their delivery constraints (notes, delays, etc.).
    * The loading logic prioritizes packages with special requirements for specific trucks.
3.  **Delivery Simulation:**
    * The delivery process begins, starting with Truck 1 at 8:00 AM.
    * The core of the simulation is the `start_delivery_route` function, which uses a **nearest neighbor algorithm**. For each truck, it repeatedly selects the closest undelivered package from its current location.
    * Time is calculated based on the truck's speed of 18 mph. As the truck travels, its internal clock and total mileage are updated.
    * When a package is delivered, its status and delivery time are updated.
    * The simulation handles real-world events, such as a driver returning to the hub to pick up a delayed package or an address being corrected at 10:20 AM.
4.  **Reporting:**
    * After the simulation runs, the total mileage for all trucks is displayed.
    * The user is prompted to enter a time.
    * The `report_status` function then iterates through all packages in the manifest and displays their status (Delivered, In Transit, or At Hub) precisely at the user-specified time by comparing the query time with each package's loading and delivery times.

## File Structure

* `main.py`: The main entry point for the application. It initializes data, runs the delivery simulation, and handles user input for reporting.
* `hash_table.py`: Defines the `HashTable` class, a custom data structure for storing and managing package data.
* `package.py`: Defines the `Package` class, which models a single package and its attributes.
* `truck.py`: Defines the `Truck` class, which models a delivery truck, its contents, and its current state (location, time, mileage).
* `data_loader.py`: Contains functions for parsing CSV files and the logic for loading packages onto the trucks.
* `delivery_route.py`: Contains the core delivery simulation logic, including the nearest neighbor algorithm.
* `reporting.py`: Contains the function to generate and display the status of all packages for a user-specified time.

## How to Run

1.  Ensure you have Python 3 installed.
2.  Place the `data` folder containing `Package File.csv` and `Distance Table.csv` in the same directory as the Python scripts.
3.  Run the main program from your terminal:
    ```bash
    python main.py
    ```
4.  The program will first ask you to input a time to generate a report. Enter the hour and then the minute (using a 24-hour clock format).
5.  First, the program will print a log of all deliveries as they occur during the simulation.
6.  Finally, it will display a snapshot of the status of all 40 packages at the time you specified.