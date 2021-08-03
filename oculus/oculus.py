#!/usr/bin/python3
import argparse
import os
import sys
sys.path.append('__init__')
import get_ip as ad
import file_mg as file 
from art import *
from termcolor import colored

SEC_PATH = "/usr/bin/"

def print_banner():

	print(colored(text2art ("OCULUS"),'cyan'))
	print(colored("|_ Version :", 'red',attrs=['bold']),colored(" 1.0#beta","cyan"))
	print(colored("|_ Authors :", 'red',attrs=['bold']),colored(" Ilham & Chaymae","cyan"))
	print(colored("|_ Usage :",'red',attrs=['bold']),colored(" python3 oculus.py [options]","cyan"))

def args_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', help='valid url or ip of the target')
	return parser.parse_args()
def main():
	try:	
		args = vars(args_parser())
		url= args['u']
		path_dir ="reports/" + url
		file.create_dir(path_dir)
		ip = ad.get(url)
		print('The IP Address is :',ip)
		os.system(SEC_PATH  + 'qterminal -e "nmap -A '+ip+' -p- -o '+path_dir+'/nmap.txt"') # This will call nmap to scan for open ports on the target!
		os.system(SEC_PATH  + 'qterminal -e "nikto +h '+url+' -output '+path_dir+'/nikto.txt"') # This will run nikto to scan the target from top 10 owasp vulns!
		os.system(SEC_PATH  + 'qterminal -e "gobuster -u '+url+ ' -w /home/eddie/Bureau/tools/directory-list-2.3-medium.txt /dirsearch.txt"') # This will run gobuster against the target to find hidden folders and files in the server (in will work if there is a web server) !
		os.system(SEC_PATH  + 'qterminal -e "wpscan --url '+ip+' /wpscan.txt"') # In case of testing on a Wordpress! this will run Wpscan tool and start enumiration on the target!
		os.system(SEC_PATH  + 'qterminal -e "ftp '+ip+'"')  # this will open ftp connection with the target and u need to test for anonymous coneection!
	except ValueError as e:
		print(e)
	except:
		print("failed")
	
	


if __name__ == '__main__':

	print_banner()
	print("\n")
	if sys.version_info.major < 3 :
		print("use python3" )
		exit(0)
	main()
	
