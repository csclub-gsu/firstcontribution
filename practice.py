from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import re
import json

# url = "https://oscar.gatech.edu/pls/bprod/wwtraneq.P_TranEq_Nme"
url = "https://www.gosolar.gsu.edu/bprod/bwckschd.p_disp_dyn_sched"

# Create an instance of ChromeOptions
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
# Create a new Chrome browser instance using the options we set above

driver = webdriver.Chrome(options=opts,executable_path="/jenif/Documents/Projects/Python/chromedriver")

driver.get(url)
print()
driver.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr/td/select/option[2]").click() # select semester
driver.find_element(By.XPATH, "/html/body/div[3]/form/input[2]").click() # click the submit button
driver.find_element(By.XPATH, "/html/body/div[3]/form/table[1]/tbody/tr[1]/td[2]/select/option[2]").click() # click the Bachelor's button
driver.find_element(By.XPATH, "/html/body/div[3]/form/table[1]/tbody/tr[2]/td[2]/select/option[55]").click() # click CS
driver.find_element(By.XPATH, "/html/body/div[3]/form/table[1]/tbody/tr[2]/td[2]/select/option[126]").click() # click math
driver.find_element(By.XPATH, "/html/body/div[3]/form/input[12]").click() # search classes
test = driver.find_elements(By.CLASS_NAME, "dddefault") # search classes
print(test)
print('Yay')

x = driver.page_source

f = open("classes.csv", "a")
errorfile = open("errors.csv", "a")
#headers = {'Content-Type': 'application/json'}
#params = {'p_term': '202301', 'sel_levl': 'US', 'sel_subj': 'CSC', 'sel_camp': '%', 
#'sel_ptrm': '%', 'sel_instr': '%', 'sel_attr': '%', 'begin_hh': '0',
#'begin_mi': '0', 'begin_ap': 'a', 'end_hh': '0', 'end_mi': '0',
#'end_ap': 'a'}
#p = json.dumps(params)
#x = requests.post(url, data = params)
#params = {'p_term': '202301', 'sel_levl': 'US', 'sel_subj': 'CSC', 'sel_camp': '%', 
#'sel_ptrm': '%', 'sel_instr': '%', 'sel_attr': '%', 'begin_hh': '0',
#'begin_mi': '0', 'begin_ap': 'a', 'end_hh': '0', 'end_mi': '0',
#'end_ap': 'a'}
#x = requests.post(url, params = params)

clean = re.compile('<.*?>')
text = re.sub(clean, '', x)
text = re.split("\n\n\n\n", text)
location = re.split("\n",text[7])#[-1]
location2 = re.split("\n",text[12])#[-1]
location3 = re.split("\n",text[13])#[-1]
location4 = re.split("\n",text[14])#[-1]
location = location.replace(",", " ")
location = location.replace("&nbsp;", " ")
text = text[9]
classes = re.split("\n\n\n&nbsp;\n\n\n",text)