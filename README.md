# Soltar y Botar 
* __Edgar Moreno__
* __Laura Valentina Gonzalez Neira__

Cuando se ejecute el proyecto que se encuentra en el repositorio se verá una imagen o video, dependiendo del archivo py que seleccione, en la cual se indica si el movimiento que se está realizando es botar o soltar el objeto. 
![Movimiento de soltar](https://github.com/LauraValentinaGonzalezNeira/ProyectoFinal2021-1/blob/main/imangenSoltar.PNG)

![Movimiento de soltar](https://github.com/LauraValentinaGonzalezNeira/ProyectoFinal2021-1/blob/main/imagenBotar.PNG)

Para diferenciar cuál de los dos movimientos se presenta nos basamos en la distancia que hay entre el dedo meñique y el dedo pulgar, en el caso de soltar la distancia entre los dedos es pequeña, por el contrario, cuando se bota el objeto de manera intencional esta distancia es mucho mayor. Para obtener el valor de esta distancia se implementó la librería de numpy, la cual nos permitió obtener los valores de las coordenadas de las puntas de los dedos, para luego utilizar la función np.linalg.norm la cual calcula la norma vectorial entre los dedos. 


Teniendo ese valor se asignó un rango para cada uno de los casos presentados y finalmente utilizando la librería OpenCV se ubicó el texto de salida que indica que movimiento se está realizando y una línea que muestra entre qué puntos se está tomando la distancia medida. 
