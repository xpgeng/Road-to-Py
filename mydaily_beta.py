# _*_ coding:utf-8 _*_
'''
Mydaily version2.0
根据大妈的讲课添加了一些函数
修改了日期的表达方式

'''
from time import gmtime, strftime

def main():

#get the commands of  quit, write or check the past
    choice_command = raw_input('Hey! buddy!\nq:quit\nw:write a new diadry\np:check the past diaries?\n> ')

    if choice_command == "q": #here maybe can add several words
	    print 'See you later..'
	    quit() 
#write the diary
    elif choice_command == "w":
	    input_content = raw_input('Let\'s write: ')
	    save_or_not = raw_input('Do you want to save this diary? y/n: ')
	
	    if save_or_not == "y":
	        with open('diary.md','a') as f:
	    	    now = strftime("%Y年%m月%d日 %H:%M:%S", gmtime())
	            f.write("%s\n\n %s\n\n" %(now, input_content))
                print "Yours diary has been saved."
	    elif save_or_not == "n":
		    print "Your diary has been deleted..."
		    quit# here can add  write another one, maybe will use some modules
		    #or defs... cycle?
#show all the past diaries
    elif choice_command == "p":
        with open('diary.md','r') as f:
            old_dairy = f.read()
            print old_dairy 
    else:
        print 'Sorry, please use correct command.'

    f.close()

if __name__=="__main__":
    main()



