print("🙏 WELCOME TO KBC 🙏")
print("🏆 KAUN BANEGA CROREPATI 🎉🎊")
question=["🔷 Q1.How many continents 🌍 are there❓",              
    "🔷 Q2.What is the capital of India❓",            
    "🔷 Q3.NG mei kaun se course padhaya jaata hai🙄❓"    
]
options=[["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution=[3, 4, 1] 
answer=["3.Seven","4.Eight","3.Chennai","4.Delhi","1.Software Engineer","2.Counselling"]
i=0
amount=1000000
count=0
b=0
a=1
while i<len(question):
    print(question[i])
    j=0
    k=1
    while j<len(options[i]):
        print(options[i][j])
        j=j+1
    lifeline=input("DO YOU WANT LIFELINE😊")
    if lifeline=="YES":
        print("5️⃣ 0️⃣ 5️⃣ 0️⃣")
        if count==0:
            print(answer[b+i])
            print(answer[b+a])
            num=int(input("ENTER THE ANSWER"))
            if num==solution[i]:
                print("YOUR ANSWER IS RIGHT✅")
                print("YOU WON",amount,"$")
            else:
                print("YOUR ANSWER IS WRONG❌")
                print("YOU LOOSE THE GAME😞")
                break
            print()
            count=count+1
        else:
            print("YOU HAD ALREADY USED LIFELINE🥰")
            e=int(input("ENTER THE ANSWER"))
            if e==solution[i]:
                print("YOUR ANSWER IS RIGHT✅")
                print("YOU WON",amount,"$")
            else:
                print("YOUR ANSWER IS WRONG❌")
                print("YOU LOOSE THE GAME😞")
                break
            print()
    else:
        f=int(input("ENTER THE ANSWER"))
        if f==solution[i]:
            print("YOUR ANSWER IS RIGHT✅")
            print("YOU WON",amount,"$")
        else:
            print("YOUR ANSWER IS WRONG❌")
            print("YOU LOOSE THE GAME😞")  
            break
        print()
    amount=amount+1000000
    i=i+1
    a=a+1
    b=b+1   
print("YOU WON","😍 💐",amount," 🍫")
print("THANK YOU FOR PLAYING🍫 💐")