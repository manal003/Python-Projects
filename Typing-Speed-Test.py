from time import *
import random as r

def mistakes(given_para, user_typed):
    error = 0
    count = 0
    for i in range(len(given_para)): 
        count +=1       
        try:           
            if  given_para[i] != user_typed :
                error+=1
                
        except:
            error+=1   # Out of index range so that program does not stop 
    print("Total Words : ",count)
    print("Errors ; ",error)       

def speedTest(time_1, time_2, user_typed):
    total_time = round(time_2 - time_1)
    speed = round(len(user_typed)/total_time)

    return speed


text = ["The quick brown fox jumps over the lazy dog.","Typing is a skill that improves with consistent practice.", "A journey of a thousand miles begins with a single step.", "Success is not final, failure is not fatal: it is the courage to continue that counts.", "Practice typing every day to boost your speed and accuracy."]

ran_text = r.choice(text)
print(ran_text)
print("Total No. of text : ",len(ran_text))
print()
print()

time_s = time()
user_text = input("Enter your text : ")
time_e = time()
print("Speed : ", speedTest(time_s,time_e,user_text),"w/sec")
mistakes(ran_text, user_text)      
# print("Mistakes : ",mistakes(ran_text, user_text))

