import re
import random
import json
import time


with open("bot.json") as json_data:
    responses_data = json.load(json_data)
    


def getAnswer(user_input):
    words = re.split(r'\s+|[,;?!.-]\s*', user_input)
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response,required_words):
        nonlocal highest_prob_list
        message_certainty = 0
        has_required_words = True

        for word in words:
            if word in list_of_words:
                message_certainty +=1

        for word in required_words:
            if word not in user_input:
                has_required_words = False
                break

        percentage = float(message_certainty)/ float(len(list_of_words)) #1/2

        if has_required_words or single_response==1:
             highest_prob_list[bot_response] = int(percentage*100)
        else:
            highest_prob_list[bot_response] = 0
    


    


    for r in responses_data:
        response(r["bot_response"][random.randrange(3)], r["list_of_words"], r["single_response"], r["required_words"])



 
    best_response = max(highest_prob_list, key=highest_prob_list.get)

    if highest_prob_list[best_response] > 0 :
        return best_response
    else:
        wrost_response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][random.randrange(4)]
        return wrost_response

        

with open("img.txt","r") as img:
    print(img.read())

while True:
    user_input = input("YOU==> ")
    print("-------------------------------------------")
    Potrobot_output = getAnswer(user_input.lower())
    print("POTROBOT==> ",sep=' ', end='', flush=True)
    for i in range(0,len(Potrobot_output)):
        print(Potrobot_output[i],sep=' ', end='', flush=True)
        time.sleep(0.1);
        if(i==len(Potrobot_output)-1): print("");
    print("-------------------------------------------")

    