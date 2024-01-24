# pytran
Python util to transfer repos between GitHub usernames

## Setup
- Setup your virtual environment, e.g. via https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment
- Install requirements, i.e.

```
(.venv) allyndawn@Astera pytran % pip install -r requirements.txt
Requirement already satisfied: numpy==1.26.3 in ./.venv/lib/python3.11/site-packages (from -r requirements.txt (line 1)) (1.26.3)
```

- Copy `sampleconfig.json` to `config.json` at the root of the project
- Edit `config.json` to contain the GitHub username and personal access token you want to transfer from and the GitHub username to transfer to

## Running
- python pytran.py

Sample UI:

```
0 myoldname.github.io
1 wx-serial-poster
2 tm4c123-interrupts-iar
3 bee525-lab1-task3
4 bee525-lab1-task8
5 hellodocker2
6 BEE531HW4
7 BEE590HW4
8 Decoders
9 github-pages-with-jekyll
10 BEE590HW1
11 bee525-lab1-task1
12 bee525-lab1-task4
13 BEE532HW2
Enter number of repo to transfer from myoldname to allyndawn (or just hit enter to abort): 2
Transfer of tm4c123-interrupts-iar initiated
```

