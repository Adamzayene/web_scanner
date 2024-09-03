import webbrowser
import whois
import socket
from bs4 import BeautifulSoup
import requests
from requests import get
import re
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import argparse
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def validate_url(url):
    """Ensure the URL starts with http:// or https://."""
    if not re.match(r'http[s]?://', url):
        url = 'https://' + url
    return url

def fetch_robots(url, open_in_browser=False):
    """Fetch and display the robots.txt file for a given URL."""
    url = validate_url(url)
    if open_in_browser:
        webbrowser.open(url + '/robots.txt')
    else:
        response = get(url + '/robots.txt')
        print(Fore.GREEN + response.text)

def fetch_sitemap(url, open_in_browser=False):
    """Fetch and display the sitemap.xml file for a given URL."""
    url = validate_url(url)
    if open_in_browser:
        webbrowser.open(url + '/sitemap.xml')
    else:
        response = get(url + '/sitemap.xml')
        print(Fore.GREEN + response.text)

def fetch_whois_info(domain):
    """Fetch and display WHOIS information for a given domain."""
    domain_info = whois.whois(domain)
    print(Fore.YELLOW + str(domain_info))

def fetch_ip(url):
    """Retrieve and display the IP address for a given URL."""
    url = validate_url(url)
    hostname = url.split("://")[-1].split("/")[0]
    try:
        ip = socket.gethostbyname(hostname)
        print(Fore.CYAN + f"{hostname} = {ip}")
    except socket.gaierror as e:
        print(Fore.RED + f"Error retrieving IP: {e}")

def extract_emails(url):
    """Extract and display email addresses from a given webpage."""
    url = validate_url(url)
    response = get(url).text
    emails = re.findall(r'\S+@\S+', response)
    for email in emails:
        print(Fore.MAGENTA + email)

def extract_phone_numbers(url):
    """Extract and display phone numbers from a given webpage."""
    url = validate_url(url)
    response = get(url).text
    phone_numbers = re.findall(r'\+?\d[\d -]{8,}\d', response)
    for number in phone_numbers:
        parsed_number = phonenumbers.parse(number, None)
        print(Fore.MAGENTA + f"{number} = {geocoder.description_for_number(parsed_number, 'en')} - {carrier.name_for_number(parsed_number, 'en')}")

def extract_links(url):
    """Extract and display all links from a given webpage."""
    url = validate_url(url)
    response = get(url)
    bs = BeautifulSoup(response.text, "html.parser")
    for link in bs.find_all('a'):
        print(Fore.BLUE + link.get('href'))

def main():
    banner = f"""
{Fore.RED}              _                                             
{Fore.RED}__      _____| |__     {Fore.GREEN}___  ___ __ _ _ __  _ __   ___ _ __  
{Fore.RED}\ \ /\ / / _ \ '_ \   {Fore.GREEN}/ __|/ __/ _` | '_ \| '_ \ / _ \ '__| 
{Fore.RED} \ V  V /  __/ |_) |  {Fore.GREEN}\__ \ (_| (_| | | | | | | |  __/ |    
{Fore.RED}  \_/\_/ \___|_.__/___{Fore.GREEN}|___/\___\__,_|_| |_|_| |_|\___|_|    
{Fore.RED}                 |_____{Fore.GREEN}|                                   
    """
    print(banner)
    print(Fore.CYAN + Style.BRIGHT + "Developed by Adam Zayene(Black_Shadow)")

    parser = argparse.ArgumentParser(
        description=Fore.YELLOW + 'A simple web scanner tool for various website analysis operations.',
        epilog=Fore.CYAN + 'Use the options to perform different analyses on the specified URL.\n\nDeveloped by Adam Zayene'
    )
    
    # Adding commands
    parser.add_argument('-u', '--url', metavar='URL', type=str, required=True,
                        help=Fore.WHITE + 'Specify the target URL for the operations (e.g., www.example.com).')
    parser.add_argument('-r', '--robots', action='store_true',
                        help=Fore.WHITE + 'Check the robots.txt file of a website and display it in the terminal.')
    parser.add_argument('-b', '--browser', action='store_true',
                        help=Fore.WHITE + 'Open robots.txt or sitemap.xml in a web browser instead of displaying it in the terminal.')
    parser.add_argument('-s', '--sitemap', action='store_true',
                        help=Fore.WHITE + 'Access the sitemap.xml file of a website and display it in the terminal.')
    parser.add_argument('-w', '--whois', action='store_true',
                        help=Fore.WHITE + 'Get information about a domain using WHOIS lookup.')
    parser.add_argument('-i', '--get-ip', action='store_true',
                        help=Fore.WHITE + 'Retrieve the IP address of the specified website.')
    parser.add_argument('-e', '--extract-emails', action='store_true',
                        help=Fore.WHITE + 'Extract and display email addresses found on the specified webpage.')
    parser.add_argument('-p', '--extract-phone', action='store_true',
                        help=Fore.WHITE + 'Extract and display phone numbers found on the specified webpage.')
    parser.add_argument('-l', '--extract-links', action='store_true',
                        help=Fore.WHITE + 'Extract and display all hyperlinks found on the specified webpage.')
    parser.add_argument('--all', action='store_true',
                        help=Fore.WHITE + 'Run all operations available for the specified URL.')

    args = parser.parse_args()

    # If --all is specified, set all other flags to True
    if args.all:
        args.robots = True
        args.sitemap = True
        args.whois = True
        args.get_ip = True
        args.extract_emails = True
        args.extract_phone = True
        args.extract_links = True

    # Process commands based on flags
    if args.robots:
        fetch_robots(args.url, args.browser)
    if args.sitemap:
        fetch_sitemap(args.url, args.browser)
    if args.whois:
        fetch_whois_info(args.url)
    if args.get_ip:
        fetch_ip(args.url)
    if args.extract_emails:
        extract_emails(args.url)
    if args.extract_phone:
        extract_phone_numbers(args.url)
    if args.extract_links:
        extract_links(args.url)

if __name__ == "__main__":
    main()
