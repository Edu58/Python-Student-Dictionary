students = [
    {
        "email": "edwin@gmail.com",
        "name": "Edwin",
        "age": 12,
        "movie": "The Social Network"
    },
    {
        "email": "nancy@gmail.com",
        "name": "Nancy",
        "age": 10,
        "movie": "Coco"
    },
    {
        "email": "zipporah@gmail.com",
        "name": "Zipporah",
        "age": 50,
        "movie": "Young, Rich & Famous"
    },
    {
        "email": "rock@gmail.com",
        "name": "Rock",
        "age": 30,
        "movie": "Fast & Furious 9"
    },
    {
        "email": "john@gmail.com",
        "name": "John",
        "age": 32,
        "movie": "Blackish"
    }
]

print("Enter an email:")
email = input()

for d in students:
    if d["email"] == email:
        print("Name - {}".format(d["name"]))
        print("Age - {}".format(d["age"]))
        print("Favorite Movie - {}".format(d["movie"]))
