# Kyle Haston
# Feb 2020
# I want a script to add some information to a file on my server on a daily basis.

from paramiko import *
import credentials


def main():
    # Open the local file, and read some info.
    print('asdf')
    with open('some_data.txt','r') as in_file:
        with open('../../PG-Site-Forecast-Buddy/PG-Site-Forecast-Buddy/site_data.py','w') as out_file:
            data = in_file.read()
            print(data)

    # Write it to the other file.
    print('sadf')

    # Commit the other file.
    print('qwer')


if __name__ == "__main__":
    main()
