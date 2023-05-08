import csv

def flip_album():
    album = []
    with open('album.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            album.append(row)

    page = 0
    while True:
        print(f'Page {page + 1}\n')
        for i in range(1, 11):
            sticker_id = page * 10 + i
            sticker = next((s for s in album if s['id'] == str(sticker_id)), None)
            if sticker:
                if sticker['contain'].lower() == 'y':
                    print(f"{sticker['id']}. {sticker['name']} - {sticker['content']}")
                elif sticker['contain'].lower() == 'c':
                    print(f"{sticker['id']}. COLAR")
                elif sticker['contain'].lower() == 'n':
                    print(f"{sticker_id}. X")
            else:
                continue

        print("\nWhat would you like to do?")
        print("1. Next page")
        print("2. Previous page")
        print("3. Back to menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            if (page + 1) * 10 < len(album):
                page += 1
            else:
                print("You have reached the last page.")
        elif choice == "2":
            if page > 0:
                page -= 1
            else:
                print("You are already on the first page.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.\n")