import time

player_info = {}

def start_game():
  print("Welcome Hacker, this is going to be a wonderful journey into the world of hackathons!")
time.sleep(2.5)

print("This is an adventure filled with friends and adventure!")
time.sleep(2.5)

print("Before we begin, tell me a little about yourself.")
  
player_info["gender"] = input("What is your gender?")
print("...")
print("\n...okay, next up...\n")
player_info["name"] = input("What would you like to be called?")


if __name__ == "__main__": 
  
    #print("Hello World")

  start_game()
  time.sleep(10)
