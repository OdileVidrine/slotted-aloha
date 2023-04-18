import mathplotlib.pyplot as plt
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def aloha(p):
    n = 5
    return n*p(1-p)**(n-1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    y = list()
    x = list()
    for i in range(0, 95, 5):
        p = i * 0.01
        x.append(p)
        y.append(aloha(p))
        plt.plot(x, y)
        plt.show()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
