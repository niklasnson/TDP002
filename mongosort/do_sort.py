import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def initalize_sort(unsorted_list):
    temp = unsorted_list.copy() 
    temp = sorted(temp)
    i = 0 
    while mongo_sort(temp, unsorted_list) == False: 
        print(bcolors.FAIL + "Warning: no match on search result " + str(i) + bcolors.ENDC)
        i = i + 1 

    print(bcolors.OKBLUE + "Whiiie: match on search result " + str(i) + bcolors.ENDC)


def mongo_sort(sorted_list, unsorted_list):
    random.shuffle(unsorted_list) 
    if unsorted_list == sorted_list:
        print(str(unsorted_list) + "==" + str(sorted_list) + "\n")
        return True
    else:
        print(str(unsorted_list) + "=!" + str(sorted_list) + "\n")
        return False

def main():
    unsorted_list = ['python','c','ada','ruby','pascal','basic']
    initalize_sort(unsorted_list)

if __name__ == '__main__':
    main()
