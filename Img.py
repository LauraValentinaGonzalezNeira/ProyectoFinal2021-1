import cv2
import mediapipe as mp
import numpy as np


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


with mp_hands.Hands(
    static_image_mode=True, ##Se utiliza para imagenes 
    max_num_hands=2) as hands: ## Número de manos a leer

    img = cv2.imread('botar22.jpg')
    height, width, _ = img.shape ## Se obtiene el ancho y el alto 
    img = cv2.flip(img,1) ##Voltear la imagen de forma horizontal
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks: ## Para obtener los 21puntos
            mp_drawing.draw_landmarks(
                img, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )  ##Dibujar los puntos y las conexiones
            pnt = np.array([[int(coor.x*width), int(coor.y*height)] for coor in hand_landmarks.landmark]).T
            pulgar=list(pnt[:,4])
            meñique=list(pnt[:,20])
            pgr=np.array(pulgar)
            mñq=np.array(meñique)
            dist = np.linalg.norm(pgr-mñq) ## La función encuentra el valor de la norma vectorial 
            print(dist)
            ##img=cv2.flip(img,1)
            if dist < 200:
                cv2.putText(img,'El movimiento indica soltar',(50,100),cv2.FONT_HERSHEY_SIMPLEX ,1,(0,0,0),2,cv2.LINE_AA)
                cv2.line(img,pulgar,meñique,(0,255,0),3)
            else: 
                cv2.putText(img,'El movimiento indica botar',(100,90),cv2.FONT_HERSHEY_SIMPLEX ,1,(0,0,0),2,cv2.LINE_AA)
                cv2.line(img,pulgar,meñique,(0,255,0),3)


cv2.imshow("Image", img)
cv2.waitKey(0) 
cv2.destroyAllWindows()          

