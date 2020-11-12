#!/usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import keyboard
import random
import time

temp = "36."+str(random.randrange(10))
print(temp)

class SendTempException(Exception):
	pass


def sendtemp(url,email,password):
	try:
		options = webdriver.ChromeOptions()
		options.add_argument("--incognito")
		options.add_argument('--ignore-ssl-errors=yes')
		options.add_argument('--ignore-certificate-errors')
		driver = webdriver.Chrome(options = options)
		driver.get(url)
		
		time.sleep(0.5)
		driver.find_element_by_id("i0116").send_keys(email)
		driver.find_element_by_id("idSIButton9").click()
		time.sleep(0.5)
		driver.find_element_by_id("i0118").send_keys(password)
		driver.find_element_by_id("idSIButton9").click()
		WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID, 'idSIButton9')))
		time.sleep(0.5)
		driver.find_element_by_id("idSIButton9").click()
		WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, '//*[@spellcheck="true"]')))
		time.sleep(0.5)
		temper = driver.find_element_by_xpath("//*[@spellcheck='true']")
		
		temper.send_keys(temp)
		
		driver.find_element_by_xpath('//*[@type="checkbox"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@class="office-form-theme-primary-background office-form-theme-button office-form-bottom-button button-control light-background-button __submit-button__"]').click()
		driver.close()
		driver.quit()
	except:
		print("error in sendtemp")
		driver.close()
		driver.quit()
		raise SendTempException("Probably timeout")
	return 0

def lup(url,email,password):
	if keyboard.is_pressed("q"):
		return 0
	try:
		sendtemp(url,email,password)
	except SendTempException as e:
		print("error in lup:")
		print(e)
		lup(url,email,password)
		return 0
	finally:
		open("log.txt","w").write("Logged temperature to "+url+" at "+ str(datetime.datetime.now()) + " as " + email + "\n")
		return 0



import sys, getopt
import getpass

def main(argv):
	url = ""
	password = ""
	email = ""
	showpass = False
	try:
		opts, args = getopt.getopt(argv,"hU:e:p:S",["url=","pass=","email=","showpass"])
	except getopt.GetoptError:
		print('first.py -U <url> -e <email> -p <password> -S')
		sys.exit(2)
	for opt, arg in opts:
		if opt=="-h":
			print('help: first.py -U <url> -e <email> -p <password> -S')
			sys.exit()
		elif opt in ("-U","--url"):
			url = arg
		elif opt in ("-e","--email"):
			email = arg
		elif opt in ("-p","--password"):
			password = arg
		elif opt in ("-S","--showpass"):
			showpass = True
	if url == "":
		print('first.py -U <url> -e <email> -p <password> -S')
		sys.exit(2)

	if (password == ""):
		password = getpass.getpass()
	print()
	print("running temperature logger at url "+url)
	print("with email "+email)
	if showpass:
		print("with password "+password)
	else:
		print("password was hidden from output")

	lup(url,email,password)


if __name__ == "__main__":
	main(sys.argv[1:])
