#opening a file
f = open("allanswers.json", "r")
olddata = json.load(f)
list_of_answers.extend(olddata)
f.close()

#reopen the file n write mode, so we can update it
f = open("allanswers.json", "w")
f.write("[\n")
index = 0
for t in list_of_answers
    if (index < len(list_of_answers) - 1):
        json.dump(t,f) #dumping all answers from survey T
                        #putting those answers in file f
        f.write(',\n')
    else:
        json.dump(t, f)
        f.write('\n')
    index += 1
f.write(']')
f.close()
