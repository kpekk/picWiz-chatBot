#!/usr/bin/env python
# coding: utf-8

# LTAT.01.003 Tehisintellekt (2021 sügis)
# Kodutöö nr 7. Piltitöötlus - juturobot

import re

# Roboti kirjeldus, kasutuspiirangud ===================================
"""
Robot puhub kasutajaga juttu ja - kui kasutaja õigesti märku annab - suudab muuta ning
töödelda kasutaja poolt ette antud pilti / pilte.
TODO VAJA TÄIENDADA
"""
# ======================================================================


'''
Mida robot kõik teha võiks (OK = koodi lisatud, NOK = mingi mure):

* morfoloogilised teisendused ? (praks 11)
    * pildi kulutamine (erosion)
    * pildi paisutamine (dilation)
    * servade leidmine (gradient)
* väiksemad muudatused (praks 11)
    * OK heledamaks / tumedamaks tegemine (praks 12)
    * OK kontrasti muutmine (praks 12)
    * värvide muutmine (praks 12)
        * lipuvärvid
    * OK negatiiv (praks 12)
    * OK pildi pööramine (rotation)
    * NOK servade lõikamine (crop) (tf selle ja zoomi vahe on?????)
    * NOK mingi osa suurendamine (zoom) https://stackoverflow.com/questions/69050464/zoom-into-image-with-cv2
    * OK nihutamine (translation)
    * OK perspektiivimuutus (getPerspectiveTransform) 
* objektide leidmine
    * OK mallide leidmine (leitud mall / kujund highlightida)
        * mall peab olema projektikaustas
        * tekstituvastus?
    * OK keerulisemate objektide leidmine (haar cascade, praks 11)
        * silmad, näod, loomad vms
        * peab netist sobivad objektid leidma, ise defineerida raske

* üldine töökäik
    * kasutaja viskab mingi tsaukitsau lause botile, kui bot sealt mingeid keyworde ei tuvasta ss ütleb et fuck off
    * kui mingid keywordid tuvastatakse, küsitakakse kasutajalt, mida ta täpsemalt teha sooviks
        * seda pole vb vaja siis teha kui keywordiks ongi nt "negatiiv"
    * peale kasutaja soovi teada saamist küsitakse mis pildiga ta seda toimingut teha sooviks
    * kui toiming tehtud, küsib kas kasutaja soovib jätkata?
        * see toimuks mingi big ass while loopi sees
'''


def main():

    # robot teretab kasutajat ja tutvustab end
    print("Tere! Mina olen juturobot Juta Ulvina Triinu Terminaator (JUTT).")
    print("Oskan Sinu etteantud pilte töödelda.")
    print("Mida sa täpsemalt oma pildiga teha sooviksid? Spikri jaoks sisesta lihtsalt sõna 'spikker'")
    # TODO lisa menüü (kui kasutaja sisestab 'spikker')

    # juturobot töötab, kuni kasutaja hüvasti jätab
    while True:

        # küsime iga tsükli alguses kasutaja sisendit
        userinput = input(": ")

        #kasutaja jätab hüvasti============================================================
        goodbye = ["head aega", "headaega", "hüvasti", "adjöö", "goodbye", "lõpetame", "bye"]
        if any(word in userinput for word in goodbye):
            # abi saime siit https://stackoverflow.com/questions/3271478/check-list-of-words-in-another-string
            print("Oli meeldiv vestlus, hüvasti, m'lady!")
            return False

        #kasutaja ei jäta hüvasti==========================================================

        # väiksemad muudatused=============================

        # pildi heledamaks muutmine
        if re.search("heledam|liiga tume",userinput):
            print("siin teeme pildi heledamaks")

        # pildi tumedamaks muutmine
        elif re.search("tumedam|liiga hele",userinput):
            print("siin teeme pildi tumedamaks")

        # pildi kontrasti muutmine
        elif re.search("kontrast|udune",userinput):
            print("siin tegeleme kontrastiga")

        # pildi negatiivi tegemine
        elif re.search("negatii|invert",userinput):
            print("siin teeme pildi tumedamaks")

        # pildi pööramine
        elif re.search("pööra|rotate|rotateer|keera",userinput):
            # otsi siin uesti, äkki kasutaja ütles juba kuhu suunas ja palju pöörata tahab
            print("siin teeme pildi tumedamaks")

        # pildi croppimine (ja zoomimine??????) vaja selgeks teha
        elif re.search("crop|väljalõi|välja lõi",userinput):
            print("siin teeme pildi tumedamaks")

        # pildi nihutamine
        elif re.search("transl|nihuta",userinput):
            print("siin teeme nihutamist")

        # perspektiivimuutus 
        #TODO siia vaja otsitavad fraasid välja mõelda
        # nt "pilt vale nurga all" vms
        elif re.search("",userinput):
            print("siin teeme perspektiivimuutust")

        #objektide leidmine / tuvastamine================================

        # mallide leidmine (panna samasse patta keerulisemate kujunditega?)
        elif re.search("",userinput):
            print("siin otsime malle")

        # keerulisemate kujundite leidmine
        elif re.search("",userinput):
            print("siin otsime keerulisemaid kujundeid")



        # boti vastus
        response = ""
        return response
        
    
