
import sys
from datetime import date


choice_command = raw_input('Hey! buudy! write a new of quit,hmm...?> ')

if choice_command == "q": #here maybe can add several words
	print 'See you later..'
	quit() 
elif choice_command == "y":
	input_content = raw_input('Let\'s write: ')
	save_or_not = raw_input('Do you want to save this dairy? y/n: ')
	if save_or_not == "y":
	    with open('dairy.md','a') as f:
	    	now = date.today()
	        f.write("%s\n\n %s\n\n" %(now, input_content))
            print "Yours dariy has been saved."
	elif save_or_not == "n":
		print "Your dairy has been deleted..."
		quit# here can add  write another one, maybe will use some modules
		    #or defs... cycle?
elif choice_command == "b":
    with open('dairy.md','r') as f:
        old_dairy = f.read()
        print old_dairy 
else:
    print 'Sorry, please use correct command.'

f.close()








#birth = date(1989, 10, 29)
#now = date.today()

#now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

#age = now - birth

#print age.days


