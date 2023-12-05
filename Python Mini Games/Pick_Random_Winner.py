import random
import time

def pick_winner(participants):
    winner = random.choice(participants)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return winner, timestamp

def countdown():
    print("Get ready for the winner announcement...")
    time.sleep(3)
    print("     3  ")
    time.sleep(1)
    print("    2  ")
    time.sleep(1)
    print("  Thanks again for donating to my fundarising The Hospice of the Good Sheperd!!!")
    time.sleep(3)
    print("   1  ")
    time.sleep(1)
    print("  Go! ")
    time.sleep(1)
    print("-------")

participants = ["Thomas Hughes", "Jason Duncan", "Jason Duncan", "Adam Kirkpatrick", "Adam Kirkpatrick", "Kris Howard",
                "Rebecca Dean", "Murray King", "Paca Garnica", "Tere Orduna", "Tere Orduna", "Elena Martin", "Jose Ibanez",
                "Jose Ibanez", "Jose Ibanez", "Jose Ibanez", "Jonathan Hodgins", "Jonathan Hodgins", "Jonathan Hodgins", 
                "Daniel Leach", "Alex Taylor", "Susana Cortes Chain", "Susana Cortes Chain", "Peter Davies", "Peter Davies"]

countdown()
winner, timestamp = pick_winner(participants)

print("And the winner is...")
time.sleep(2)
print("Drumroll, please...")
time.sleep(2)
print("*")
time.sleep(1)
print("*")
time.sleep(1)
print("*")
print("******************************")
print("*                            *")
print(f"*      {winner}         *")
print("*                            *")
print("******************************")
print("Congratulations!")
print("Timestamp:", timestamp)

# Calculate the probability for names starting with user input
total_participants = len(participants)
# user_name = input("Enter your name: ")
name_count = sum(1 for name in participants if name.startswith(winner))
probability_name = name_count / total_participants

print(f"Win Probability for '{winner}':", probability_name)