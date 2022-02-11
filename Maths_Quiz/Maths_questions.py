import random

def setup_check():
    file = open("highscores.csv", "a")
    file.close()
    
    file = open("highscores.csv", "r")
    file_contents = file.readlines()
    file.close()
    
    if len(file_contents) == 0:
        file = open("highscores.csv", "w")
        for i in range(10):
            file.write("AAA,0,\n")
        file.close()
        
def high_scores(score):
    file = open("highscores.csv", "r")
    high_scores = []
    new_high_scores = []
    for line in file:
        temp = line.split(",")
        high_scores.append(temp)
    file.close()
    
    i = 0
    on_leader = False
    while len(new_high_scores) < 10:
        if int(high_scores[i][1]) > score:
            new_high_scores.append(high_scores[i])
            i += 1
        elif int(high_scores[i][1]) < score and on_leader == False:
            print("High score!")
            on_leader = True
            while True:
                initial = input("Enter 3 letter initial: ")
                is_alpha = initial.isalpha()
                length = len(initial)
                initial = initial.upper()
                if is_alpha == False:
                    print("The initial did not consist of 3 letters.")
                elif length != 3:
                    print("You did not enter 3 letters")
                else:
                    break
            temp = [initial, str(score), "\n"]
            new_high_scores.append(temp)
        else:
            new_high_scores.append(high_scores[i])
            i += 1
    
    file = open("highscores.csv", "w")
    for i in range(len(new_high_scores)):
        file.write(new_high_scores[i][0] + "," + new_high_scores[i][1] + ",\n")
        print("{position}: {initial} {point_score}".format(
              position = (i + 1), initial = new_high_scores[i][0],
              point_score = new_high_scores[i][1]))
    file.close()
    
def num_generator(difficulty):
    nums = []
    for i in range(difficulty + 1):
        nums.append(random.randint((-10*difficulty), (10*difficulty)))
    return nums

def ops_generator(difficulty):
    ops_to_use = []
    for i in range(difficulty):
        num = random.randint(0, 3)
        ops_to_use.append(ops[num])
    return ops_to_use

def question_generator(difficulty, nums, ops_to_use):
    question = str(nums[0])
    for i in range(difficulty):
        question += " " + ops_to_use[i]
        question += " " + str(nums[i + 1])
    return question

setup_check()

ops = ["*", "/", "-", "+"]
score = 0

while True:
    wrong = 0
    
    print("""Pick a difficulty between 1 and 10.
All answers will be rounded to 3d.p.""")
    correct = False
    while correct == False:
        try:
            difficulty = int(input(">"))
            if difficulty >= 1 and difficulty <= 10:
                correct = True
            else:
                print("You did not enter a number between 1 and 10")
        except ValueError:
            print("You did not enter an integer number")
            
    points = 0       
    while points < 10:
        while True:
            nums = num_generator(difficulty)
            ops_to_use = ops_generator(difficulty)
            try:
                question = question_generator(difficulty, nums, ops_to_use)
                answer = float(eval(question))
                answer = round(answer, 3)
                break
            except ZeroDivisionError:
                print("Dividing by zero will cause a zero division error")
        print(question)
        
        while True:
            try:
                user_answer = float(input("Answer: "))
                break
            except ValueError:
                print("You did not enter a number.")
                
        if user_answer == answer:
            print("Correct!")
            points += 1
            print("Points: " + str(points))
        else:
            print("Wrong!")
            print("Points: {point_total}".format(point_total = points))
            wrong += 1
                  
    print("10 points! Yay :)")
    score += (difficulty*10) - (wrong)
                  
    print("Continue y/n?")
    user_opt = input(">")
    if user_opt.upper() == "N":
        break
    
print("Score: {point_score}".format(point_score = score))
print("""

""")

high_scores(score)

input()
