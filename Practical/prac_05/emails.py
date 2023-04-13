def main():
    email_dict = {}
    while True:
        email = input("Email: ")
        if email == "":
            break

        name = extract_name(email)
        name_prompt = f"Is your name {name}? (Y/n) "
        confirm = input(name_prompt).lower()
        if confirm == "" or confirm == "y":
            email_dict[email] = name
        else:
            name = input("Name: ")
            email_dict[email] = name.title()

    for email, name in email_dict.items():
        print(f"{name} ({email})")


def extract_name(email):
    """
    Given an email, extracts the name of the user by taking the part before the @ symbol
    and replacing periods with spaces. Returns the extracted name.
    """
    name = email.split("@")[0]
    name = name.replace(".", " ")
    return name.title()


main()
