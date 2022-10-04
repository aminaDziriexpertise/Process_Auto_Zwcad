from time import sleep
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask




driver = webdriver.Firefox()
url = 'https://odoo-r7.gexpertise.fr/web/login'
new_url = 'https://odoo-r7.gexpertise.fr/web?#id=403&model=livrables.actif.client&view_type=form&menu_id=203'
driver.get(url)
username = driver.find_element(By.ID,"login")
password = driver.find_element(By.ID,"password")
username.send_keys("i.benabdallah@gexpertise.fr")
password.send_keys("i$XnRR6H*l8d")

# getting the button by class name
#button = driver.find_element((By.XPATH, ".//div[@id='wrapwrap']/main/div[@class='oe_website_login_container']/form[@class='oe_login_form']/div[@class='clearfix oe_login_buttons text-center mb-1 pt-3']/button[@class='btn btn-primary btn-block']"))
button1 = driver.find_element(By.XPATH,'//button[@type="submit"]').click()
# clicking on the button
#button1.click()

print("time out")
    # Do some stuff
def getMeG():
      pass # do nothing
    # This is not working 
sleep(3)
page = driver.get(new_url)
    # Do more Stuff
def getMeV():
    pass # do nothing
    # waits for 3 seconds
sleep(3)

#*********************ID*************************
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/span[@class='o_field_char o_field_widget o_readonly_modifier o_required_modifier oe_inline']"))
    ) 
ID = element.get_attribute("innerHTML")
print('ID', ID)

#*********************Nom__Livrable*************************
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/h1/span[@class='o_field_char o_field_widget o_required_modifier']"))
    )
nom_livrable = element.get_attribute("innerHTML")
print('nom_livrable', nom_livrable)
#***********************Address****************************
element1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/div[@class='o_group']/table/tbody/tr/td[2]/a[@class='o_form_uri o_field_widget']"))
        
    )
address= element1.get_attribute("innerHTML")
print('address', address)

#**********************Nom__du__client**********************
element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/div[@class='o_group']/table/tbody/tr/td[2]/a[@class='o_form_uri o_field_widget o_required_modifier']"))
    )
Nom__du__client= element2.get_attribute("innerHTML")
Nom__du__client = Nom__du__client.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')

print('Nom__du__client',Nom__du__client)


#**********************N° Dossier**********************
element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[4]"))
    )
Num_Dossier= element2.get_attribute("innerHTML")
TEXT = Num_Dossier.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
print(TEXT)

#**********************N° Arch**********************
element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[5]"))
    )
Num_Arch= element2.get_attribute("innerHTML")
Num_Arch = Num_Arch.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
print(Num_Arch)

#**********************1er contact**********************
element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[6]"))
    )
element3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[7]"))
    )
er_contact = element2.get_attribute("innerHTML")
nom_er_contact = element3.get_attribute("innerHTML")
nom_er_contact = nom_er_contact.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
print(er_contact,nom_er_contact)

#**********************2eme contact**********************
element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[8]"))
    )
second_contact= element2.get_attribute("innerHTML")
second_contact = second_contact.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
print(second_contact)

#**********************3eme contact**********************
element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[9]"))
    )
third_contact= element2.get_attribute("innerHTML")
third_contact = third_contact.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
print(third_contact)

#**********************DETAILED Address**********************
element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[12]"))
    )
Full_address= element2.get_attribute("innerHTML")
print(Full_address)

#**********************Mission**********************
elementmission = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[16]"))
       
    )
elementmission1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[19]"))
    )
elementmission2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[20]"))
    )
Mission1= elementmission.get_attribute("innerHTML")
Mission2= elementmission1.get_attribute("innerHTML")
Mission3= elementmission2.get_attribute("innerHTML")
print((Mission1,Mission2,Mission3))

#**********************Cree__par****************************
element3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table[@class='o_group o_inner_group']/tbody/tr/td[2]/a[@class='o_form_uri o_field_widget o_readonly_modifier']"))
    )
Cree__par= element3.get_attribute("innerHTML")
print('Cree__par',Cree__par)


#**********************Cree__le*****************************
element3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table[@class='o_group o_inner_group']/tbody/tr[2]/td[2]/span[@class='o_field_date o_field_widget o_readonly_modifier']"))
    )
Cree__le= element3.get_attribute("innerHTML")
print('Cree__le',Cree__le)

#**********************Cadastre*********************
element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[24]"))
    )
cadastre= element2.get_attribute("innerHTML")
cadastre = cadastre.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
print(cadastre)

#**********************Visa Rendu*********************
element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[59]"))
    )
visa_rendu= element2.get_attribute("innerHTML")
visa_rendu = visa_rendu.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '').replace('<span>;', '').replace('</span>;', '')
print(visa_rendu)





def return_data():
    result=(ID,nom_livrable,Nom__du__client,address,Cree__par,Cree__le,visa_rendu,cadastre,Mission1,Mission2,Mission3,Full_address,Num_Arch,Num_Dossier)
    return result