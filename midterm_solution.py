chore_names = ["Sweeping / Mopping", "Dishwashing", "Taking Out Trash",
               "Cleaning Bathroom", "Buying Groceries"]
chore_frequency = ["Daily", "After meals", "Every other day", "Weekly", "Weekly"]

print("=" * 50)
print("DORM ROOM -- CHORE LIST")
print("=" * 50)

# Room monitor name (non-empty, no digits, no spaces)
while True:
    room_monitor = input("Room monitor name: ").strip()
   
    if room_monitor == "":
        print("Cannot be empty.")
        continue
    if " " in room_monitor:
        print("No spaces allowed in name.")
        continue
    if any(ch.isdigit() for ch in room_monitor):
        print("Name cannot contain numbers.")
        continue
    break

# Room number (numbers, letters, and punctuation allowed)
while True:
    raw_room = input("Room number: ").strip()
    if raw_room == "":
        print("Room number cannot be empty. Please enter a room number.")
        continue
    if raw_room == "0":
        print("Room number cannot be 0. Please enter a valid room number.")
        continue
    room_number = raw_room.upper()
    break

# Display chore list
print("\n" + "=" * 50)
print("DORM ROOM -- CHORE LIST")
print("=" * 50)
for i in range(len(chore_names)):
    print(f"{i + 1}. {chore_names[i]:<25} [{chore_frequency[i]}]")
print("=" * 50)

# Assignment lists
assigned_chores = []
assigned_roommates = []
assigned_status = []

# Allowed status inputs
allowed_done = {"done", "d", "yes", "y"}
allowed_not_done = {"not done", "not_done", "notdone", "n", "no", "incomplete"}

# Accept chore assignments 4 times
for chore_slot in range(1, 5):
    print(f"\n--- CHORE {chore_slot} ---")

    # Chore number loop (0 to skip) - single digit only
    while True:
        raw = input(f"Chore number (0 to skip): ").strip()
        if raw == "":
            print(f"Input cannot be empty. Enter 0 to skip or a single digit between 1 and {len(chore_names)}.")
            continue
        # Check if input contains only digits
        if not raw.isdigit():
            print("Invalid input. Please enter only a single number (0 to skip or a chore number).")
            continue
        # Check if it's a single digit
        if len(raw) != 1:
            print(f"Chore number must be a single digit only. Enter 0 to skip or a digit between 1 and {len(chore_names)}.")
            continue
        try:
            num = int(raw)
        except ValueError:
            print("Invalid input. Please enter a single digit (0 to skip or a chore number).")
            continue
        if num == 0:
            chore_number = 0
            break
        if 1 <= num <= len(chore_names):
            chore_number = num
            break
        print(f"Invalid chore number. Enter 0 to skip or a digit between 1 and {len(chore_names)}.")

    if chore_number == 0:
        print(f"Chore number (0 to skip): 0")
        continue

    # Roommate name (letters only, no spaces, no numbers)
    while True:
        roommate_name = input("Roommate name: ").strip()
        if roommate_name == "":
            print("Roommate name cannot be empty. Please enter a name.")
            continue
        if " " in roommate_name:
            print("Roommate name cannot contain spaces. Please enter a name without spaces.")
            continue
        # Check if input contains only letters
        if not roommate_name.isalpha():
            print("Roommate name can only contain letters. Please enter a valid name.")
            continue
        break

    # Status (validated, case-insensitive)
    while True:
        raw_status = input("Status (done/not done): ").strip()
        if raw_status == "":
            print("Status cannot be empty. Please enter 'done' or 'not done'.")
            continue
        sval = raw_status.lower().replace("_", " ").strip()
        if sval in allowed_done:
            status = "done"
            break
        if sval in allowed_not_done:
            status = "not done"
            break
        print("Unrecognized status. Please type 'done' or 'not done' (or y/n).")

    assigned_chores.append(chore_number)
    assigned_roommates.append(roommate_name)
    assigned_status.append(status)

# Count completed chores and completion rate
completed_count = sum(1 for s in assigned_status if s == "done")

total_assigned = len(assigned_chores)
completion_rate = int((completed_count / total_assigned) * 100) if total_assigned > 0 else 0

# Determine room status tag
if completion_rate == 100:
    room_status = "ROOM IS SPOTLESS!"
elif completion_rate >= 50:
    room_status = "ALMOST THERE!"
else:
    room_status = "NEEDS CATCHING UP!"

# Print formatted chore report
print("\n" + "=" * 50)
print(f"ROOM {room_number} -- WEEKLY CHORE REPORT")
print("=" * 50)
print(f"Room Monitor:{room_monitor}")
print("-" * 50)

for i in range(len(assigned_chores)):
    chore_num = assigned_chores[i]
    chore_name = chore_names[chore_num - 1]
    chore_freq = chore_frequency[chore_num - 1]
    roommate = assigned_roommates[i]
    status = assigned_status[i]

    print(f"[{i + 1}] {chore_name:<24} [{chore_freq}]")
    print(f" Roommate:{roommate}")
    print(f" Status:{status}")

print("-" * 50)
print(f"Completed:{completed_count} out of {total_assigned} assigned")
print(f"Completion Rate:{completion_rate}%")
print(f"Room Status:{room_status}")
print("=" * 50)

