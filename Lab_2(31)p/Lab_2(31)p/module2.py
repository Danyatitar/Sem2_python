from typing import NamedTuple
import pickle
class Fakultet(NamedTuple):
    name: str
    number_of_students: int
class University(NamedTuple):
    name: str
    city: str
    degree_of_acreditation: int
    number_of_fakultets: int
    fakultets: list
def out_universities(ul:list)-> None:
    for i in range(len(ul)):
     print("name: ",ul[i].name)
     print("city: ", ul[i].city)
     print("degree_of_acreditation: ", ul[i].degree_of_acreditation)
     print("number_of_fakultets: ", ul[i].number_of_fakultets)
     for i in range(len(ul[i].fakultets)):
         out_fakultets(ul[i].fakultets)
     print()
def out_acreditation(nul:list)-> None:
    for i in range(len(nul)):
     print("name: ",nul[i].name)
     print("city: ", nul[i].city)
     print("degree_of_acreditation: ", nul[i].degree_of_acreditation)
     print()
def out_fakultets(fl:list) -> None:
    for i in range(len(fl)):
      print("name_of_fakultet: ", fl[i].name)
      print("number_of_students: ", fl[i].number_of_students)
def input_universities()-> list:
    print("input number of universities")
    n=int(input())
    ul=[]
    for j in range(n):
     fl=[]
     print("input name of university")
     name=input()
     print("input city")
     city=input()
     print("input degree of acreditation")
     degree_of_acreditation=int(input())
     print("input number of fakultets")
     number_of_fakultets=int(input())
     for i in range(number_of_fakultets):
         print("input name of fakultet")
         name_fakultet=input()
         print("input number of students")
         number_of_students=int(input())
         f=Fakultet(name_fakultet,number_of_students)
         fl.append(f)
     print()
     u=University(name,city,degree_of_acreditation,number_of_fakultets,fl)
     ul.append(u)
    return ul

def max_students(ul:list,city:str)->list:    
    students=[]
    name_and_fakultet=[]
    for i in range(len(ul)):
        if(ul[i].city==city):
            for j in range(len(ul[i].fakultets)):
                students.append(ul[i].fakultets[j].number_of_students)
    max=0
    for i in range(len(students)):
        if(students[i]>max):
            max=students[i]
    for i in range(len(ul)):
        if(ul[i].city==city):
         for j in range(len(ul[i].fakultets)):
            if (ul[i].fakultets[j].number_of_students==max):
                name_and_fakultet.append(ul[i].name)
                name_and_fakultet.append(ul[i].fakultets[j].name)
    return name_and_fakultet
def acreditation(ul:list)->list:
    nul=[]
    for i in range(len(ul)):
        if(ul[i].degree_of_acreditation==3 or ul[i].degree_of_acreditation==4):
            nul.append(ul[i])
    return nul
def write_to_bin(name: str, list: list) -> None:
    pickle.dump(list, open(name, 'wb'))
def write_to_bin2(name: str, list: list) -> None:
    f=open(name, 'wb');
    for i in range(len(list)):
     pickle.dump(list[i].name, f)
     pickle.dump(list[i].city, f)
     pickle.dump(list[i].degree_of_acreditation, f)
    f.close()
def read_from_bin(name: str) -> list:
    list = pickle.load(open(name, 'rb'))
    return list