
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

# we need to think about how we can represent questions on the test
# there are two parts: the question prompts and the answers
# we will build a class to handle this and import it

from Question import Question

# now we need to create our objects
# we can even add questions into here and it will know how to ask and grade it
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

# now we need to write a function to run the test and check answer
# we also want it to grade the test, so we need to create a score
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)
