# day17: quiz_brain.py
# show question
# check answer
# increment count
class QuizBrain:

    def __init__(self, questions) -> None:
        self.question_number = 0
        self.score = 0
        self.questions = questions
        self.running = True

    def _check_answer(self, guess, answer):
        if (guess == "t" or guess == "True") and answer == "True":
            return True
        elif (guess == "f" or guess == "False") and answer == "False":
            return True
        else:
            return False

    def _get_score(self):
        return str(self.score) + "/" + str(len(self.questions))

    def run(self):
        while self.question_number < len(self.questions) and self.running:
            q = self.questions[self.question_number]
            self.question_number += 1
            answer = input(
                f"\nQuestion {self.question_number}. {q.question} (True/False): ")

            if answer == 'q':
                self.running = False
                print("You exited the quiz.")
            elif self._check_answer(answer, q.answer):
                self.score += 1
                print(
                    f"CORRECT.  Your score is {self._get_score()}.")
            else:
                print(
                    f"Incorrect answer.  Your score is {self._get_score()}.")
