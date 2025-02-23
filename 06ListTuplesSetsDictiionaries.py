a=[]


print(a)


a=["Baneen", "Esha","Esha",  "Urooj", "Urooj","Urooj"  , "Urooj", "Hafsa", "Hamza", "Arshad", "Talha","Junaid", "Saaria"]

print(a)
print(a[4])

a[4]="Hamza Faisal"


print(a)


a.sort()
print(a)


a.reverse()
print(a)



a.append("Ali")

print(a)



a.insert(2, "Taha")

print(a)

a.pop(2)
print(a)


a.remove("Ali")
print(a)


print(a.count("Esha"))
a.clear()
print(a)






a={}

print(type(a))

a=set()
print(type(a))


a={2,3,3,3,4,5,89}

print(a)


a.add(78)
a.add((34,4,55))

print(a)
a.pop()
print(a)

a.remove(89)
print(a)


print(len(a))







a=()
print(a)


a=(1,)

print(type(a))


a=("maryam", "fatimah","Hamza", "Hamza","Saaria")
print(a)



print(a[1])


print(a.count("Hamza"))



print(a.index("maryam"))




a={


    "name":"hamza",
    "age":24,
    "hobbies":["reading", "programming"],
    "education":{
        "BS":2021,
        "MS":2024,
        "DS":2025
    }
}

print(a["name"])
print(a["hobbies"])
print(a["education"]["DS"])




print(a.keys())
print(a.values())
print(a.items())
print(a)


print(a["age"])
print(a.get("age"))



words={

    "saniha":"accident",
    "qalam":"pen",
    "kitab":"book"

}


print("check your words ", list(words.keys()))


search= input("Enter Your Word")


print(words.get(search))