Country Capitals Quiz (Python)

A command-line multiple-choice quiz that tests the user’s knowledge of country capitals. The quiz fetches country data from a public API and generates random questions.

How to Run

Install Python 3 and the requests library:

pip install requests


Run the program:

python capitals_quiz.py

How It Works

Fetches country names and capitals from the REST Countries API.

Randomly selects 5 countries for the quiz.

Presents four answer options for each question (one correct, three random wrong answers).

Tracks and displays the user’s score at the end.

Learning Points

Working with APIs using Python’s requests module

Handling JSON data

Generating quizzes with randomization

Handling user input and validating responses
