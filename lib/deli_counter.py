KATZ_DELI = []
OTHER_DELI = ["Logan", "Avi", "Spencer"]
ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]

def line(que):
    message=""
    if (que == []):
        message="The line is currently empty."
    else:
        index=1
        message="The line is currently: "
        for customer in que:
            message=message + f"{index}. {customer} " 
            index+=1 
           
    print(message.strip())        

def take_a_number(que, name):
    position=len(que) + 1
    que.append(name)
    print (f"Welcome, {name}. You are number {position} in line.")

def now_serving(que):
    if (len(que) == 0):
        print ("There is nobody waiting to be served!")
    else:
        customer=que.pop(0) 
        print(f"Currently serving {customer}.") 
        
    
print (line(OTHER_DELI))   