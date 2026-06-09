import numpy as np
import cv2

### Bruitage
# On prend notre image de base
img=cv2.imread("Debruitage_images/img/originale.jpg",0)

# On Crée le nuage de point gaussien de la taille de notre image 
gauss_noise=np.zeros((img.shape),dtype=np.uint8)
cv2.randn(gauss_noise,128,20)
gauss_noise=(gauss_noise*10).astype(np.uint8)

# On ajoute à notre image le nuage de point qui est notre bruit
img_noised=cv2.add(img,gauss_noise)

# On save l'image avec le bruit
cv2.imwrite("Debruitage_images/img/img_noise.jpg", img_noised)


### Débruitage
# Récupération del'image à débruiter
img2=cv2.imread("Debruitage_images/img/img_a_debruiter.png")

# On réduit le bruit avec la fonction dédiée
noise_removed_img=cv2.fastNlMeansDenoising(img2, None, 30.0, 15, 15)

cv2.imwrite("Debruitage_images/img/img_noise_removed.png", noise_removed_img)

