customer={
    "name":"John Smith",
    "age":30,
    "isVerified":True
}
print(customer["name"])
print(customer.get("birthdate"))
print(customer.get("birthdate", "Jan 1 2006"))
customer["name"]="Jack Smith"
print(customer["name"])
customer["gender"]="Male"
print(customer)
