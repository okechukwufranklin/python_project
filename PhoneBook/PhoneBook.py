PhoneBook = []

def Save_Number():
    contact_info = {}
    ContactName = input("Enter Name:")
    ContactNumber = int(input("Enter Phone Number:"))
    contact_info[ContactName] = ContactNumber
    PhoneBook.append(contact_info)
    PhoneBook_Display()
    return contact_info

def Delete_Number(name):
    for contact_info in PhoneBook:
        if name in contact_info:
            del contact_info[name]
            print(f"Contact for '{name}' deleted successfully.")
            PhoneBook_Display()
            return
    print(f"Contact for '{name}' not found in the PhoneBook.")

    print("1.back\n 2.Exit")
    number = int(input())
    if number == 1:
        PhoneBook_Display()
    if number == 2:
        pass


def Search_Name(name):
    for contact_info in range(len(PhoneBook)):
        if name in PhoneBook[contact_info]:
            print(PhoneBook[contact_info])
    print("1.back\n 2.Exit")
    number = int(input())
    if number == 1:
        PhoneBook_Display()
    if number == 2:
        pass


def Veiw_Contacts():
    for contact_info in PhoneBook:
        print(PhoneBook)
        return PhoneBook
    print("1.back\n 2.Exit")

    number = int(input())
    if number == 1:
         PhoneBook_Display()
    if number == 2:
        pass


def Edit_Contacts():
    print("feature coming Soon")
    print("Stay Tune For Next Update")
    print("1.back\n 2.Exit")
    number = int(input())
    if number == 1:
        PhoneBook_Display()
    if number == 2:
        pass



def PhoneBook_Display():
    number = int(input("1.Save Number\n2.Edit Number\n3.Delete Number\n4.Search Number\n5.View Contacts\n"))
    if number == 1:
        Save_Number()
    if number == 2:
        Edit_Contacts()
    if number == 3:
        name = input("Enter Name To Delete")
        Delete_Number(name)
    if number== 4:
        name = input("Enter Name To Search")
        Search_Name(name)
    if number == 5:
        Veiw_Contacts()


PhoneBook_Display()
