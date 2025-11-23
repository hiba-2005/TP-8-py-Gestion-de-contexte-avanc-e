from batch_processor import BatchProcessor

if __name__ == "__main__":
    chemin_csv = "operations.csv"
    with BatchProcessor(chemin_csv) as batch:
        batch.traiter()
