import os, sys

commands = [ 'pwd', 'cd', 'ls', 'cat', 'exit' ]

def pwd():
    """ print current working directory """ 
    print(os.getcwd())

def cd(args):
    """ change working directory and print its path """
    try:
        new_path = args[0]
        os.chdir(new_path)
        pwd()
    except: 
        print('error - no such directory ?')

def ls():
    dirs = os.listdir(os.getcwd())
    for item in dirs: 
        print(item)

def cat(args):
    """ prints a file to the terminal """
    filename = args[0]
    try:
        with open(filename) as file: 
            for line in file: 
                print(line, end='')
    except: 
        print('error - file not found ?')
        
def exit():
    print("exit()")
    sys.exit()

def exec(cmd, args):
    """ executes a command and pass args if needed """
    if cmd in commands:
        if args:
            eval(cmd)(args)                     # eval så slipper vi lite if satser
        else: 
            eval(cmd)()

def main():
    """ main loop, cmd will be the command and args a list of arguments """
    while True:
        cmd = input('command > ').split(' ')
        cmd, args = cmd[0], cmd[1:]
        exec(cmd, args)
        
if __name__ == '__main__':
	main()
