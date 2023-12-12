
def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        count = 0
        out = "The line is currently:"
        while count < len(katz_deli):
            out += f" {count+1}. {katz_deli[count]}"
            count += 1
        print(out)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")


def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del katz_deli[0]
