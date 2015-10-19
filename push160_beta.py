import csv
from sys import argv
from os.path import exists

script, csv_file, copy_file = argv

exists(copy_file)

config = open(copy_file,'w')

head = """
[core]
\trepositoryformatversion = 0
\tfilemode = true
\tbare = false
\tlogallrefupdates = true
\tignorecase = true
\tprecomposeunicode = true
[remote \"OMOOC2py\"]
"""
config.write(head)

with open(csv_file, 'rU') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        config.write("\turl = %s/OMOOC2py.git\n" %row['username'])

end = "\tfetch = +refs/heads/*:refs/remotes/OMOOC2py/*"
config.write(end)

print "done"

#copy_file.close()        
