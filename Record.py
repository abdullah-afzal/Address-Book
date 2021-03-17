import string
import re
class Record:

    def addRecord(self):
        self.name = input("Enter Name:\t")
        while self.name.strip() == "":
            print("Name can not be empty :)")
            self.name = input("Enter First Name:\t")
        self.mobile = input("Enter Mobile number:\t")
        while not(self.mobile.isdigit()):
            print("Invalid mobile number")
            self.mobile = input("Enter a valid mobile number:\t")
        self.phone = input("Enter Landline number:\t")
        while not(self.phone.isdigit()):
            self.phone = input("Enter a valid phone number:\t")
        self.email = input("Enter Email:\t")
        emailExpression = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        while not(re.search(emailExpression,self.email)):
            self.email=input("Enter a valid Email address:\t")
        self.website = input("Enter Website:\t")
        websiteExpression = '^[a-z0-9]+[\._]?[a-z0-9]+\w+[.]\w{2,3}$'
        while not (re.search(websiteExpression, self.website)):
            self.website = input("Enter a valid site address:\t")
        self.city = input("Enter City:\t")
        while self.city.strip() == "":
            print("City name can not be empty :)")
            self.city = input("Enter valid city name:\t")
        self.profession = input("Enter Profession\t")
        while self.profession.strip() == "":
            print("Profession name can not be empty :)")
            self.city = input("Enter valid Profession:\t")
        fileReader = open('Addressbook.txt')
        bool = 1
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if self.mobile == part[1] or self.phone == part[2] or self.email == part[3]:
                    bool = 0
        fileReader.close()
        if bool == 0:
            print("Record already exist with matching parameters")
        elif bool == 1:
            file = open('Addressbook.txt', 'a')
            file.write(
                self.name + "," + self.mobile + "," + self.phone + "," + self.email + "," + self.website + "," + self.city + "," + self.profession)
            file.write("\n")
            file.close()
            print("-------Record Added-------")
    def display(self, part):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Name = " + part[0])
        print("Mobile = " + part[1])
        print("Phone = " + part[2])
        print("Email = " + part[3])
        print("Website = " + part[4])
        print("City = " + part[5])
        print("Profession = " + part[6])

    def searchByExactName(self, name):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if name == part[0]:
                    bool = 1
                    self.display(part)
        return bool

    def searchByExactMobile(self, mobile):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if mobile == part[1]:
                    bool = 1
                    self.display(part)
        return bool

    def searchByExactPhone(self, phone):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if phone == part[2]:
                    bool = 1
                    self.display(part)
        return bool

    def searchByExactEmail(self, email):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if email == part[3]:
                    bool = 1
                    self.display(part)
        return bool

    def searchByExactWeb(self, site):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if site == part[4]:
                    bool = 1
                    self.display(part)
        return bool

    def searchByExactCity(self, city):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if city == part[5]:
                    bool = 1
                    self.display(part)
        return bool

    def searchByExactProfession(self, profession):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if profession == part[6]:
                    bool = 1
                    self.display(part)
        return bool
    def searchByName(self,name):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if name in part[0]:
                    bool = 1
                    self.display(part)
        return bool
    def searchByMobile(self,mobile):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if mobile in part[1]:
                    bool = 1
                    self.display(part)
        return bool
    def searchBYphone(self,phone):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if phone in part[2]:
                    bool = 1
                    self.display(part)
        return bool
    def searchByEmail(self,email):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if email in part[3]:
                    bool = 1
                    self.display(part)
        return bool
    def searchByWeb(self,site):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if site in part[4]:
                    bool = 1
                    self.display(part)
        return bool
    def searchByCity(self,city):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if city in part[5]:
                    bool = 1
                    self.display(part)
        return bool
    def searchByProfession(self,profession):
        bool = 0
        fileReader = open('Addressbook.txt')
        for line in fileReader:
            if line != "\n":
                part = line.split(",")
                if profession in part[6]:
                    bool = 1
                    self.display(part)
        return bool
    def VIPdelete(self,name,mobile):
        bool = 0
        fileReader = open("Addressbook.txt", "r")
        lines = fileReader.readlines()
        fileReader = open("Addressbook.txt", "w")
        for line in lines:
            if line != "\n":
                part = line.split(",")
                if name == part[0] and mobile == part[1]:
                    bool = 1
                else:
                    fileReader.write(line)
        return bool
    def deleteAllContactByName(self,name):
        bool = 0
        fileReader = open("Addressbook.txt", "r")
        lines = fileReader.readlines()
        fileReader = open("Addressbook.txt", "w")
        for line in lines:
            if line != "\n":
                part = line.split(",")
                if name != part[0]:
                    fileReader.write(line)
                else:
                    bool = 1
        return bool
    def deleteAllContactByMobile(self,mobile):
        bool = 0
        fileReader = open("Addressbook.txt", "r")
        lines = fileReader.readlines()
        fileReader = open("Addressbook.txt", "w")
        for line in lines:
            if line != "\n":
                part = line.split(",")
                if mobile != part[1]:
                    fileReader.write(line)
                else:
                    bool = 1
        return bool
    def deleteAllContactByCity(self,city):
        bool = 0
        fileReader = open("Addressbook.txt", "r")
        lines = fileReader.readlines()
        fileReader = open("Addressbook.txt", "w")
        for line in lines:
            if line != "\n":
                part = line.split(",")
                if city != part[5]:
                    fileReader.write(line)
                else:
                    bool = 1
        return bool
    def updateByName(self,oname,omobile,uname):
        bool = 0
        fileReader = open("Addressbook.txt", "r")
        lines = fileReader.readlines()
        fileReader = open("Addressbook.txt", "w")
        for line in lines:
            if line != "\n":
                part = line.split(",")
                if oname == part[0] and omobile == part[1]:
                    fileReader.write(uname+","+part[1]+","+part[2]+","+part[3]+","+part[4]+","+part[5]+","+part[6])
                else:
                    fileReader.write(line)
        return bool
    def updateByMobile(self,oname,omobile,mobile):
        bool = 0
        fileReader = open("Addressbook.txt", "r")
        lines = fileReader.readlines()
        fileReader = open("Addressbook.txt", "w")
        for line in lines:
            if line != "\n":
                part = line.split(",")
                if oname == part[0] and omobile == part[1]:
                    fileReader.write(part[0] + "," + mobile + "," + part[2] + "," + part[3] + "," + part[4] + "," + part[5] + "," +part[6])
                else:
                    fileReader.write(line)
        return bool
    def updateByCity(self,oname,omobile,city):
        bool = 0
        fileReader = open("Addressbook.txt", "r")
        lines = fileReader.readlines()
        fileReader = open("Addressbook.txt", "w")
        for line in lines:
            if line != "\n":
                part = line.split(",")
                if oname == part[0] and omobile == part[1]:
                    fileReader.write(part[0]+ "," + part[1] + "," + part[2] + "," + part[3] + "," + part[4] + "," + city + "," +part[6])
                else:
                    fileReader.write(line)
        return bool
    def updateByWeb(self,oname,omobile,web):
        bool = 0
        fileReader = open("Addressbook.txt", "r")
        lines = fileReader.readlines()
        fileReader = open("Addressbook.txt", "w")
        for line in lines:
            if line != "\n":
                part = line.split(",")
                if oname == part[0] and omobile == part[1]:
                    fileReader.write(part[0] + "," + part[1] + "," + part[2] + "," + part[3] + "," + web + "," + part[5] + "," + part[6])
                else:
                    fileReader.write(line)
        return bool
    def updateByEmail(self,oname,omobile,email):
        bool = 0
        fileReader = open("Addressbook.txt", "r")
        lines = fileReader.readlines()
        fileReader = open("Addressbook.txt", "w")
        for line in lines:
            if line != "\n":
                part = line.split(",")
                if oname == part[0] and omobile == part[1]:
                    fileReader.write(part[0] + "," + part[1] + "," + part[2] + "," + email + "," + part[4] + "," + part[5] + "," + part[6])
                else:
                    fileReader.write(line)
        return bool
    def updateByPhone(self,oname,omobile,ph):
        bool = 0
        fileReader = open("Addressbook.txt", "r")
        lines = fileReader.readlines()
        fileReader = open("Addressbook.txt", "w")
        for line in lines:
            if line != "\n":
                part = line.split(",")
                if oname == part[0] and omobile == part[1]:
                    fileReader.write(part[0] + "," + part[1] + "," + ph + "," + part[3] + "," + part[4] + "," + part[5] + "," + part[6])
                else:
                    fileReader.write(line)
        return bool
    def updateByProfession(self,oname,omobile,prof):
        bool = 0
        fileReader = open("Addressbook.txt", "r")
        lines = fileReader.readlines()
        fileReader = open("Addressbook.txt", "w")
        for line in lines:
            if line != "\n":
                part = line.split(",")
                if oname == part[0] and omobile == part[1]:
                    fileReader.write(part[0] + "," + part[1] + "," + part[2] + "," + part[3] + "," + part[4] + "," + part[5] + "," +prof)
                else:
                    fileReader.write(line)
        return bool