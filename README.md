# OC_P02

Ce programme permet de scrapper le site web https://books.toscrape.com pour en ressortir les éléments suivants:

  1. Pour chaque catégorie de livre le programme crée un fichier CSV contenant pour chaque livre:
      product_page_url
      universal_ product_code (upc)
      title
      price_including_tax
      price_excluding_tax
      number_available
      product_description
      category
      review_rating
      image_url
      
  2. Le programme va télécharger l'image de chaque livre consulté

  3. Les fichiers générés seront classés dans un dossier CSV ou Image selon leur type

## Packages à installer
    Se référer au fichier requirements.txt
    
## Utilisation
    Mettre à jour le chemin pour créer les dossiers où seront stockés les fichiers csv et image dans la page "constants.py"
    Exécuter le fichier main.py
  
