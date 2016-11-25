# Our quiz!

score = 0

def quiz():

    global score

    question1()
    question2()
    question3()
    question4()
    question5()
    

    print("This quiz is about ThE iNtERnET")
    


def question1():
    global score
        
    print("Question 1:")
    print("What is the most richest website in the world?")
    print("a. Wikipedia")
    print("b. Youtube")
    print("c. Amazon")
    print("d. Google")
    answer = input("Pick your answer: ")
    
    if answer == "Amazon":
        score = score + 10
    print(score)
    

def question2():
    global score

    print("Question 2:")
    print("How many Google searches are made per second?")
    print("a. 5 million")
    print("b. 60,000")
    print("c. 1.2 million")
    print("d. 40,000")
    answer = input("Pick your answer: ")
    
    if answer == "40,000":
        score = score + 10
    print(score)
    

def question3():
    global score

    print("Question 3:")
    print("What is the most popular meme?")
    print("a. doge")
    print("b. pepe the frog")
    print("c. grumpy cat")
    print("d. nyan cat")
    answer = input("Pick your answer: ")

    if answer == "doge":
        score = score + 10
    print(score)
    

def question4():
    global score

    print("Question 4:")
    print("When was ThE iNteRNet created?")
    print("a. January 1st 1983")
    print("b. August 1st 2003")
    print("c. February 30th 1962")
    print("d. December 19th 3729")
    answer = input("Pick your answer: ")

    if answer == "January 1st 1983":
        score = score + 10


def question5():
    global score
    
    print("Question 5: ")
    print("Who created the internet?")
    print("a. Fred")
    print("b. Robert E. Kahn")
    print("c. Vint Cerf")
    print("d. doge")
    answer = input("Pick your answer: ")

    if answer == "Robert E. Kahn":
        score = score + 10
    print(score)


def question6():
    global score

    print("Question 6:")
    
    
    
    
    
    





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
