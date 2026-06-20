mytasks=[]
def showMenu():
    print("add task")
    print("view tasks")
    print("exit")

def addTask():
        task=input("enter task to add:")
        mytasks.append(task)
        return
def viewtasks():
      for count, tasks in enumerate(mytasks, start=1):
            print(count, tasks)

def main():
      print("To Do list:")
      while True:
            showMenu()
            choice=input("enter your choice 1-3:")     
            if choice=="1":
                  addTask()
            elif choice=="2":
                  viewtasks()
            elif choice=="3":
                  print("exiting...")
                  break
            else:
                  print("invalid choice")

main()             