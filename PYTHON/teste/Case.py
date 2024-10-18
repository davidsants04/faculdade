import random

numero=random.randint(1,5)

match numero:

    case 1:
        print("numero um kkkk")
    case 2:
        print("numero dois kkk")
    case _:
        print("outro numero") # case _ Serve como um "else"
