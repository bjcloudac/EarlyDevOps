# EarlyDevOps
## A small Entry Level DevOps Project
>Prerequisites:
 This project make use of Codespaces & Co-Pilot from GitHub which makes projects easy to integarte with GitHub and get Codehelp from Co-Pilot.    

~~Optional Steps if you use codepsace. Co-Pilot can be tried out for free for a period if you want.~~

*1.Create Your GitHub repo 2. Go to the Repo 3. Click on Code-> CodeSpaces-> +icon to create and start code spaces on main repo 4. Use the cloud Visual Studio Code as your editor*

* Create a small python program to illustrate unit testing, create a folder `mkdir eDevOp` and `touch mymodule.py`
* `cd eDevOp` followed by `vi mymodule.py` or simply open the file in an editor. Then make an initial python program:
>`def square(no):
        return no ** 2`
    
* make first commit to the repo by `git add *` then `git status` to make sure it adds mymodule.py and readme.md then `git commit -m "Adding first python file and readme to the repo"` then `git push` to add to your cloud repo.

* Now create a test file called test_mymodule.py and generate the code like:
`import unittest`
`from mymodule import square`

`class TestSquare(unittest.TestCase):`
    `def test_square(self):`
        `self.assertEqual(square(10), 100)`
        `self.assertEqual(square(0), 0)`
        `self.assertEqual(square(-5), 25)`

`if __name__ == '__main__':`
    `unittest.main()`
* #`python3 -m unittest test_mymodule.py` - Use this line to run the tests from terminal

*Again Make Your Commits to the repo*

