import time
import random

file_path = "data/log.txt"

start_time = time.time()  
while time.time() - start_time <10:
    random_number = random.randint(1, 1000)  
    

    with open(file_path, "a") as file:
        file.write(f"This is Eman_{random_number}.\n")
        print(f"Log entry added to {file_path} with random number: {random_number}")

    with open(file_path, "r") as file:
        print("Current file contents:")
        print(file.read())
    time.sleep(1)

print("Script finished after 10 seconds.")
