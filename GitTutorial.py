
"""
    Tutorial Python Script to showcase different methods of git workflow with collaborators
    Very basic tutorial on git add, git commit, git push, and git rebase

"""


class Adder:

    def sum(self, x, y):
        """
            returns sum of x and y args
        """
        return x + y 
    def add_2(self, x):
        """
            returns sum of 2 and x arg
        """
        return x + 2
class Multiplyer:
    def multiply(self, x, y):
        """
            returns product of x and y args
        """
        return x * y

class Subtractor:
    def subtract(self, x, y):
        """
            returns difference of x and y args
        """
        return x - y
    
def main():
    adder_obj = Adder()
    multiplyer_obj = Multiplyer()

    print(adder_obj.sum(1,1))
    print(adder_obj.add_2(2))

    print(multiplyer_obj.multiply(2,2))

if __name__ == "__main__":
    main()