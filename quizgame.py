# import the required modules
import time


# greetings
print("Welcome to quize game")
print("This is computer and coding related quize game")


# writing the game logic
score = 0
print("What is cpu stands for? ")
print("A.Central processing unit")
time.sleep(1)
print("B.Central processing utilisation")
time.sleep(1)
print("C.None of these")
time.sleep(1)

cpu = input("Choose (A, B, C): ")
if cpu == "A" or "a":
    print("Yes, a, central processing unit is the correct answer")
    print("Your answer is correct")
    score += 1

else:
    print("No, a, central processing unit is the correct answer")
    print("Your answer is incorrect")
    score -= 1

print("Next question")

print("What is gpc stands for? ")
print("A.Gaming processing c")
time.sleep(1)
print("B.Gaming PC")
time.sleep(1)
print("C.None of these")
time.sleep(1)

gpc = input("Choose (A, B, C): ")
if gpc == "B":
    print("Yes, b, gaming pc is the correct answer")
    print("Your answer is correct")
    score += 1

else:
    print("No, b, gaming pc is the correct answer")
    print("Your answer is incorrect")
    score -= 1

print("Next question")

print("What is py stands for? ")
print("A.Personal year")
time.sleep(1)
print("B.Perspective year")
time.sleep(1)
print("C.Python")

py = input("Choose (A, B, C): ")
if py == "python":
    print("Yes, c, python is the correct answer")
    print("Your answer is correct")
    score += 1

else:
    print("No, c, python is the correct answer")
    print("Your answer is incorrect")
    score -= 1

print("Next question")

print("What is js stands for? ")
print("A.javasslang")
time.sleep(1)
print("B.javaslang")
time.sleep(1)
print("C.None of these")

js = input("Choise (A, B, C): ")
if js == "C":
    print("Yes, c, None of these is the correct answer")
    print("Your answer is correct")
    score += 1

else:
    print("No, c, None of these is the correct answer")
    print("Your answer is incorrect")
    score -= 1

print("Next question")

print("What is php stands for? ")
php = input("Answer: ")
if php == "personal home page":
    print("Yes, personal home page is the correct answer")
    print("Your answer is correct")
# end of the quizegame
