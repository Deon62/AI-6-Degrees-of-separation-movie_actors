Six Degrees of Separation - Movie Actor Connection
This project is an AI-based implementation of the "Six Degrees of Separation" concept for connecting movie actors. The algorithm identifies a path between two actors, showing how they are connected within six degrees or fewer through the movies they have appeared in together.

Project Overview
The Six Degrees of Separation is a theory that anyone on Earth can be connected to any other person through a chain of acquaintances with a maximum of six steps. This project adapts that concept to connect movie actors, using an algorithm that finds the shortest connection path between two actors based on the movies they've both featured in.

Features
Input two actor names, and the algorithm finds the shortest connection path between them.
Uses an efficient search algorithm to minimize the degrees of separation.
Based on real-world data of movies and cast members.
Files
degrees.py: Main script that implements the algorithm for finding connections between actors.
movies.csv: Contains data on movies, including IDs, titles, and years.
people.csv: Contains data on actors, including IDs, names, and birth years.
stars.csv: Links actors with the movies they've starred in, using actor and movie IDs.
util.py: Contains utility functions to support data processing and searching.
Requirements
Python 3.x
Any necessary libraries listed in requirements.txt (if applicable)
Usage
Clone the repository and navigate to the project directory:

bash
Copy code
git clone https://github.com/Deon62/AI-6-Degrees-of-separation-movie_actors.git
cd AI-6-Degrees-of-separation-movie_actors
Run the main script to find the connection between two actors:

bash
Copy code
python degrees.py
Follow the on-screen prompts to enter the names of two actors. The program will display the shortest connection path, showing each movie and co-actor link along the way.

Example
Suppose you want to find the connection between Leonardo DiCaprio and Kevin Bacon. The algorithm will output a list of movies and actors that connect them, showing each degree of separation.

Data Sources
movies.csv: List of movies with unique IDs, titles, and release years.
people.csv: List of actors with unique IDs, names, and birth years.
stars.csv: Relationship data between actors and movies by ID.
Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License.

Feel free to adjust the sections or add more details as needed!






