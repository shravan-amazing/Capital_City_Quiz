import requests
import random


try:
    response = requests.get(
        "https://restcountries.com/v3.1/all?fields=name,capital", timeout=10)
    data = response.json()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()


countries = {}
for country in data:
    if isinstance(country, dict):
        name_data = country.get("name")
        capitals = country.get("capital")
        if isinstance(name_data, dict) and capitals:
            common_name = name_data.get("common")
            countries[common_name] = capitals[0].lower()


quiz_questions = random.sample(list(countries.items()), 5)
score = 0
print("Welcome to the multiple-choice quiz!")

user_name = input("Enter your name: ")
print("Let's start!\n")

for country, correct_capital in quiz_questions:

    wrong_answers = random.sample(
        [cap for ctry, cap in countries.items() if cap != correct_capital], 3
    )

    options = wrong_answers + [correct_capital]
    random.shuffle(options)

    print(f"What is the capital of {country}?")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option.capitalize()}")

    while True:
        try:
            answer = int(input("Your choice (1-4): "))
            if 1 <= answer <= 4:
                break
            else:
                print("Enter a number between 1 and 4.")
        except ValueError:
            print("Enter a valid number.")

    if options[answer - 1] == correct_capital:
        print("Correct!\n")
        score += 1
    else:
        print(
            f"Wrong! The correct answer is {correct_capital.capitalize()}.\n")

print(
    f"Quiz over! {user_name}, your score is {score} out of {len(quiz_questions)}")
