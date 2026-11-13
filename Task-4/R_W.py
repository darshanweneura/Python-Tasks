Students = ["Darshan", "Nandani","Krishna", "Meet"]
n = len(Students)


for i in range(n):

    file = open("student.txt", "a")

    file.write("\nName: "+ Students[i])
    file.close()
    

file = open("student.txt", "r")
Data = file.read()
print(Data)

file.close()



try:
    with open("Students.txt" ,"r" ) as file:
        print(file.read())
except FileNotFoundError:

    print("File does not exist!")