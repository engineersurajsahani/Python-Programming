# Decorators

def print2Table(func):
    def table():
        print("Table of 2 :- ")
        for i in range(1,11):
            print("2 * ",i," = ",2*i)
    return table

@print2Table       
def message():
    print("Messgae Function :- ")
    
message()
