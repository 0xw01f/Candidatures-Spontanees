## Comment l'utiliser

`Ne mettez pas tout de suite les informations des personnes que vous souhaitez contacter. Essayez avec votre adresse email avant chaque envoi/modification du script.`

Il vous faut installer python et pip (https://www.python.org/).

Cloner ce repository & entrer dans le dossier :
```bash
git clone https://github.com/0xw01f/Candidatures-Spontanees/
cd Candidatures-Spontanees/
```


Installer les packets nécessaires :
```bash
python3 -m pip install -r requirements.txt
```


### Compléter le fichier config.py

```
SMTP_SERVER = 'smtp.gmail.com' # Leave as is
PORT = 587 # Leave as is
SENDER_EMAIL = 'you@mail.tld' # Your gmail email
PASSWORD = 'somepassortoken' # Your gmail password or app password if you have 2FA enabled
CSV_FILE = "recipients.csv" # CSV file with recipients' information (Some fields are required !)
CV_TEMPLATE = "cv_template.pdf" # Curriculum Vitae, 
LM_TEMPLATE = "lm_template.pdf" # Motivation Letter
ADDITIONAL_FILES = ['brochure.pdf', 'calendar.pdf'] # Additional files to attach to the email
JOB_NAME = "Python Developer" # Default job name
```

### Changer les fichiers PDF d'exemple :
- brochure.pdf
- calendar.pdf
- cv_template.pdf
- lm_template.PDF

### Changer le contenu du fichier recipients.csv

`Ne mettez pas tout de suite les informations des personnes que vous souhaitez contacter. Essayez avec votre adresse email avant chaque envoi/modification du script.`

Un fichier Dropcontact typique contient, entre autre, les informations suivantes :

```csv
Civilité;firstName;Suggestion de Prénom;lastName;fullName;title;Email;Email Qualification;profileUrl;Information Dropcontact;Société;Nom Légal de Société;Téléphone Société;Site Web;Dernier CA Publié;Dernier Résultat Publié;LinkedIn de l'entreprise;Secteur d’Activité;Numéro Siren;Numéro Siret Siège Social;Adresse;Code Postal du Siège Social;Ville Siège Social;Pays;Numéro de TVA;location
```
Toutes ces infos ne sont pas utilisées par le script, donc libre à vous de les changer.

Les informations obligatoires sont :
Civilité
firstName
lastName
fullName
email
societe
job_title

Le fichier recipients.csv doit contenir un contact par ligne.

⚠️ Attention aux doublons dans votre fichier source.

Rappel de bonnes pratiques :
- Rester poli et courtois
- Prendre le temps de répondre aux personnes qui répondent à vos emails automatiques (même en cas de refus)
- TOUJOURS tester le script sur un profil factice avce votre email pour s'assurer que tout est OK


### Lancer le script

```bash
python3 ./main.py
```


### Besoin d'aide ?
Contactez moi.

Info: J'ai aidé ChatGPT et Claude à faire le script (ils n'y seraient pas arrivés sans moi)
Info2: Si des recruteurs voient que mes mails nétaient pas réels, et que je partage la techique, ne me détestez pas s'il vous plaît
