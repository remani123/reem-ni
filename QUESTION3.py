import json

test = {"one": [{"q1": "what is your name name ? ", "res1": "name"}],
        "tow": [{"q2": "what is 4+7 ?", "res2": "11"}],
        "three": [{"q3": "what is 18+16 ?", "res3": "34"}],
        "four": [{"q4": "what is 1+9 ? ", "res4": "10"}],
        "five": [{"q5": "what is 14+6 ? ", "res5": "20"}],
        "six": [{"q6": "what is 4+6 ? ", "res6": "10"}],
        "seven": [{"q7": "what is 25+15 ? ", "res7": "40"}],
        "eight": [{"q8": "what is 25+15 ? ", "res8": "50"}],
        "nine": [{"q9": "what is 30+40 ? ", "res9": "70"}],
        "ten": [{"q10": "what is 15+15 ? ", "res10": "30"}]
        }
# putting the questions in json data file

with open('qr.json', "w") as write_file:
    json.dump(test, write_file)

with open("qr.json", "r") as data_file:
    test = json.load(data_file)
n = 0
d = {}
for i in range(9):
    q11 = input(print(test["one"][0]["q1"]))
    if q11 == test["one"][0]["res1"]:
        n = n + 1
    q22 = input(test["tow"][0]["q2"])
    if q22 == test["tow"][0]["res2"]:
        n = n + 1
    q33 = input(test["three"][0]["q3"])
    if q33 == test["three"][0]["res3"]:
        n = n + 1
    q44 = input(test["four"][0]["q4"])
    if q44 == test["four"][0]["res4"]:
        n = n + 1
    q55 = input(test["five"][0]["q5"])
    if q55 == test["five"][0]["res5"]:
        n = n + 1
    q66 = input(test["six"][0]["q6"])
    if q66 == test["six"][0]["res6"]:
        n = n + 1
    q77 = input(test["seven"][0]["q7"])
    if q77 == test["seven"][0]["res7"]:
        n = n + 1
    q88 = input(test["eight"][0]["q8"])
    if q88 == test["eight"][0]["res8"]:
        n = n + 1
    q99 = input(test["nine"][0]["q9"])
    if q99 == test["nine"][0]["res9"]:
        n = n + 1
    q1010 = input(test["ten"][0]["q10"])
    if q1010 == test["ten"][0]["res10"]:
        n = n + 1
    break
print("Your Degree Is : ", n, "/10")

students_responses ={ "response": [q11, q22, q33, q44, q55, q66, q77, q88, q99, q1010, n] }
with open('students.json', "w") as write_file:
    json.dump(students_responses, write_file)

print(students_responses)
