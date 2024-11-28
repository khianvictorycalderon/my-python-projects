
print(" Enter 5 names, type stop to terminate names")

for x in range(0,5):
    ui = input(" Enter your name: ")
    if ui.lower().strip() == "stop":
        print(" Program terminated.")
        break
    else:
        print(f" Hello {ui}")