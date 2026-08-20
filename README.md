**Chef-It**
A desktop application designed to help users discover new recipes and restaurants based on their personal preferences, built using Python, Kivy, and MySQL.

**Overview**
Choosing what to cook or where to eat can often become repetitive, especially when users have specific preferences. Chef-It addresses this by allowing users to filter recipes and restaurants according to the factors that matter most to them and receive relevant results from a locally stored database.

The application is divided into two main discovery modes:
**Recipe Discovery:** Search through a database containing 180+ dishes using filters like cuisine, difficulty level, and nutritional value to view required ingredients and step-by-step instructions.
**Restaurant Discovery:** Filter through 180+ restaurants by cuisine, price range, ambience, ratings, delivery availability, and location.

**Key Features**
**Dynamic Search System:** Automatically falls back to a flexible SQL LIKE-based search if no exact filter matches are found, ensuring you are never left with an empty result screen.
**Flexible Query Construction:** Unset filters are automatically excluded from the WHERE clause, allowing you to search using any combination of preferences.
**Complete Stack Integration:** Combines a Kivy graphical user interface, a Python backend logic layer, and a MySQL relational database.
