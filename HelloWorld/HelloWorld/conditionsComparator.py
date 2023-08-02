name = "Jen"
name_char_count = len(name)

if name_char_count < 3:
    print("Name must be at least 3 characters")
elif name_char_count > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")