
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

    
def main():
    adder_obj = Adder()
    print(adder_obj.sum(1,1))

if __name__ == "__main__":
    main()