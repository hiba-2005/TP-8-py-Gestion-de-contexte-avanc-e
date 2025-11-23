import csv
from datetime import datetime


class BatchProcessor:
    def __init__(self, csv_path, log_path="journal.log"):
        self.csv_path = csv_path
        self.log_path = log_path
        self.csv_file = None
        self.log_file = None
        self.reader = None

    def __enter__(self):
        try:
            self.csv_file = open(self.csv_path, "r", newline="", encoding="utf-8")
        except OSError as e:
            raise RuntimeError(f"Erreur lors de l'ouverture du fichier CSV: {e}")

        try:
            self.log_file = open(self.log_path, "a", encoding="utf-8")
        except OSError as e:
            self.csv_file.close()
            raise RuntimeError(f"Erreur lors de l'ouverture du fichier de log: {e}")

        self.reader = csv.reader(self.csv_file)
        self._log(f"Début du batch sur {self.csv_path}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._log(f"Exception: {exc_type.__name__} - {exc_val}")

        self._log(f"Fin du batch sur {self.csv_path}")

        if self.csv_file:
            try:
                self.csv_file.close()
            except OSError:
                pass

        if self.log_file:
            try:
                self.log_file.close()
            except OSError:
                pass

        return False

    def _log(self, message):
        timestamp = datetime.now()
        try:
            self.log_file.write(f"[{timestamp}] {message}\n")
            self.log_file.flush()
        except OSError:
            pass

    def traiter(self):
        for index, ligne in enumerate(self.reader, start=1):
            try:
                self._log(f"Début traitement ligne {index}: {ligne}")
                resultat = self._traiter_ligne(ligne)
                self._log(f"Fin traitement ligne {index}: {resultat}")
            except Exception as e:
                self._log(f"Erreur ligne {index}: {e}")
                raise

    def _traiter_ligne(self, ligne):
        return [cellule.upper() for cellule in ligne]
