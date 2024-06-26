import First_Project, Second_Project, os

# Ask user to choose a project
project = input("1. first project\n2. second project\npick one: ")

if project == "1":
    cll = []  # Initialize list of CircularLinkedLists
    stacks = []  # Initialize list of Stacks
    queues = []  # Initialize list of Queues

    while True:
        os.system("cls")  # Clear screen
        print("1.create a CircularLinkedList\n2.add a node to list\n3. display list\n4.remove prime "
              "numbers\n5.sorting and merging two lists\n6.creating a stack\n7.using a stack\n8.creating a "
              "queue\n9.using a queue")

        answer = input("pick one: ")  # Ask user for input

        if answer == "1":
            os.system("cls")  # Clear screen
            cll.append(First_Project.CircularLinkedList())  # Create a new CircularLinkedList object
            print("new list added")  # Print confirmation
            input("press enter to go back")  # Wait for user input

        elif answer == "2":
            os.system("cls")  # Clear screen
            print("which list you want to add node to:")
            counter = 1
            for x in cll:
                print(counter, ":")
                x.display()
                counter += 1

            add_node = int(input("pick one: "))
            node_content = int(input("what is the node: "))
            cll[add_node - 1].append(node_content)
            cll[add_node - 1].display()
            input("press enter to go back")

        elif answer == "3":
            os.system("cls")  # Clear screen
            for x in cll:
                x.display()
            input("press enter to go back")

        elif answer == "4":
            os.system("cls")  # Clear screen
            print("which list you want to remove prime numbers of:")
            counter = 1
            for x in cll:
                print(counter, ":")
                x.display()
                counter += 1

            primes = int(input("pick one: ")) - 1
            cll[primes].remove_primes()
            cll[primes].display()
            input("press enter to go back")

        elif answer == "5":
            os.system("cls")  # Clear screen
            counter = 1
            for x in cll:
                print(counter, ":")
                x.display()
                counter += 1

            first_list = int(input("first list: ")) - 1
            second_list = int(input("second list: ")) - 1
            result = First_Project.CircularLinkedList.merge_sorted(cll[first_list], cll[second_list])
            print("merged list = ")
            result.display()

            if input("do you want to add it to the lists?(y/n)") == "y":
                cll.append(result)
                print("added")
                input("press enter to go back")
            else:
                input("press enter to go back")

        elif answer == "6":
            os.system("cls")  # Clear screen
            stacks.append(First_Project.Stack())  # Create a new Stack object
            print("new stack added")  # Print confirmation
            input("press enter to go back")  # Wait for user input

        elif answer == "7":
            os.system("cls")  # Clear screen
            counter = 1
            for x in stacks:
                print(counter, ": ")

            stack_to_use = int(input("pick one: ")) - 1
            usage = input("1.push\n2.pop\npick one: ")

            if usage == "1":
                data = int(input("gimme a number: "))
                stacks[stack_to_use].push(data)
            elif usage == "2":
                stacks[stack_to_use].pop()

            stacks[stack_to_use].display()
            input("press enter to go back")

        elif answer == "8":
            os.system("cls")  # Clear screen
            queues.append(First_Project.Queue())  # Create a new Queue object
            print("new queue added")  # Print confirmation
            input("press enter to go back")  # Wait for user input

        elif answer == "9":
            os.system("cls")  # Clear screen
            counter = 1
            for x in queues:
                print(counter, ": ")

            queue_to_use = int(input("pick one: ")) - 1
            usage = input("1.add\n2.delete\npick one: ")

            if usage == "1":
                data = int(input("gimme a number: "))
                queues[queue_to_use].add(data)
            elif usage == "2":
                queues[queue_to_use].delete()

            queues[queue_to_use].display()
            input("press enter to go back")

elif project == "2":
    while True:
        os.system("cls")  # Clear screen
        print("1.infix to postfix\n2.infix to prefix\n3.postfix to infix\n4.postfix to prefix\n5.prefix to "
              "infix\n6.prefix to postfix")

        answer = input("pick one: ")  # Ask user for input

        if answer == "1":
            os.system("cls")  # Clear screen
            Second_Project.infix_to_postfix(input("infix expression: "))  # Convert infix to postfix
            input("press enter to go back")  # Wait for user input

        elif answer == "2":
            os.system("cls")  # Clear screen
            Second_Project.infix_to_prefix(input("infix expression: "))  # Convert infix to prefix
            input("press enter to go back")  # Wait for user input

        elif answer == "3":
            os.system("cls")  # Clear screen
            Second_Project.postfix_to_infix(input("postfix expression: "))  # Convert postfix to infix
            input("press enter to go back")  # Wait for user input

        elif answer == "4":
            os.system("cls")  # Clear screen
            Second_Project.postfix_to_prefix(input("postfix expression: "))  # Convert postfix to prefix
            input("press enter to go back")  # Wait for user input

        elif answer == "5":
            os.system("cls")  # Clear screen
            Second_Project.prefix_to_infix(input("prefix expression: "))  # Convert prefix to infix
            input("press enter to go back")  # Wait for user input

        elif answer == "6":
            os.system("cls")  # Clear screen
            Second_Project.prefix_to_postfix(input("prefix expression: "))  # Convert prefix to postfix
            input("press enter to go back")  # Wait for user input
