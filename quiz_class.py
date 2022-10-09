class Quiz:

  def __init__(self, _quiz_arr):
    self.quiz_arr = _quiz_arr
    self.question_number = 0
    self.score = 0

  def next_question(self):
    _question = self.quiz_arr[self.question_number].question
    _answer = self.quiz_arr[self.question_number].answer
    _difficulty = self.quiz_arr[self.question_number].difficulty
    self.question_number += 1
    user_input = input(f"{self.question_number}. {_question}?: ")
    user_is_correct = self.check_answer(user_input, _answer)
    correction_answer_options = ['true', 'false']
    if (user_input.lower() != correction_answer_options[0].lower()
        and user_input.lower() != correction_answer_options[1].lower()):
      self.question_number -= 1
      print("don't mock about. Pick 'true' or 'false'.")

    if (not user_is_correct):
      print("wrong")
    if (user_is_correct and _difficulty == "hard"):
      self.score += 3
      print(
        f"correct. You also get an extra 2 points for answering a {_difficulty} question"
      )
    if (user_is_correct and _difficulty == "medium"):
      self.score += 2
      print(
        f"correct. You also get an extra 1 points for answering a {_difficulty} question"
      )
    if (user_is_correct and _difficulty == "easy"):
      self.score += 1
      print(f"correct. You answered a {_difficulty} question")

  def check_answer(self, _answer, _user_input):
    return _answer.lower() == _user_input.lower()

  def still_questions_left(self):
    return self.question_number < len(self.quiz_arr)
