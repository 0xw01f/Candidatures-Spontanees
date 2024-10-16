## Que fait ce script ?
Ce script permet d'envoyer des **candidatures spontanées** à une liste de personnes. Les candidatures sont personnalisées et s'adressent directement à la personne qui reçoit l'email.

Le script récupère les informations (Prénom, Nom, Civilité, Email, Entreprise, Poste) pour compléter un email d'accroche type.

Il génère également des **CV** et des **lettres de motivation** personnalisés pour chaque poste et personne ciblés, et les attache à l'email de candidature.

En plus, il peut ajouter des fichiers supplémentaires, comme un **calendrier** ou une **brochure**, à l'email.

## Comment l'utiliser

**Avant toute utilisation réelle, faites des essais en utilisant votre propre adresse email**. Cela vous permet de vérifier que tout fonctionne bien avant d'envoyer des candidatures réelles.

### Pré-requis
Il vous faut installer **Python** et **pip**. Si ce n'est pas encore fait, vous pouvez les installer ici : [https://www.python.org/](https://www.python.org/).

### Cloner le repository & entrer dans le dossier :

```bash
git clone https://github.com/0xw01f/Candidatures-Spontanees/
cd Candidatures-Spontanees/
```

### Installer les dépendances :
```bash
python3 -m pip install -r requirements.txt
```

### Configurer le fichier `config.py`

Modifiez les informations dans le fichier `config.py` pour qu'il corresponde à votre situation :

```python
SMTP_SERVER = 'smtp.gmail.com'  # Serveur SMTP (Gmail par défaut)
PORT = 587  # Port SMTP (Gmail)
SENDER_EMAIL = 'you@mail.tld'  # Votre adresse Gmail
PASSWORD = 'somepasswordtoken'  # Votre mot de passe Gmail ou mot de passe d'application si 2FA est activé
CSV_FILE = "recipients.csv"  # Fichier CSV contenant les informations des destinataires
CV_TEMPLATE = "cv_template.pdf"  # Modèle de CV
LM_TEMPLATE = "lm_template.pdf"  # Modèle de lettre de motivation
ADDITIONAL_FILES = ['brochure.pdf', 'calendar.pdf']  # Fichiers supplémentaires à attacher à l'email
JOB_NAME = "Python Developer"  # Nom du poste par défaut
```

⚠️ **Note importante** : Si l'authentification à deux facteurs (2FA) est activée sur votre compte Gmail, vous devrez utiliser un **mot de passe d'application** à la place de votre mot de passe habituel. Vous pouvez en générer un ici : [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

### Changer les fichiers PDF d'exemple

Remplacez les fichiers suivants dans le dossier par vos propres versions :
- `brochure.pdf`
- `calendar.pdf`
- `cv_template.pdf`
- `lm_template.pdf`

### Modifier le fichier `recipients.csv`

**Attention :** N'ajoutez pas immédiatement les informations des personnes que vous souhaitez contacter. Testez d'abord avec votre propre email.

Votre fichier CSV doit avoir un format similaire à ceci :

```csv
Civilité;firstName;lastName;fullName;title;Email;Société;job_title
```

Les champs obligatoires sont :
- `Civilité`
- `firstName`
- `lastName`
- `fullName`
- `Email`
- `Société`
- `job_title`

Chaque ligne doit représenter un contact. **Attention aux doublons** dans le fichier.

### Bonnes pratiques :
- Soyez toujours **poli** et **courtois** dans vos communications.
- Prenez le temps de répondre aux personnes qui vous répondent, même en cas de refus.
- **Testez toujours** le script avec votre propre email avant de l'utiliser avec des destinataires réels.

## Génération de CV et lettres de motivation

Le script génère des fichiers **PDF uniques** pour chaque candidature. Il complète les informations telles que le nom du destinataire, le nom de l'entreprise, et le poste, dans des modèles de **CV** et de **lettres de motivation**.

### Où modifier les textes ?

Les textes des emails et lettres de motivation se trouvent dans le code source, dans le fichier `main.py`.

- Exemple de lettre de motivation à la fin du fichier `main.py`.
- Variables disponibles :
  - `recipient['fullName']`
  - `recipient['firstName']`
  - `recipient['societe']`
  - `recipient['job_title']` (le poste de votre interlocuteur)
  - `job_name` (le poste que vous postulez)

Adaptez le texte de votre lettre de motivation en fonction de ces variables.

### Modifications du CV
Le script remplit uniquement le titre du poste que vous visez sur votre CV PDF (`cv_template.pdf`).

Pour ajuster la position du texte :
- Ligne 23 pour le CV
- Ligne 41 pour la lettre de motivation

![Example](https://i.imgur.com/NtxNFHJ.png)

### Lancer le script

Une fois que tout est configuré, vous pouvez lancer le script :

```bash
python3 main.py
```

### Besoin d'aide ?
N'hésitez pas à me contacter pour toute question ou problème.

---

**Info** : J'ai utilisé ChatGPT et Claude pour m'aider à créer ce script (ils n'y seraient pas arrivés seuls !).

**Info 2** : Si des recruteurs voient que mes emails n'étaient pas réels, et que je partage cette méthode, **ne me détestez pas** s'il vous plaît.
