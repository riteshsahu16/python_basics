import random as random
#Select  any random no. in range(1,5) except any given n

QUESTIONS = [
        {
            "name": " India's largest city by population",
            "option1": "Delhi",
            "option2": "Mumbai",
            "option3": "Pune",
            "option4": "Bangalore",
            "answer": 2,
            "money": 1000
        },{
            "name": "India is a federal union comprising twenty-nine states and how many union territories?",
            "option1": "6",
            "option2": "7",
            "option3": "8",
            "option4": "9",
            "answer": 2,
            "money": 2000
        }]


n = QUESTIONS[0]['answer']

print("n : ", n, "x : ", x)

#make other 2 options null
#option index starts from : 1 to 4
#QUESTIONS[0][i]



for i in QUESTIONS[0].keys():
	print(i, " ", QUESTIONS[0][i])


