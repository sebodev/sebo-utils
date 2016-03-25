

def new(tasks_to_run):
    try:
        ans = raw_input('\nType t and then hit enter if \n' \
                        ' a) This is for a template \n' \
                        ' b) This is for a starter site\n' \
                        ' c) You would like to create a custom site, but you don\'t plan on doing any dev work on the site\n' \
                        'Otherwise, type c \n' \
                        ).lower()[0]
        if ans == 't':
            tasks_to_run.wordpress = True
            print('A Chrome window will open shortly')
        elif ans == 'c':
            ans = raw_input("Do you need to set up the wordpress site for this custom project. Type yes or no").lower()[0]
            if ans == 'y':
                tasks_to_run.wordpress = True
            ans = raw_input("Do you need to create the _s theme. This will create it on both the webfaction server, and on your computer. Type no if the theme already exists on webfaction. Type yes or no").lower()[0]
            if ans == 'y':
                tasks_to_run.new_s_project = True
            else:
                ans = raw_input("In that case the theme must already exist on webfaction, and we just need to copy it to this computer. Type yes or no").lower()[0]
                if ans == 'y':
                    tasks_to_run.existing_s_project = True
                else:
                    print("I give up. I have no idea what you want to do. Type sebo --help for a full list of options")
        else:
            print('Fine, just ignore my instructions of typing t or c. I\'m going to ignore you too')
    except IndexError:
        raise Exception('\n\n  I didn\'t get a valid response from you :( ')
