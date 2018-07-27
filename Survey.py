#survey_answers {    (write out at least 3 questions)
# 'artist' : 'rihanna',
# 'city' : 'new york',
# 'person' : 'barack'
#}



answers = {}
list_of_answers = []
#user = []

survey = [
    "What's your name?",
    "How old are you?",
    "What's your favorite city?"
]

survey_k = [
    #keys
    'name',
    'age',
    'city'
]
#while we want to keep taking surveys:
#while user == "yes":
for x in range(len(survey)) :
        answer = input(survey[x])
        answers[survey_k[x]] = answer
list_of_answers.append(answers)

#print the list of dictionaries
#print(list_of_answers)

#answer = "riri"
#answers['artist'] = 'riri'
answer = "Serene"
answers['name'] = answer

answer = "16"
answers['age'] = answer

answer = "Dubai"
answers['city'] = answer


print (answers)
