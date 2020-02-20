# Kyle Haston
# Feb 2020
# I want a script to add some information to a file on my server on a daily basis.

import datetime
from paramiko import *
import credentials


def main():
    # Open the local file, and read some info.
    print('asdf')
    with open('some_data.txt','r') as in_file:
        # with open('../../PG-Site-Forecast-Buddy/PG-Site-Forecast-Buddy/site_data.py','w') as out_file:
        with open('site_data.py','w') as out_file:
            data = in_file.readlines()

            # Get the date.
            today_str = str(datetime.datetime.today()).split()[0]
            print('    today: ' + today_str)


            # Write it to the other file.
            for line in data:
                if today_str in line:
                    print('    writing this to the file: ' + line)

            print('    done writing!')

            # Commit the other file.
            print('    commit the other file: ')


if __name__ == "__main__":
    main()
