import module2 as f
ul=f.input_universities()
f.write_to_bin("Universities.bin",ul)
print("Input city")
city=input()
name_and_fakultet=f.max_students(ul,city)
nul=f.acreditation(ul)
f.write_to_bin2("Acreditation.bin",nul)
f.out_universities(ul)
print("The fakultet with the most count of students in ",city)
print(name_and_fakultet[0],": ",name_and_fakultet[1])
print()
print("Universities with 3 and 4 degree of acreditation")
f.out_acreditation(nul);