**CHEF-IT**<br>
A desktop application that is designed to help users discover various new recipes and restaurants based on their personal preferences, built using Python, Kivy, and MySQL.<br>
<br>
**OVERVIEW**<br>
Choosing what to cook or where to eat often becomes quite repetitive, especially for users with specific dietary, cost or cuisine preferences. Chef-It solves this with a multi-criteria filtering system. Users set the parameters that matter most to them, and the application queries a locally stored database to return only the recipes and restaurants that match.<br>
<br>
The application is divided into two main discovery modes:<br>

**1. Recipe Discovery:** Search through a database containing 200+ dishes using filters like cuisine, difficulty level, and nutritional value to view required ingredients and step-by-step instructions.<br>
**2. Restaurant Discovery:** Filter through 180+ restaurants by cuisine, price range, ambience, ratings, delivery availability, and location.<br>
<br>
**KEY FEATURES**<br>

**1. Dynamic Search System:** Automatically falls back to a flexible SQL LIKE-based search if no exact filter matches are found, ensuring you are never left with an empty result screen.<br>
**2. Flexible Query Construction:** Unset filters are automatically excluded from the WHERE clause, allowing you to search using any combination of preferences.<br>
**3. Complete Stack Integration:** Combines a Kivy graphical user interface, a Python backend logic layer and a MySQL relational database.<br>
<br>
**TECH STACK**<br>
**Python:** Core application logic, database integration, SQL query construction and component communication.<br>
**Kivy:** Desktop interface design, screen and view management, user input handling and dynamic result rendering.<br>
**MySQL:** Storage and management of restaurant and recipe datasets.<br>
<br>
**Authors**<br>

Developed as a team project by:<br>
**Aryaman Banerjee** – Focused on Python backend, database design, record entry, Kivy frontend views and search query fallback logic.<br>
**Vir Chanda** – Focused on designing application structure, user experience workflows, component integration, testing and debugging.
