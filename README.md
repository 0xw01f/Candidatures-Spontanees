# Candidatures Spontanées

## Que fait ce script ?

[example](img/example.png)

Ce script permet d'envoyer des **candidatures spontanées** à une liste de personnes. Les candidatures sont personnalisées et s'adressent directement à la personne qui reçoit l'email.

Le script récupère les informations (Prénom, Nom, Civilité, Email, Entreprise, Poste) pour compléter un email d'accroche type.

Il génère également des **CV** et des **lettres de motivation** personnalisés pour chaque poste et personne ciblés, et les attache à l'email de candidature.

En plus, il peut ajouter des fichiers supplémentaires, comme un **calendrier** ou une **brochure**, à l'email.

## Comment l'utiliser

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

## Utilisation d'un fichier `email_content.txt` pour le contenu des emails

Au lieu de modifier le contenu des emails directement dans le fichier Python, vous pouvez utiliser un fichier externe appelé `email_content.txt`. Ce fichier contiendra le corps de l'email, avec des **placeholders** qui seront remplacés par les informations spécifiques à chaque destinataire (comme le nom ou l'entreprise).

### Créer le fichier `email_content.txt`

Créez un fichier nommé `email_content.txt` dans le même répertoire que le script Python, avec un format similaire à ceci :

```txt
Subject: Application for {job_name} at {company}

Dear {full_name},

I hope this message finds you well. I am writing to express my interest in the {job_name} position at {company}. With my background and experience in {recipient_job_title}, I believe I could be a strong fit for your team.

Attached, you will find my CV and cover letter for more details on my qualifications. I look forward to the possibility of discussing how I can contribute to your company.

Best regards,
Your Name
Your Contact Information
```

### Variables disponibles pour personnaliser le contenu de l'email

- `{full_name}` : Le nom complet du destinataire.
- `{company}` : Le nom de l'entreprise du destinataire.
- `{job_name}` : Le nom du poste pour lequel vous postulez (défini dans `config.py`).
- `{recipient_job_title}` : Le titre du poste du destinataire.

Ces variables seront automatiquement remplacées par les informations appropriées pour chaque destinataire.

### Gestion d'erreurs

#### Fichier `email_content.txt` manquant

Si le fichier `email_content.txt` est manquant, vous verrez le message suivant dans le terminal :

```
Error: The email content file 'email_content.txt' was not found. Please make sure the file exists in the correct directory.
```

Cela signifie que le fichier contenant le modèle de votre email n'a pas été trouvé. Pour résoudre ce problème, assurez-vous d'avoir créé et ajouté le fichier `email_content.txt` dans le répertoire du projet.

### Gestion des erreurs d'authentification SMTP

Le script a été modifié pour gérer les erreurs d'authentification SMTP afin qu'aucun email ne soit envoyé si l'authentification échoue.

#### Message d'erreur en cas d'authentification échouée

Si les identifiants de connexion au serveur SMTP (comme l'email et le mot de passe) sont incorrects, vous verrez le message suivant dans le terminal :

```
SMTP Authentication Error: Invalid credentials for {your_email}. Please check your username and password.
Details: {détails de l'erreur}
```

Le programme ne tentera pas d'envoyer d'emails si cette erreur se produit.

### Résolution des erreurs SMTP

1. **Vérifiez vos identifiants de connexion** : Assurez-vous que l'adresse email et le mot de passe (ou mot de passe d'application) dans le fichier `config.py` sont corrects.
2. **Utilisation d'un mot de passe d'application** : Si vous avez activé l'authentification à deux facteurs (2FA) sur votre compte Gmail, vous devez générer un mot de passe d'application à utiliser dans le script. Vous pouvez générer un mot de passe d'application ici : [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

En cas d'erreur, corrigez vos identifiants dans `config.py` et relancez le script.

### Génération de CV et lettres de motivation

Le script génère des fichiers **PDF uniques** pour chaque candidature. Il complète les informations telles que le nom du destinataire, le nom de l'entreprise, et le poste, dans des modèles de **CV** et de **lettres de motivation**.

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

### Mises à jour clés :
1. **Fichier `email_content.txt`** : Le README inclut désormais des instructions sur la création du fichier `email_content.txt` et l'utilisation de **placeholders** (modèles) qui sont remplacés dynamiquement par les données du destinataire.
2. **Gestion de l'erreur "Fichier introuvable"** : Des instructions ont été ajoutées pour gérer les cas où le fichier `email_content.txt` est manquant, avec des détails sur le message d'erreur et comment résoudre le problème.
3. **Gestion des erreurs d'authentification SMTP** : Explication détaillée de la façon dont le script gère les erreurs d'authentification SMTP, ce à quoi ressemble le message d'erreur et comment résoudre les problèmes en vérifiant les identifiants ou en utilisant un mot de passe d'application Google.
4. **Autres améliorations** : Le README a été clarifié et simplifié à plusieurs endroits, facilitant la compréhension de l'utilisation et de la configuration du script pour les utilisateurs.


