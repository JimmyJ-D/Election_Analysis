#What is the score?
score = int(input("What is your test score? "))

#Determine the grade. 
if score >= 90:
    #this the true statment
    print('Your grade is an A. ')
#if not true do this next
else:
    if score >=80:
        #this is the next true statment match
        print('Your grade is a B. ')
    #if not true do this next
    else:
        if score >= 70:
            #this is the next true statement match
            print('Your grade is a C. ')
        #if not trude do this next
        else:
            if score >= 60:
                #this is the next true statment match
                print('Your grade is a D. ')
            else:
                print('Your grade is an F. ')
    
    