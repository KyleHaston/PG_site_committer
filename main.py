# Kyle Haston
# Feb 2020
# I want a script to add some information to a file on my server on a daily basis.

import datetime
import os
import sys


def main():
    # Open the input file, and read some info.
    with open('some_data.txt', 'r') as in_file:
        with open('output.txt', 'a') as out_file:
            data = in_file.readlines()

            # Get the date.
            today_str = str(datetime.datetime.today()).split()[0]
            print('    today: ' + today_str)

            # If there is data to be written today, write it to the other file.
            for line in data:
                if today_str in line:
                    print('    writing this to the file: ' + line)
                    out_file.write(today_str + '\n')

                    print('    commit the other file: ')  # Commit the other file.
                    os.system('git pull')
                    os.system('git commit -am "commit for ' + line + '"')
                    os.system('git push')
                    sys.exit(0)

                else:
                    print('    not writing anything today!')


if __name__ == "__main__":
    main()
