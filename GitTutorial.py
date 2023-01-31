"""
    Tutorial Python Script to showcase different methods of git workflow with collaborators
    Very basic tutorial on git add, git commit, git push, and git rebase

"""


class Adder:
    @classmethod
    def sum(cls, x, y):
        """
        returns sum of x and y args
        """
        return x + y

    @classmethod
    def add_2(cls, x):
        """
            Returns sum of 2 and x
        """
        return 2 + x

def main():
    print(Adder.sum(1, 1))
    print(Adder.add_2(1))

if __name__ == "__main__":
    main()
