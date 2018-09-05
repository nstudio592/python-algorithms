'''A stack is a data structure where items are inserted and remove from
the top of the list. It can be envisioned as a stack of books or 
plates.'''
stack = []

def viewStack():
    '''View all items in the stack'''
    if len(stack) < 0:
        print("Stack is empty")
    else:
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])

def push():
    '''Add item to the top of the stack'''
    value = input("Enter item you wish to add to the stack: ")
    stack.append(value)

def pop():
    '''Remove item from the top of the stack (once stack isn't empty)'''
    if len(stack) > 0:
        value = stack.pop(-1) #removes item at last index
        print(value, "was removed from the stack.")

def main():
    choice = '0'
    print("\nStack Implentation in Python")
    while choice != '4':
        print("\n************************************")
        print("1) View items in the stack")
        print("2) Add an item to the top of stack")
        print("3) Remove item from top of stack")
        print("4) Exit...")
        print("************************************")
    
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            viewStack()
        elif choice == '2':
            push()
        elif choice == '3':
            pop()
        elif choice == '4':
            print("Successfully exited the program :) ")
            break
        else:
            print("Invalid Selection")

main()
    
        
    
    
    
    
        

