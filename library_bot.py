import json

with open("books.json", "r") as f:
    books = json.load(f)

while True:
    question = input("You: ").lower()

    for book in books:
        if book["title"].lower() in question:
            print("Book Found")
            print("Author:", book["author"])
            break