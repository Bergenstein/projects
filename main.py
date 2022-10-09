from question_model import Question
from data import question_data
from quiz_class import Quiz
from art import logo

print(logo)


def generate_question_objects():
  question_arr = []
  for i in range(len(question_data)):
    question = question_data[i]['question']
    answer = question_data[i]['correct_answer']
    difficulty = question_data[i]['difficulty']
    question = Question(question, answer, difficulty)
    question_arr.append(question)
  return question_arr


question_arr = generate_question_objects()

new_quiz = Quiz(question_arr)

while (new_quiz.still_questions_left()):
  new_quiz.next_question()

if (new_quiz.question_number == len(new_quiz.quiz_arr)):
  print(f"quiz is finished and your final score is {new_quiz.score}")
