queue = []

def viewQueue():
    for i in range(len(queue)):
        print(queue[i])

def enqueue():
    value = input("Enter item you wish to enter into the queue: ")
    queue.append(value)

def dequeue():
    '''Remove item from the top of the stack (once stack isn't empty)'''
    if len(queue) > 0:
        value = queue.pop(0) #removes item at first index
        print(value, "was removed from the stack.")

def main():
    choice = '0'
    print("\nStack Implentation in Python")
    while choice != '4':
        print("\n************************************")
        print("1) View items in the queue")
        print("2) Add an item to the bottom of queue")
        print("3) Remove item from top of queue")
        print("4) Exit...")
        print("************************************")
    
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            viewQueue()
        elif choice == '2':
            enqueue()
        elif choice == '3':
            dequeue()
        elif choice == '4':
            print("Successfully exited the program :) ")
            break
        else:
            print("Invalid Selection")

main()
