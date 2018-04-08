import sys
import os
import re
from os.path import basename,abspath,join
    
pattern = "(\[[0-9]{1,3}\])"

def load_choices(choices_folder):
    choices = {}
    for bname in os.listdir(choices_folder):
        name = bname.rstrip(".md")
        apath = abspath(choices_folder) + "/" + bname
        choices[name] = apath
    
    return choices

def load_answers(answers_path):
    answers = {}
    with open(answers_path,"r") as f:
        for line in f:
            if len(line.strip()) == 0: continue
            if line.startswith("#"): continue
            if line.startswith("["): continue

            subject = "n/a"
            short_txt = "n/a"
            long_txt = "n/a"
            score = 100

            # try to subject,short_txt,long_txt
            try:
                subject = line.split(":",1)[0].strip()
                short_txt = line.split(":",1)[1].split(".",1)[0].strip()
                long_txt = line.split(".",1)[1].strip() 
            except IndexError as err:
                print("Couldn't parse subject,short and long txt, line:",line,"error:",err)

            # try to parse score
            try:
                score = re.findall(pattern,short_txt)[-1]
                short_txt = short_txt.replace(score,"")
                score = score.replace("[","").replace("]","")
                score = int(score)
            except IndexError as err:
                print("Couldn't parse score, short_txt:",short_txt,"error:",err)

            answers[subject] = {"long":long_txt,"short":short_txt,"score":score}

    return answers

def load_requirements(requirements_path):
    requirements = []
    with open(requirements_path) as f:
        for line in f:
            if len(line.strip()) == 0: continue
            score_boxes = ""
            score = 100
            try:
                score_boxed = re.findall(pattern,line)[-1] 
                score = score_boxed.replace("[","").replace("]","")
                score = int(score)
            except IndexError as err:
                print("Couldn't parse score, line",line,"error:",err)

            requirement = line.replace(score_boxed,"").strip()
            requirements.append((requirement,score))
            
    return requirements

# Calculate satisfaction for choice (0-100)
def calc_outcome(requirements,choice_path):
    total = 0
    answers = load_answers(choice_path)
    for requirement_info in requirements:
        requirement = requirement_info[0]
        weight = requirement_info[1]
        score = answers[requirement]["score"]
        plus = weight * score
        # debug:#  print(weight,"*",score,"=",plus)
        total += plus

    # debug: # print("total:",total)
    percent = float(total)/100
    return percent


def main(folder):
    requirements = load_requirements(folder + "/requirements.txt")
    choices = load_choices(folder + "/choices")
    for choice,choice_path in choices.items():
        answers = load_answers(choice_path)
        outcome = calc_outcome(requirements,choice_path)
        print("name: %s" % choice)
        print("=========================================")
        for requirement_info in requirements:
            requirement = requirement_info[0]
            short_txt = answers[requirement]["short"]
            score = answers[requirement]["score"]
            print("%s: %s (%d)" % (requirement,short_txt,score))
        print("=========================================")
        print("outcome: %.2f" % outcome)
        print("")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("usage: decis.py [folder]")
