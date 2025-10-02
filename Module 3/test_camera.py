import cv2

cap =  cv2.VideoCapture(0) # Zéro pour la camera par défaut
if not cap.isOpened():
    print("Erreur: Impossible d'ouvrir la caméra.")
else:
    ret, frame = cap.read()
    if ret:
        print(f"Résolution: {frame.shape}")
    else:
        print(f"Impossible de capturer une frame.")

cap.release()
