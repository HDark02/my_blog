from flask import Flask, render_template, url_for, redirect
import logging

# Crée l'application Flask
app = Flask(__name__)

# Configurer le logging pour capturer les erreurs
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Définir la route principale
@app.route('/')
def app_view():
    try:
        # Tentative de rendre la page index.html
        return render_template('index.html', my_name="Alex Dynamo")  # Assurez-vous que le fichier index.html est dans le dossier templates
    except Exception as error:
        # En cas d'erreur, loggez l'erreur dans le fichier de logs
        logger.error('App component error: %s', error)
        # Vous pouvez appeler une fonction report_error pour envoyer l'erreur quelque part si nécessaire
        report_error(error)  # Cette fonction doit être définie si vous souhaitez envoyer des erreurs à un service externe
        # Retourner une erreur HTTP 500 en cas d'exception
        return 'Internal Server Error', 500
@app.route("/<all_>")
def main(all_):
    return redirect(url_for("app_view"))

# Fonction de rapport d'erreur (vous pouvez l'adapter à votre besoin, par exemple pour envoyer l'erreur par email ou la stocker dans un fichier)
def report_error(error):
    # Exemple : envoyer l'erreur par email ou sauvegarder dans une base de données, etc.
    # Par exemple, vous pouvez intégrer un service comme Sentry, Rollbar, ou envoyer un email.
    print(f"Reporting error: {error}")

# Démarrer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)  # Active le mode debug pour afficher plus d'informations pendant le développement
