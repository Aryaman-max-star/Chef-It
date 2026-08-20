**CHEF-IT**

Chef-It is a desktop application designed to help users discover new recipes and restaurants based on their personal preferences. The application was built using Python, Kivy, and MySQL, combining a graphical user interface with a relational database to create a complete end to end food discovery experience.

Overview:
The idea behind Chef-It is simple: Chef-It allows users to filter recipes and restaurants based on the factors that matter most to them and then returns relevant results from a locally stored database. It is difficult to make decisions regarding dinning due to varies and a plethora of preferences and Chef-It helps simplify this process.
The application contains two main discovery modes: Recipe Discovery and Restaurant Discovery.

1. Recipe Discovery:
The recipe section allows users to search through a database of 180+ dishes, with more added every month, using filters such as cuisine, difficulty level, and nutritional value.
Once a suitable recipe is found, the application displays the relevant information, including the complete ingredient list and step by step cooking instructions allowing users to go from discovering a recipe to actually preparing it seamlessly.

2. Restaurant Discovery:
The restaurant section works in a similar way, allowing users to discover restaurants from a database of 200+ entries.
Users can filter restaurants based on cuisine, price range, and ambience. The results provide useful information such as the restaurant's specialty cuisine, rating, and location, helping users narrow down their options based on what they are looking for.

Search System:
One of the features of Chef-It is its fallback search system. The application first attempts to find an exact match based on the filters selected by the user.
If no exact results are found, Chef-It automatically performs a more flexible SQL LIKE based search. This means that the application can still return potentially relevant results instead of simply displaying an empty result when the user's preferences do not perfectly match the available data.
The SQL queries are also built dynamically. Filters that the user does not select are excluded from the WHERE clause, allowing the same search system to handle different combinations of preferences.

Application Structure:
The user interface is built entirely using Kivy. It manages the different screens within the application, including the introduction screen, mode selection, recipe discovery, and restaurant discovery.
Kivy popups are also used for the filter forms, allowing users to enter their preferences before performing a search.
MySQL acts as the application's database layer, storing the recipe and restaurant datasets and allowing the application to retrieve relevant records dynamically.
Python connects the different components together. It handles the database connection, constructs the SQL queries, manages the primary and fallback search logic, and dynamically creates the Kivy widgets used to display results.

Tech Stack:
Python
Core application logic, database queries, search functionality, and application flow.

Kivy
Desktop graphical user interface, screen management, popups, and dynamic result rendering.

MySQL
Storage and retrieval of the recipe and restaurant datasets.

My Role:
Chef-It was developed as part of a team of two, where I was responsible for the majority of the application's technical implementation. My work focused on the Python and database integration, including developing the database query logic, managing and entering database records, and connecting the application to MySQL.
I also designed and implemented the application frontend and views using Kivy, including the different screens, user input forms, and dynamic result displays. In addition, I developed the Python integration code for the supporting subpart files, ensuring that the different components of the application worked together correctly and communicated with the database as intended.


Running Locally:
To run Chef-It locally, first install the required Python dependencies:
python -m pip install "kivy[base]"
and 
import msql.connector
Next, set up a local MySQL database using the schema expected by main.py. The database contains a Restaurants table and a recipes table (code for all of the table attributes and values have been attached in another corresponding file within this repository). The expected column names can be found in the query result mapping code within main.py.

For security, the database password should be stored as an environment variable rather than directly inside the source code.

export DB_PASSWORD="your_password_here"

Once the database has been configured, start the application with:

python main.py
Project Background

Chef-It was one of my early hands on projects where I built an application from the ground up rather than following a tutorial. It gave me practical experience connecting a graphical interface, backend application logic, and a real relational database into one working system.

More importantly, it helped me understand how the different layers of a software application work together, from designing and querying a database to managing application state and dynamically generating the user interface.

The project is also part of what sparked my continued interest in software development and applied problem solving alongside my engineering degree.

