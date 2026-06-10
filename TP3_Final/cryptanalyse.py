import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chargement des mots de passe
df = pd.read_excel("TP3_Final/Codes_possibles.xlsx")
mots_de_passe = df["Codes possibles"].dropna().astype("Int64").astype(str).tolist()

# Lancement de chrome automatisé
driver = webdriver.Chrome()
driver.get("https://imagecypher.fr/")
time.sleep(3)

# Click dans la section décryptage (Il faut que la zone soit visible dans le navigateur)
decrypt_button = driver.find_element(By.ID, "tab-decode")
decrypt_button.click()
time.sleep(1)

# Upload de l'image
upload_box = driver.find_element(By.ID, "img-input-decode")

upload_box.send_keys(
    # Saisir le chemin absolu du fichier imagecypher-secret.png
    # "C:/Users/cleme/.../Python_secu_cryptage/TP3_Final/imagecypher-secret.png"
)
time.sleep(2)

for password in mots_de_passe:
    password = password.strip()
    
    # Trouver le champ de texte du mot de passe
    password_input = driver.find_element(By.ID, "password-decode")
    password_input.clear()
    password_input.send_keys(password)
    
    # Trouver et cliquer sur le bouton "Décoder"
    submit_button = driver.find_element(By.ID, "btn-decode")
    submit_button.click()
    time.sleep(0.5)
    
    # On récupère l'élément qui affiche le texte de reussite (toujours présent sur la page mais en display none)
    result_element = driver.find_element(By.ID, "decoded-message")
    # S'il s'affiche c'est qu'on a trouvé le mot de passe
    if result_element.is_displayed():
        print(f"\n[+] Trouvé ! Le mot de passe est : {password}")
        print(f"Message décrypté : {result_element.text}")
        break

# Fermeture du navigateur
driver.quit()