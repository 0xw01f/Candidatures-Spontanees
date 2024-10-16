
## Que fait ce script ?
IL permet d'envoyer des candidatures spontanées à une liste de personnes. Ces candidatures sont personnalisées, et s'adressent directement à la personne qui reçoit l'email. 

On récupère les infos (Prénom, No, Civilité, Mail, Entreprise, Poste) pour compléter un email d'accroche type.

Ce script génère aussi des CV et des Lettres de Motivation pour chaque différent poste et différente personne que vous ciblez, et les attache à l'email de candidature.

Il attache également des fichiers supplémentaires, comme le calendrier et la brochure de l'école. 



## Comment l'utiliser

`Ne mettez pas tout de suite les informations des personnes que vous souhaitez contacter. Essayez avec votre adresse email avant chaque envoi/modification du script.`

Il vous faut installer python et pip (https://www.python.org/).

Cloner ce repository & entrer dans le dossier :
```bash
git clone https://github.com/0xw01f/Candidatures-Spontanees/
cd Candidatures-Spontanees/
```


Installer les paquets nécessaires :
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

Vous avez sûrement le 2FA d'activé sur votre compte Google. Alors au lieu du mot de passe il faut créer un "app password" ici : https://myaccount.google.com/apppasswords

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


### La génération de lettre de motivation et de CV
Ce script génère aussi des pdf uniques à chaque candidature. En prenant le nom du destinataire, son entreprise et d'autres informations, il complète une lettre de motivation ou un CV à trou et écrit ces informations sur votre template de CV et de lettre de motivation actuel.

##### Où sont les textes à modifier ?
Pour le moment il faut aller chercher dans le code source.

À la fin du fichier `main.py` vous avez un "exemple" de lettre de motivation. 
Utilisez les variables :
`recipient['fullName']`
`recipient['firstName']`
`recipient['societe']`
`recipient['job_title']` -> Le job de votre interlocuteur
`job_name` -> Votre futur job

Et écrivez votre propre lettre de motivation !

Pour le CV, le script n'écrit que l'intitulé du poste que vous souhaitez sur votre CV en PDF (`cv_template.pdf`).

Modifiez la position du texte que le script écrit :
Ligne 23 pour le CV
Ligne 41 pour la lettre de motivation  

![Example](https://i.imgur.com/NtxNFHJ.png)



### Lancer le script

```bash
python3 ./main.py
```


### Besoin d'aide ?
Contactez moi.

Info: J'ai aidé ChatGPT et Claude à faire le script (ils n'y seraient pas arrivés sans moi)

Info2: Si des recruteurs voient que mes mails nétaient pas réels, et que je partage la technique, ne me détestez pas s'il vous plaît
