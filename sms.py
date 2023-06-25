import os
import time
from termcolor import colored
import requests
import platform


def main():
    print(colored(
        """
    @@@@@@@@@@@@@@@@@@@@@@@@@@**********@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@*****************************@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@**************************************@@@@@@@@@@@@
    @@@@@@**************@@@@@@@@@@@@@@@@@@@@@@@**************@@@@@
    @@@***    *****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*****    ***@@
    @@***      **@@@@@@@@@@*****************@@@@@@@@@@**      **@@
    @@@****  ***@@@@@@***************************@@@@@@***  ***@@@
    @@@@@@@@@@@@*************@@@@@@@@@@@@@*************@@@@@@@@@@@
    @@@@@@@@@@***    ***@@@@@@@@@@@@@@@@@@@@@@@***    **@@@@@@@@@@
    @@@@@@@@@@@***  ***@@@@@@@***********@@@@@@@**   ***@@@@@@@@@@
    @@@@@@@@@@@@@@*@@@@@***********************@@@@*@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@**    *****@@@@@*****    **@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@***  ***@@@@@@@@@@@***  **@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@*******@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@*********@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@********@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    **@@@**@@@@@@@@@@@@@@@@@@**@@@@@@*@@@@@*@@@@@@@@@@@@@@@@@*@@@@
    **@@@**@*@@@*@*****@@******@@*****@@@@****@*****@@*****@@*****
    **@@@**@@*@*@@*@@@**@*@@@**@**@@@*@@@@@**@@*@***@@*@@@@@@*@@@*
    **@@@**@@@**@@*@***@@*@@@**@****@*@@@@@***@*****@@*****@@*@@@*
    @@@@@@@@**@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    Created by Hussain Humaidan
    Uploaded by Hyprid tech
    We are not responsible of any illegal action
    """, 'blue'))

    time.sleep(1)

    print('1: Send sms')
    print('2: Help!')
    print('3: Youtube Channel')

    choices = input("\nPlease choice: ")

    if choices == "1":
        os.system('clear')
        time.sleep(1)
        smsnumb = input("Input the number of the target: ")
        message = input("Please input the message: ")

        resp = requests.post('https://textbelt.com/text', {
            'phone': f'{smsnumb}',
            'message': f'{message}',
            'key': 'textbelt',
        })

        print(resp.json())
        time.sleep(3)
        return main()

    elif choices == "2":
        os.system("clear")
        time.sleep(1)
        lines = "=========================================================================================="
        print(
            "Your phone number was not provided in E.164 format: you need to input the country code ex.+91"
        )
        print(lines)
        print(
            "Only one test text message is allowed per day: you can't send more than one message per day, however you could use vpn"
        )
        print(lines)
        print(
            "Anything more please report an issue at github"
        )
        print(lines)
        print(
            "Follow the video to know more about the tool :)\nhttps://youtu.be/dSdBRrozFBc"
        )

    elif choices == "3":
        os.system("clear")
        time.sleep(1)
        time.sleep(1)
        print("\nhttps://www.youtube.com/@hybrid-technology\n\nHave fun legally :)")


main()