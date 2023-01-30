"""
    Tutorial Python Script to showcase different methods of git workflow with collaborators
    Very basic tutorial on git add, git commit, git push, and git rebase

"""


class Adder:
    @classmethod
    def sum(x, y):
        """
        returns sum of x and y args
        """
        return x + y


def main():
    print(Adder.sum(1, 1))


if __name__ == "__main__":
    main()
