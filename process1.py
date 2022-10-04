from time import sleep
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, request
import string
from pyzwcad import ZwCAD, APoint
import array
import comtypes
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import random
import numpy as np
import json
import requests


class Main():

        def __init__(self) -> None:
            self.driver = webdriver.Firefox()
            self.url = 'https://odoo-r7.gexpertise.fr/web/login'
            self.new_url = 'https://odoo-r7.gexpertise.fr/web?#id=403&model=livrables.actif.client&view_type=form&menu_id=203'
            self.acad = ZwCAD()


        def authentification_Odoo(self):
            self.driver.get(self.url)
            username = self.driver.find_element(By.ID,"login")
            password = self.driver.find_element(By.ID,"password")
            username.send_keys("i.benabdallah@gexpertise.fr")
            password.send_keys("i$XnRR6H*l8d")

        def extract_data_odoo(self):
            button1 = self.driver.find_element(By.XPATH,'//button[@type="submit"]').click()
            #button1.click()   #clicking on the button
            page = self.driver.get(self.new_url)
            # waits for 3 seconds
            sleep(3)
            #*********************ID*************************
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/span[@class='o_field_char o_field_widget o_readonly_modifier o_required_modifier oe_inline']"))
            ) 
            self.ID = element.get_attribute("innerHTML")
            #print('ID', ID)

            #*********************Nom__Livrable*************************
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/h1/span[@class='o_field_char o_field_widget o_required_modifier']"))
            )
            self.nom_livrable = element.get_attribute("innerHTML")
            #print('nom_livrable', nom_livrable)
            #***********************Address****************************
            element1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/div[@class='o_group']/table/tbody/tr/td[2]/a[@class='o_form_uri o_field_widget']"))

            )
            self.address= element1.get_attribute("innerHTML")
            #print('address', address)

            #**********************Nom__du__client**********************
            element2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/div[@class='o_group']/table/tbody/tr/td[2]/a[@class='o_form_uri o_field_widget o_required_modifier']"))
            )
            Nom__du__client= element2.get_attribute("innerHTML")
            self.Nom__du__client = Nom__du__client.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')

            #print('Nom__du__client',Nom__du__client)

            #**********************N° Dossier**********************
            element2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[4]"))
            )
            self.Num_Dossier= element2.get_attribute("innerHTML")
            self.TEXT =  self.Num_Dossier.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
            #print(TEXT)

            #**********************N° Arch**********************
            element2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[5]"))
            )
            Num_Arch= element2.get_attribute("innerHTML")
            self.Num_Arch = Num_Arch.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
            #print(Num_Arch)

            #**********************1er contact**********************
            element2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[6]"))
            )
            element3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[7]"))
            )
            er_contact = element2.get_attribute("innerHTML")
            nom_er_contact = element3.get_attribute("innerHTML")
            self.nom_er_contact = nom_er_contact.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
            #print(er_contact,nom_er_contact)

            #**********************2eme contact**********************
            element2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[8]"))
            )
            second_contact= element2.get_attribute("innerHTML")
            self.second_contact = second_contact.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
            #print(second_contact)

            #**********************3eme contact**********************
            element2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[9]"))
            )
            third_contact= element2.get_attribute("innerHTML")
            self.third_contact = third_contact.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
            #print(third_contact)

            #**********************DETAILED Address**********************
            element2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[12]"))
            )
            self.Full_address= element2.get_attribute("innerHTML")
            #print(Full_address)

            #**********************Mission**********************
            elementmission = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[16]"))

            )
            elementmission1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[19]"))
            )
            elementmission2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[20]"))
            )
            self.Mission1= elementmission.get_attribute("innerHTML")
            self.Mission2= elementmission1.get_attribute("innerHTML")
            self.Mission3= elementmission2.get_attribute("innerHTML")
            #print((Mission1,Mission2,Mission3))

            #**********************Cree__par****************************
            element3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table[@class='o_group o_inner_group']/tbody/tr/td[2]/a[@class='o_form_uri o_field_widget o_readonly_modifier']"))
            )
            self.Cree__par= element3.get_attribute("innerHTML")
            #print('Cree__par',Cree__par)


            #**********************Cree__le*****************************
            element3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table[@class='o_group o_inner_group']/tbody/tr[2]/td[2]/span[@class='o_field_date o_field_widget o_readonly_modifier']"))
            )
            self.Cree__le= element3.get_attribute("innerHTML")
            #print('Cree__le',Cree__le)

            #**********************Cadastre*********************
            element2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[24]"))
            )
            cadastre= element2.get_attribute("innerHTML")
            self.cadastre = cadastre.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '')
            #print(cadastre)

            #**********************Visa Rendu*********************
            element2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/p/span[59]"))
            )
            visa_rendu= element2.get_attribute("innerHTML")
            self.visa_rendu = visa_rendu.replace('<br>', '').replace('&nbsp;', '').replace('&amp;', '').replace('<span>;', '').replace('</span>;', '')
            #print(visa_rendu)
            result=( self.ID, self.nom_livrable,Nom__du__client, self.address, self.Cree__par, self.Cree__le,visa_rendu,cadastre, self.Mission1, self.Mission2, self.Mission3, self.Full_address,Num_Arch, self.Num_Dossier)
            return result
        
        def plotLivrable(self):
                    p= APoint(1653934.9114,8210383.9801,0.00)
                    p = self.acad.model.AddText(self.nom_livrable, p, 1.2)
                    p.Color = 0
                    return p 


        
        def plotCadastre(self):
                p= APoint(1653946.9265,8210369.6057,0.00)
                p = self.acad.model.AddText(self.cadastre, p, 0.8)
                p.Color = 0
                return p 

        



        def plotAddress( self):
                p1 = APoint(1653944.4373,8210377.9012 ,0.000)
                p = self.acad.model.AddText(self.address, p1, 1.3)
                p.Color = 0
                return p


        def plotNote(self):
                p0 = APoint(1653939.2848,8210324.0597 ,0.000)
                p1 = APoint(1653939.6737,8210321.3752 ,0.000)
                p2 =APoint(1653939.9631,8210317.9016,0.000)
                p0 = self.acad.model.AddText("Note: ", p0,1.0)
                p0.Color = 0
                p = self.acad.model.AddText("Calcul réalisé à partir des relevés effectués en"+self.Cree__le+"par GEXPERTISE CONSEIL ",p1,0.5)
                p.Color = 0
                p1 = self.acad.model.AddText( "les affectations des locaux  correspondent aux occupations apparentes le jour du mesurage.",p2,0.5)
                p1.Color = 0
                return p 
        

        def plotDate_RESP(self):
                p1 = APoint(1653953.3782,8210308.7335 ,0.000)
                p = self.acad.model.AddText("Date :"+self.Cree__le +"- Resp :" +self.Cree__par, p1, 0.6)
                p.Color = 0
                return p 

        def plotID(self):
                p1 = APoint()
                p = self.acad.model.AddText(self.ID)
                return(p)

        def plotNum_dossier(self):
                p= APoint(1653951.8446,8210310.2712,0.00)
                p = self.acad.model.AddText(self.Num_Dossier, p, 0.7)
                p.Color = 0
                return p 

        def plotNum_Archive(self):
                p= APoint(1653951.9483,8210308.6641,0.00)
                p = self.acad.model.AddText(self.Num_Arch, p, 0.7)
                p.Color = 0
                return p

                

        def plot(self):
                
                print("Model", self.acad.model ) 
                print("ModelSpace", self.acad.doc.ModelSpace)
                print("Document", self.acad.ActiveDocument) 
                print ('Current', self.acad.doc.Name)


                #  _________Lancer COMMANDE pour passer vers une autre presentation_________
                command_str = 'aller sur : M2XX_E0_(SDP) '
                #print (command_str)
                #self.acad.doc.SendCommand(command_str)

                #resp = requests.get('http://127.0.0.1:5000/address')
                #txt = resp.content
                #print(txt)


                
               # api_url = 'http://127.0.0.1:5000'
               # r = requests.post(url=api_url)
                # print(r.status_code)
                # print(r.reason)
                # print(r.text)


                #  ________________________EXTRACT all TEXT _______________________________
                for text in self.acad.iter_objects('Text'): # extraire data de type text
                        # print('text: %s at: %s' % (text.TextString, text.InsertionPoint))
                        text.InsertionPoint = APoint(text.InsertionPoint) 

                #  ________________________PLOT_____________________________________________
                #p = plot( )     
                
                
                #acad.app.ZoomExtents()
                self.plotLivrable()
                self.plotAddress()
                #plotDate_RESP()
                self.plotNote()
                self.plotCadastre()
                self.plotNum_Archive()
                self.plotNum_dossier()
                print ("DONE" )
        def API(self):
                url = 'http://127.0.0.1:5000'
                app = Flask(__name__)
                app.config["DEBUG"] = True
                @app.route('/', methods=['GET'])
                def resultat():
                  return '{} {} {} {} {} {} {} {} {}'.format(self.nom_livrable, self.address, self.Nom__du__client, self.Cree__par, self.Cree__le, self.Num_Dossier, self.Num_Arch, self.visa_rendu, self.cadastre)
             
                @app.route('/', methods=['POST'])
                def extract():
                   print("flask")
                   data = request.get_data()
                   print(data)
                  # print(request.get_json())
                   return "", 200
 
                app.run()



        def run(self):
                self.authentification_Odoo()
                self.extract_data_odoo()
                self.plot()
                self.API()


                
                
        
                





if __name__ == '__main__':
    extract = Main()
    extract.run()
   