from Record import Record
def main():
    temp = Record()
    print("*******************************************")
    print("\t\t\tAddress Book")
    print("*******************************************")
    print("Select an option")
    print("1.\tAdd record")
    print("2.\tUpdate record")
    print("3.\tExect record search")
    print("4.\tSearch by hint")
    print("5.\tSearch and delete specific record")
    print("6.\tSearch and delete a collection")
    print("0.\tExit")
    option = input("Enter your choice:-\t ")
    while option <'0' or option>'6':
        option=input("Select a valid choice:\t ")
    if option == '0':
        exit()
    elif option == '1':
        temp.addRecord()
    elif option == '2':
        iName = input("Enter current name\t")
        iMobile = input("Enter current mobile number\t")
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if iName == part[0] and iMobile == part[1]:
                    bool = 1
        if bool == 0:
            print("No record found")
        else:
            print("\t\ta.Update Name")
            print("\t\tb.Update Mobile")
            print("\t\tc.Update Phone")
            print("\t\td.Update Email")
            print("\t\te.Update Website")
            print("\t\tf.Update City")
            print("\t\tg.Update Profession")
            subchoice = input("Select an option\t")
            while subchoice < 'a' or subchoice > 'g':
                subchoice = input("Enter a valid choice\t")
            if subchoice == 'a':
                newValue = input("Enter new name:\t")
                temp.updateByName(iName, iMobile, newValue)
                print("Record Update successfully")
            if subchoice == 'b':
                newValue = input("Enter new Mobile number:\t")
                fileReader = open('Addressbook.txt')
                for line in fileReader:
                    if line != "\n":
                        part = line.split(",")
                        if newValue == part[1]:
                            print("A record already exist with same mobile number")
                        else:
                            temp.updateByMobile(iName, iMobile, newValue)
                            print("Record Update successfully")
            if subchoice == 'c':
                newValue = input("Enter new Phone number:\t")
                fileReader = open('Addressbook.txt')
                for line in fileReader:
                    if line != "\n":
                        part = line.split(",")
                        if newValue == part[2]:
                            print("A record already exist with same phone number")
                        else:
                            temp.updateByPhone(iName, iMobile, newValue)
                            print("Record Update successfully")
            if subchoice == 'd':
                newValue = input("Enter new email:\t")
                fileReader = open('Addressbook.txt')
                for line in fileReader:
                    if line != "\n":
                        part = line.split(",")
                        if newValue == part[1]:
                            print("A record already exist with same email")
                        else:
                            temp.updateByEmail(iName, iMobile, newValue)
                            print("Record Update successfully")
            if subchoice == 'e':
                newValue = input("Enter new website:\t")
                temp.updateByWeb(iName, iMobile, newValue)
                print("Record Update successfully")
            if subchoice == 'f':
                newValue = input("Enter new city:\t")
                temp.updateByCity(iName, iMobile, newValue)
                print("Record Update successfully")
            if subchoice == 'g':
                newValue = input("Enter new profession:\t")
                temp.updateByProfession(iName, iMobile, newValue)
                print("Record Update successfully")

    elif option == '3':
        print("\t\ta. Search By Name")
        print("\t\tb. Search By Mobile number")
        print("\t\tc. Search By Phone number")
        print("\t\td. Search By email")
        print("\t\te. Search By website")
        print("\t\tf. Search By city")
        print("\t\tg. Search By profession")
        subChoice = input("Select an option\t")
        while subChoice < 'a' or subChoice > 'g':
            subChoice = input("Select a valid option\t")
        if subChoice == 'a':
            searchName = input("Enter name to search\t")
            if temp.searchByExactName(searchName) == 0:
                print("No results founds (:")
        if subChoice == 'b':
            searchMobile = input("Enter mobile number to search\t")
            if temp.searchByExactMobile(searchMobile) == 0:
                print("No results founds (:")
        if subChoice == 'c':
            searchphone = input("Enter phone number to search\t")
            if temp.searchByExactphone(searchphone) == 0:
                print("No results founds (:")
        if subChoice == 'd':
            searchemail = input("Enter email to search\t")
            if temp.searchByExactEmail(searchemail) == 0:
                print("No results founds (:")
        if subChoice == 'e':
            searchwebsite = input("Enter website to search\t")
            if temp.searchByExactWebsite(searchwebsite) == 0:
                print("No results founds (:")
        if subChoice == 'f':
            searchcity = input("Enter city to search\t")
            if temp.searchByExactCity(searchcity) == 0:
                print("No results founds (:")
        if subChoice == 'g':
            searchprofession = input("Enter profession to search\t")
            if temp.searchByExactProfession(searchprofession) == 0:
                print("No results founds (:")
    elif option == '4':
        print("\t\ta. Search By Name")
        print("\t\tb. Search By Mobile number")
        print("\t\tc. Search By Phone number")
        print("\t\td. Search By email")
        print("\t\te. Search By website")
        print("\t\tf. Search By city")
        print("\t\tg. Search By profession")
        subChoice=input("Select an option\t")
        while subChoice<'a' or subChoice > 'g':
            subChoice = input("Select a valid option\t")
        if subChoice=='a':
            searchName=input("Enter name to search\t")
            if temp.searchByName(searchName) == 0:
                print("No results founds (:")
        if subChoice=='b':
            searchMobile=input("Enter mobile number to search\t")
            if temp.searchByMobile(searchMobile) == 0:
                print("No results founds (:")
        if subChoice=='c':
            searchphone=input("Enter phone number to search\t")
            if temp.searchByphone(searchphone) == 0:
                print("No results founds (:")
        if subChoice=='d':
            searchemail=input("Enter email to search\t")
            if temp.searchByEmail(searchemail) == 0:
                print("No results founds (:")
        if subChoice == 'e':
            searchwebsite = input("Enter website to search\t")
            if temp.searchByWebsite(searchwebsite) == 0:
                print("No results founds (:")
        if subChoice == 'f':
            searchcity = input("Enter city to search\t")
            if temp.searchByCity(searchcity) ==0:
                print("No results founds (:")
        if subChoice == 'g':
            searchprofession = input("Enter profession to search\t")
            if temp.searchByProfession(searchprofession)==0:
                print("No results founds (:")

    elif option == '5':
        iName=input("Enter name\t")
        iMobile=input("Enter mobile number\t")
        if temp.VIPdelete(iName,iMobile)==0:
            print("No such record exist")
        else:
            print("Record deleted successfully")
    elif option == '6':
        print("\t\ta. Delete by name")
        print("\t\tb. Delete by mobile number")
        print("\t\tc. Delete by city")
        subchoice = input("Enter your choice:\t")
        while subchoice < 'a' or subchoice > 'c':
            subchoice = input("Enter a valid choice:\t")
        if subchoice == 'a':
            searchingInput = input("Enter name you want to delete\t")
            if temp.deleteAllContactByName(searchingInput) == 0:
                print("Record not found ):")
            else:
                print("Record deleted successfully :)")
        if subchoice == 'b':
            searchingInput = input("Enter mobile number you want to delete\t")
            if temp.deleteAllContactByMobile(searchingInput) == 0:
                print("Record not found ):")
            else:
                print("Record deleted successfully :)")
        if subchoice == 'c':
            searchingInput = input("Enter city you want to delete\t")
            if temp.deleteAllContactByCity(searchingInput) == 0:
                print("Record not found ):")
            else:
                print("Record deleted successfully :)")
while 1:
    main()