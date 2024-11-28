print(" Keep asking for name until user type stop. Type 'stop' to terminate the program.")
names = []

while True:
    ui = input(" Enter name: ")
    if ui.lower().strip() == "stop":
        for name in names:
            print(f" {name}")
        break
    else:
        names.append(ui)