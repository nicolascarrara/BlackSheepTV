/*****************************************************************\
***                                                               *
***                                                               *
***                       BLACKSHEEPTV                            *
***                                                               *
***                                                               *
\\*****************************************************************/

 ******************* Site Crawlé pour séries TV *****************
 ================================================================

 - www.thetvdb.com

 ********************* Site Crawlé pour Films *******************
 =================================================================

 - www.themoviedb.org

 Paquets Installés :
 - bs4
 - coreapi
 ( voir requirements.txt )

Installation des fixtures :
- ./manage.py migrate
- ./manage.py loaddata fixtures.json

Lancement du serveur :
- ./manage.py runserver --insecure
(Pour charger les fichiers statics même en production)
