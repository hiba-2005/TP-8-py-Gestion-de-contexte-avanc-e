from datetime import datetime
from contextlib import ExitStack


class ConnectionManager:
    def __init__(self, service_name):
        self.service_name = service_name

    def __enter__(self):
        print(f"[{datetime.now()}] Connexion à {self.service_name} établie.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"[{datetime.now()}] Déconnexion de {self.service_name}.")
        if exc_type:
            print(f"Erreur détectée : {exc_type.__name__} — {exc_value}")
       
        return False


def test_sans_erreur():
    with ExitStack() as stack:
        log = stack.enter_context(open("log.txt", "a", encoding="utf-8"))
        conn = stack.enter_context(ConnectionManager("Serveur X"))

        message = f"[{datetime.now()}] Tâche effectuée sur {conn.service_name}\n"
        print("-> Écriture dans log.txt :", message.strip())
        log.write(message)


def test_avec_erreur():
    with ExitStack() as stack:
        log = stack.enter_context(open("log.txt", "a", encoding="utf-8"))
        conn = stack.enter_context(ConnectionManager("Base Y"))
   
        log.write(f"[{datetime.now()}] Début d'une opération sur {conn.service_name}\n")
       
        raise RuntimeError("Erreur de traitement")


if __name__ == "__main__":
    test_sans_erreur()

    try:
        test_avec_erreur()
    except RuntimeError as e:
        print("Exception capturée dans le code appelant :", e)
