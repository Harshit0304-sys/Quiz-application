questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ",
                       "In what year did the Great October Socialist Revolution take place? ",
                       "What is the largest lake in the world? ",
                       "Which planet in the solar system is known as the Red Planet? ",
                       "Who wrote the novel War and Peace? ",
                       "What is the capital of Japan?",
                       "Which river is the longest in the world? ",
                       "What gas is used to extinguish fires? ",
                       "What animal is the national symbol of Australia?",
                       "Which of the following planets is not a gas giant?",
                       "What is the name of the process by which plants convert sunlight into energy?")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
                   ("A. 1917", "B. 1923", "C. 1914", "D. 1920"),
                   ("A. Caspian Sea", "B. Baikal", "C. Lake Superior", "D. Ontario"),
                   ("A. Venus", "B. Earth", "C. Mars", "D. Jupiter"),
                   ("A. Anton Chekhov", "B. Fyodor Dostoevsky", "C. Leo Tolstoy", "D. Ivan Turgenev"),
                   ("A. Beijing", "B. Tokyo", "C. Seoul", "D. Bangkok"),
                   ("A. Amazon", "B. Mississippi", "C. Nile", "D. Yangtze"),
                   ("A. Oxygen", "B. Nitrogen", "C. Carbon dioxide", "D. Hydrogen"),
                   ("A. Kangaroo", "B. Koala", "C. Emu", "D. Crocodile"),
                   ("A. Mars", "B. Jupiter", "C. Saturn", "D. Uranus"),
                   ("A. Respiration", "B. Photosynthesis", "C. Oxidation", "D. Evolution"))

answers = ("C", "D", "A", "A", "B","A","B","C","C","B","C","B","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")