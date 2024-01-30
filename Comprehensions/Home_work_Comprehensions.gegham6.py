def access_elemet(my_list, index):
    try:
        Element = my_list[index]
        print(f"Element of index {index}: {Element}")
    except IndexError:
        print(f"indexError: index {index} is out of range.")
    finally:
        print("task completed")

my_list =[1, 2, 3, 4, 5]

access_elemet (my_list, 2)

access_elemet(my_list, 7)