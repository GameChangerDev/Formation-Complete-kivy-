from secrets import token_bytes
from hashlib import sha256
import json


pwd = input("entrez le mot de passe : ")
sel = token_bytes(16)
hash_obj = sha256(sel + pwd.encode("utf-8"))
hex_origin = hash_obj.hexdigest()

def create_hexdigest(salt, password):       # Créer le resumé hexadécimal du hash
    hashage = sha256(bytes.fromhex(salt) + password.encode("utf-8"))
    return hashage.hexdigest()

if pwd:                            # Enregistrement crypté du mot de passe
    with open("pwd.json", "w") as f:
        json.dump({"sel": sel.hex(), "hex_hash": hex_origin}, f, indent=3)
        print("mot de passe enregistré.")
else:                               # Lecture de fichier dans lequel on a enrégistré le mot de passe
    with open("pwd.json", "r") as f:
        pwd_file = json.load(f)

while True:
    print("Veuillez vous connectez : ")
    print(f"{".-."*60}", sep="\n")
    pwd_verif = input("Entrez le mot de passe de Connexion : ")# mot de pass de connection
    print(f"{".-."*60}", sep="\n")

    if not pwd:
        hex_origin2 = create_hexdigest(pwd_file["sel"], pwd_verif) # hexadeciaml du hash de connexion
        hex_origin = pwd_file["hex_hash"] # hexadeciaml du hash de de définition
    else:
        hex_origin2 = sha256(sel + pwd_verif.encode("utf-8")).hexdigest() # hexadeciaml du hash de connexion


    if hex_origin == hex_origin2:# hash de definition  est égal au hash de conexion
        print(f"{".-." * 60}")
        print("Mot de passe Correct Vous êtes connecté aux ressources", sep="\n")
        print(f"{".**." * 60}")
        print(f"{".-*-." * 60}")
        print(f"{".-**-." * 60}")
        break
    else:
        print(f"{".-." * 60}")
        print("Mot de passe incorrect")
        continue

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# il faut retenir que le json ne stocke que des infos en hexadécimale, pour travailler sur le cryptage des mots de passes,
# il faut travailler avec la classe bytes de builtins, _HASH de hashlib et le fonction token_bytes de secrets