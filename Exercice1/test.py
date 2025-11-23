from pathlib import Path
from TempFileWriter import TempFileWriter
from Partie2 import temp_file


if __name__ == "__main__":
    
    
    print(" TEST 1 : TempFileWriter")
   
    print("Avant le with, temp.txt existe ? ", Path("temp.txt").exists())

    try:
        with TempFileWriter() as f:
            print("Dans le with, temp.txt existe ? ", Path("temp.txt").exists())
            f.write("Contenu temporaire\n")
    except Exception as e:
        print("Erreur capturée :", e)

    print("Après le with, temp.txt existe ? ", Path("temp.txt").exists())

  
    print(" TEST 2 : temp_file()")

    print("Avant le with, temp2.txt existe ? ", Path("temp2.txt").exists())

    with temp_file() as f:
        print("Dans le with, temp2.txt existe ? ", Path("temp2.txt").exists())
        f.write("Autre test\n")

    print("Après le with, temp2.txt existe ? ", Path("temp2.txt").exists())


    print(" TEST 3 : ExitStack")
 
    


   