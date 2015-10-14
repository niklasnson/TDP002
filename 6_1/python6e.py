import getopt, sys, os, re

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def load_file(filename): 
    temp = ''
    with open(filename) as file:
        for line in file: 
            temp += line
    return temp

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def write_file(filename, content, suffix=None): 
    target = open(set_filename(filename, suffix), 'w')
    target.truncate()
    target.write(content)

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def set_filename(filename, suffix=None):
    if suffix != None: 
        temp = os.path.splitext(filename)
        filename = temp[0] + "." + suffix
    return filename 

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def load_directory(directory, filtr=None): 
    temp = []
    for (dir, _, files) in os.walk(directory):
        for f in files:
            if filtr != None and f.endswith(filtr): 
                path= os.path.join(dir, f)
                temp.append(path)
            elif filtr == None:
                path= os.path.join(dir, f)
                temp.append(path)
    return temp

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def process_file(source, license, suffix=None): 
    if suffix == None: 
        print('processing file: ', source)
    else: 
        print('processing file: ', source, ">", set_filename(source, suffix))
    content = update_source(load_file(source), license)
    write_file(source, content, suffix)

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def process_directory(sources, license, suffix=None): 
    for source in sources: 
        process_file(source, license, suffix)

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def update_source(source, license): 
    license = "BEGIN COPYRIGHT" + license + "END COPYRIGHT"     
    return re.sub(r'BEGIN COPYRIGHT[\s\S]*?END COPYRIGHT', license, source)

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def usage(): 
    print('\n')
    print('python6e')
    print('Usage: python python6e.py [switches] [filename or folder]')
    print('   --license= [apache|gnu|mit]')
    print('   --filter= [file suffix (.py)]')
    print('   --suffix= [file suffix (.tmp)]')
    print('\nExample: python python6e.py --license=apache --filter=py --suffix=tmp testfiles')
    print('       : python python6e.py --l=apache testfiles/test_a.py')

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def main(): 
    try: 
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "license=", "filter=", "suffix="])  #opts = options och args = filen in. 
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    suffix= None
    filtr= None
        
    for o, a in opts: 
        if o in ('--h', '--help'):
            usage()
            sys.exit()
        elif o in ('--f', '--filter'):
            filtr= str(a)
        elif o in ('--l', '--license'): 
            try: 
                licence = load_file('licenses/'+a+'.text')
            except: 
                print('error: unable to read the license file') 
                sys.exit()
        elif o in ('--s', '--suffix'):
            suffix= a
        
    if os.path.isfile(args[0]):
        process_file(args[0], licence, suffix)
    else:
        cue = load_directory(args[0], filtr)
        process_directory(cue, licence, suffix)
        
""" ------------------------------------------------------------------------------------------------------------------------------------ """
    
if __name__ == '__main__':
    main()    
