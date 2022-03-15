import os
import time
from termcolor import colored
import requests
import sys


def main():
    def logo():
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

    logo()

    time.sleep(1)

    print('1: Send sms')
    print('2: Help!')
    print('3: Youtube Channel')

    choices = input("\nPlease choice: ")

    def SMS():
        os.system('clear')
        time.sleep(1)
        logo()
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

    if choices == "1":
        SMS()

    elif choices == "2":
        os.system("clear")
        time.sleep(1)
        logo()
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
            "Else: please contact hyprid tech in github or youtube"
        )
        print(lines)
        print(
            "Follow the video to know more about the tool :)"
            "*Please put the video link here Hussain*"
        )


    elif choices == "3":
        os.system("clear")
        time.sleep(1)
        logo()
        time.sleep(1)
        print("\nhttps://www.youtube.com/channel/UC8GSC-wXvPiMSaQ8y6dltzQ\n\nHave fun legally :)")


main()
