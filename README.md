**CHEF-IT**

Chef-It

Chef-It is a desktop application designed to help users discover new recipes and restaurants based on their personal preferences. Built using Python, Kivy, and MySQL, the project combines a graphical user interface, backend application logic, and a relational database into a complete end to end food discovery application.

Overview

Choosing what to cook or where to eat can often become repetitive, especially when users have specific preferences. Chef-It addresses this by allowing users to filter recipes and restaurants according to the factors that matter most to them and receive relevant results from a locally stored database.

The application is divided into two main discovery modes: Recipe Discovery and Restaurant Discovery.

Recipe Discovery

The recipe discovery system allows users to search through a database containing 180+ dishes using filters such as cuisine, difficulty level, and nutritional value.

Once a suitable recipe is found, Chef-It displays the relevant information, including the ingredients required and detailed step by step cooking instructions. This allows users to quickly discover recipes that match their preferences and have all the information needed to prepare them.

Restaurant Discovery

The restaurant discovery system provides a similar experience for finding places to eat. Users can search through a database containing 180+ restaurants and filter results according to cuisine, price range, and ambience.

Each result provides key information such as the restaurant's specialty cuisine, price range, rating, delivery availability, and location, allowing users to compare options based on their preferences.

Search System

Chef-It uses a dynamic search system to make the filtering process more flexible.

The application first attempts to find results that directly match the filters selected by the user. If no exact matches are found, Chef-It automatically falls back to a more flexible SQL LIKE based search, allowing similar results to be returned instead of leaving the user with an empty result.

The SQL queries are also generated dynamically. Filters that the user leaves unset are excluded from the WHERE clause, meaning users can search using any combination of available preferences without requiring every filter to be selected.

Application Structure

The frontend is built using Kivy, which handles the application's screens, navigation, input forms, popups, and dynamic result displays.

MySQL provides the database layer and stores the recipe and restaurant datasets. The application retrieves information dynamically based on the user's selected filters.

Python connects the different parts of the system together. It handles the database connection, query construction, search and fallback logic, application state, and communication between the frontend and supporting application files.

Tech Stack

Python
Used for the core application logic, database integration, SQL query construction, search functionality, and communication between application components.

Kivy
Used to design the desktop interface, manage screens and views, handle user input, and dynamically display search results.

MySQL
Used to store and manage the recipe and restaurant datasets and provide the application with dynamically queried results.

Our Roles

Chef-It was developed as a team project of two, with Aryaman Banerjee and Aditya Jain contributing different parts of the application to build the complete system.

Aryaman Banerjee

Focused primarily on the application's Python, database, and frontend integration. Responsibilities included developing the integrated database query logic, managing and entering database records, designing the Kivy frontend and views, and developing the Python code responsible for connecting the different supporting application files.

I also worked on the application's search and filtering behaviour, including dynamically constructing database queries based on the user's selected preferences and implementing the fallback search logic when exact matches were unavailable.

Aditya Jain

Focused on supporting the application's application structure, functionality, and overall user experience. Responsibilities included contributing to the organisation and implementation of application components, supporting the recipe and restaurant discovery workflows, and helping refine the interaction between user inputs, search results, and the application's different screens.

Aditya also contributed to testing and debugging the application, helping ensure that the different components worked together reliably and that the overall discovery experience remained clear and intuitive.

Running Locally

Install the required Python dependencies using:

python -m pip install "kivy[base]"
python -m pip install mysql-connector-python

The project uses Kivy for the desktop application interface and MySQL Connector/Python to connect the Python application to the MySQL database.

Once the required packages have been installed, run the application using:

python main.py
Database Setup

Chef-It uses MySQL to store its restaurant and recipe data.

The database setup and restaurant seed data are provided in:

database/chef_it_database.sql

The SQL script creates the ChefIt database, creates the Restaurant table, and populates it with the project's restaurant data.

Open the SQL file in MySQL Workbench or another MySQL client and execute the script before running the application.

The recipe database follows the corresponding schema expected by the application code.

Project Structure

A typical project structure is:

Chef-It/
│
├── main.py
├── requirements.txt
├── README.md
│
├── database/
│   └── chef_it_database.sql
│
└── ...
Project Background

Chef-It was an early hands on project focused on building a complete application from the ground up rather than following a tutorial. It provided practical experience working across the different layers of a software system, from designing a user interface and managing application state to constructing SQL queries and integrating a real relational database.

The project helped develop a stronger understanding of how frontend design, backend logic, database management, and application integration work together to create a functional software product.

It also represents an early step toward exploring software development and applied problem solving alongside an engineering degree.

Database Schema

The database setup scripts are provided in the database directory. The chef_it_database.sql file contains the SQL required to create the Chef-It database, create the Restaurant table, and populate it with the project's restaurant records.

Additional SQL schema and setup scripts for the recipe dataset can be added to the same directory as the database structure is finalised.
