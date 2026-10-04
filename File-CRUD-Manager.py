from pathlib import Path
import os

def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}  :  {items}")


def createfile():
    try:
        readfileandfolder()
        name =input("Enter your file name:")
        p=Path(name)

        if not p.exists():
            with open(p,'w') as fs:
                data=input("what you want to write in this file:-")
                fs.write(data)

            print("file created successfully")
        else:
            print("This file already exist.")

    except Exception as err:
        print(f"an error occured as{err}")


def readfile():
       try:
           readfileandfolder()
           name=input("which file you want to read:-")
           p=Path(name)
           if p.exists() and p.is_file():
                       with open(p,'r') as fs:
                           data=fs.read()
                           print(data)

                       print("readed successfully")
           else:
                       print("this file doesnot exist")

       except Exception as err:
                print(f"an error occured as{err}")


def updatefile():
     try:
           readfileandfolder()
           name=input("which file you want to update:-")
           p=Path(name)
           if p.exists() and p.is_file():
                print('press 1 for changing file name :-')
                print("press  2 for overwriting the data of  file:-")
                print("press  3 for appending some content in your file:- ")
                res=int(input("tell your response:-"))
                if res==1:
                     name2=input("tell your new file name:-")
                     p2=Path(name2)
                     p.rename(p2)
                if res==2:
                     with open(p,'w') as fs:
                          data=input("what you want to write this is overwrite the data:-")
                          fs.write(data)
                if res==3:
                       with open(p,'a') as fs:
                        data=input("what you want to append:-")
                        fs.write(""+data)
           else:
                print("this file doesnot exist")

     except Exception as err:
                    print(f"an error occured as{err}")


def deletefile():
      try:
                 readfileandfolder()
                 name=input("which file you want to delete:-")
                 p=Path(name)
                 if p.exists() and p.is_file():
                    os.remove(p)
                    print("removed successfully")
                 else:
                             print("No such file exists. ")

      except Exception as err:
                      print(f"an error occured as{err}")


print("Press 1 for creating file")
print("Press 2 for reading file")
print("Press 3 for updating file")
print("Press 4 for deletion file")

check =int(input("please tell your response"))

if check==1:
    createfile()
if check==2:
    readfile()

if check==3:
    updatefile()

if check==4:
      deletefile()