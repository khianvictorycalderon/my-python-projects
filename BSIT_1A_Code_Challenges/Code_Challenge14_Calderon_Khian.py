sum = 0
while True:
    ui = int(input(" Enter a number --> "))
    sum += ui
    if ui == 0:
        print(" The loop has terminated")
        print(f" The sum of all the numbers given is {sum}")
        break