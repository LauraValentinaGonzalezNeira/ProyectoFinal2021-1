import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

vid = cv2.VideoCapture('botar1.mp4')
with mp_hands.Hands(
    static_image_mode=False, ##Se utiliza para video
    max_num_hands=1) as hands: ## Número de manos a leer

 while True:  ##Para leer el video
    ret, frame = vid.read()
    if ret == False:  
        break

    height, width, _ = frame.shape ## Se obtiene el ancho y el alto 
    frame = cv2.flip(frame,1) ##Voltear la imagen de forma horizontal
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)## Se pasan los fotogramas de vgr a rgb
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks: ## Para obtener los 21puntos
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )  ##Dibujar los puntos y las conexiones
           ##:##Devuelve la coordenada de cada punto y el punto
            pnt = np.array([[int(coor.x*width), int(coor.y*height)] for coor in hand_landmarks.landmark]).T
            pulgar=list(pnt[:,4])
            meñique=list(pnt[:,20])
            pgr=np.array(pulgar)
            mñq=np.array(meñique)
            dist = np.linalg.norm(pgr-mñq) ## La función encuentra el valor de la norma vectorial 
            #print(dist)
            if dist < 200:
                cv2.putText(frame,'El movimiento indica soltar',(20,50),cv2.FONT_HERSHEY_SIMPLEX ,1,(0,0,0),2,cv2.LINE_AA)
                cv2.line(frame,pulgar,meñique,(0,255,0),3)
            else: 
                cv2.putText(frame,'El movimiento indica botar',(20,50),cv2.FONT_HERSHEY_SIMPLEX ,1,(0,0,0),2,cv2.LINE_AA)
                cv2.line(frame,pulgar,meñique,(0,255,0),3)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(70) & 0xFF == 27: ##Para trabajar en una maquina de 64bits 
        break                       ## Tiempo que se muestra el video 

vid.release() ## Finalizar la captura del video
cv2.destroyAllWindows()##Cerrar ventanas abiertas 
