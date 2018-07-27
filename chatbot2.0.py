# greet user
def intro():
    print("Hi, I'm Chatbot!")
# start conversation
def process_input(answer):
    if answer == ("hi" or "hello" or "hey"):
        print("Hello! What do you want to major in when you grow up?")
    else:
        answer = input(" (What do you want to major in when you grow up?) ")
# make differing responses based on career choices
    if answer == ("engineering" or "medicine" or "computer science"):
                print("Nice!")
    else:
                print("Yikes!")
# make answers lower case
answer = answer.lower()
