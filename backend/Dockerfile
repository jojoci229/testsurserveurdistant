# Utiliser une image Python officielle comme image de base
FROM python:3.7-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt (si vous avez des dépendances) dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'application va fonctionner
EXPOSE 5000

# Définir la commande pour exécuter l'application (à adapter selon votre framework)
CMD ["python", "app.py"]
