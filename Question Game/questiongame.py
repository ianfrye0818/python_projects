import requests
import random
import os

while True:
  amount = input("How many questions? (1...50) ")
  if amount.isdigit() and int(amount) > 1 and int(amount) < 50:
    amount = amount
    break
  else:
    print("That is not a valid input.. please try again..")
os.system('cls' if os.name == 'nt' else 'clear')

category = random.randint(9,32)

url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty=easy&type=boolean"

response = requests.get(url)
questions= response.json()

questionDict = {}
answerDict = {}
question_counter = 1
answer_counter = 1
user_answer = {}
user_score_dict = {}

for key in questions["results"]:
  questionDict[question_counter] = key["question"]
  answerDict[question_counter] = key["correct_answer"]
  question_counter += 1

for question_id, question in questionDict.items():
  user_input = input(f"Question number {question_id}: {question}  Answer:  ")
  if user_input == "true" or "t" or "T" or "True":
    user_input = "true"
  elif user_input == "false" or "f" or "f" or "False":
    user_input = "false"
  user_answer[question_id] = user_input
  if user_answer[question_id].lower() == answerDict[question_id].lower():
    user_score_dict[question_id] = "Correct"
  else:
    user_score_dict[question_id] = "Incorrect"
  print(user_score_dict[question_id])
