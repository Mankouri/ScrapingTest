# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 14:16:17 2018

@author: jalil Scraping Deepki
"""
# http://www.portailsig.org/content/python-lire-et-ecrire-des-fichiers-microsoft-excel-application-quantum-gis
# https://www.dataquest.io/blog/web-scraping-beautifulsoup/

# http://www.immochan.com/fr/implantations-sites-commerciaux?page=1
# 24 pages, <table> avec 10 sites commerciaux par page

from requests import get
from bs4 import BeautifulSoup
from xlwt import Workbook


# Excel
book = Workbook()
 
# création de la feuille 1
feuil1 = book.add_sheet('feuille 1')
 
# ajout des en-têtes
feuil1.write(0,0,'Nom commercial du Site')
feuil1.write(0,1,'Ville')
feuil1.write(0,2,'Etat')
feuil1.write(0,3,'Surface GLA')
feuil1.write(0,4,'Nombres de boutiques')
feuil1.write(0,5,'Contact')

# Boucle pour les 24 pages
numPage = 1
while numPage <24:
    url = 'http://www.immochan.com/fr/implantations-sites-commerciaux?page='+ str(numPage)
    
    response = get(url)
    # test :affiche les 1000 premiers caractères du contenu de la page
    #print(response.text[:1000])
    # Utilisation de Beautifulsoup pour parser le code HTML de la page
    html_soup = BeautifulSoup(response.text, 'html.parser')
    # Pour les tr impaire la classe odd apparait et paire even, je décide donc
    # de cibler mon scraping sur ces classes
    site_commercial_containers_odd = html_soup.find_all('tr', class_ = 'odd')
    site_commercial_containers_even = html_soup.find_all('tr', class_ = 'even')
    
    # On recupère le nombre de résultat trouvé, on attend comme réponse 5 odd 
    # et 5 even (10 par page)
    imax = len(site_commercial_containers_odd)
    jmax = len(site_commercial_containers_even)
    
    # Boucle pour les 10 sites
    i=0
    j=0
    k=(numPage-1)*10
    stop = k+imax+jmax
    print('numPage ' + str(numPage))
    while k < stop:
        print( str(k)+ ' < ' + str(stop))
        # Extraction des données d'un site commercial odd
        nom_site = []
        nom_site = site_commercial_containers_odd[i].a.text        
        ville = site_commercial_containers_odd[i].find('td', class_ = 'views-field views-field-field-city').text.replace(" ","")
        etat = site_commercial_containers_odd[i].find('td', class_ = 'views-field views-field-field-status').text.replace(" ","")
        surface = site_commercial_containers_odd[i].find('td', class_ = 'views-field views-field-field-shopping-center-surface').text.replace(" ","")
        nb_boutique = site_commercial_containers_odd[i].find('td', class_ = 'views-field views-field-field-number-of-shops').text.replace(" ","")
        contact = site_commercial_containers_odd[i].find('td', class_ = 'views-field views-field-field-contact').text
        i = i + 1
        # test
        #print(nom_site + ' ' + ville + ' ' + etat + ' ' + surface + ' ' + nb_boutique + ' ' + contact)    
        # ajout des valeurs sur la ligne suivante
        ligneImpair = feuil1.row(k+1)
        ligneImpair.write(0,nom_site)
        ligneImpair.write(1,ville)
        ligneImpair.write(2,etat)
        ligneImpair.write(3,surface)
        ligneImpair.write(4,nb_boutique)
        ligneImpair.write(5,contact)
        k = k +1
        # Extraction des données d'un site commercial even
        nom_site = site_commercial_containers_even[j].a.text
        ville = site_commercial_containers_even[j].find('td', class_ = 'views-field views-field-field-city').text.replace(" ","")
        etat = site_commercial_containers_even[j].find('td', class_ = 'views-field views-field-field-status').text.replace(" ","")
        surface = site_commercial_containers_even[j].find('td', class_ = 'views-field views-field-field-shopping-center-surface').text.replace(" ","")
        nb_boutique = site_commercial_containers_even[j].find('td', class_ = 'views-field views-field-field-number-of-shops').text.replace(" ","")
        contact = site_commercial_containers_even[j].find('td', class_ = 'views-field views-field-field-contact').text
        j = j + 1
        lignePair = feuil1.row(k+1)
        lignePair.write(0,nom_site)
        lignePair.write(1,ville)
        lignePair.write(2,etat)
        lignePair.write(3,surface)
        lignePair.write(4,nb_boutique)
        lignePair.write(5,contact)
        k = k +1
    
    numPage = numPage + 1
# création du fichier excel
book.save('resultatDeepkiScraping.xls')
