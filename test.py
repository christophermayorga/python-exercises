def normalize_name(string):
    string = string.lower()
    string = string.strip()
    string = string.replace(" ", "_")
    for i in string:
        if i.isdigit() == True or i.isalpha() == True or i == "_":
            continue
        else:
            string = string.replace(i, "")
    return string
print(normalize_name("45tyler!!"))