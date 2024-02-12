print('WELCOME TO FOOTBAAL QUIZ')
player=input('do you want to play?')

if player.lower() != "yes":
    quit()
print('Ok Lets Play')

score=0

question = input('How Many Ballon Dor did Messi won:')
if question.lower()== "eight":
    print('Excellent its a correct answer')
    score +=1
else:
    print('Its a wrong answer')
question = input('Who is the Argentina team Football captain:')
if question.lower() == "messi":
    print('Great its a correct answer')
    score +=1
else:
    print('Its a wrong answer')
question = input('How Many Ballon Dor did Ronaldo won:')
if question == "five":
    print('Excellent its a correct answer')
    score +=1
else:
    print('Its a wrong answer')
question = input('Which football club did Lionel messi join in 2021:')
if question.lower() == "paris saint-germain":
    print('Great its a correct answer')
    score +=1
else:
    print('Its a wrong answer')
question = input('who Won the World cup in 2022 :')
if question.lower() == "argentina":
    print('Great its a correct answer')
    score +=1
else:
    print('Its a wrong answer')
question = input('How many people watched the 2022 Football Worldcup Final:')
if question.lower() == "1.12 billion":
    print('Great its a correct answer')
    score +=1
else:
    print('Its a wrong answer')

print("Your score:"+str(score))