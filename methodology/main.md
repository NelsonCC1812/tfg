# Methodology

## Tabla de contenidos

- [Methodology](#methodology)
  - [Tabla de contenidos](#tabla-de-contenidos)
  - [Idea](#idea)
    - [Problemas](#problemas)
  - [Procedimiento](#procedimiento)
    - [Origen de los datos](#origen-de-los-datos)
      - [Criterios](#criterios)
    - [Trabajo con los datos](#trabajo-con-los-datos)
      - [Uniendo los datos](#uniendo-los-datos)
      - [Tomando solo aquello que necesitamos](#tomando-solo-aquello-que-necesitamos)
      - [Calculando columnas nuevas](#calculando-columnas-nuevas)
      - [Filtrando las columnas](#filtrando-las-columnas)
      - [Converters](#converters)
      - [Reordering the data](#reordering-the-data)
      - [Modelos](#modelos)


## Idea

Lo que buscamos es analizar el desempeño de diferentes modelos de ***machine learning* (IA)** a la hora de predecir si una empresa tendrá problemas económicos en un plazo de **dos años**, en este caso, buscamos especializarlo en la industria del vino (CNAE: 1102)

Además también hemos incluido un algoritmo para descubrir si se trata de una empresa familiar basado en este artículo [Casillas - 2024.pdf](../papers/Casillas%20-%202024.pdf), para ver si esta variable podría ser relevante.


### Problemas

Debido a la pandemia de COVID-19 y los problemas económicos que causó, esto influencia los indices a analizar y nos restringe fuertemente la cantidad de datos que podemos usar, además, debido a una serie de factores que se comentarán a lo largo de la **metodología** el tamaño de la muestra es un problema central en este trabajo.

Los datos, ya sea por la fuente de los datos o por el algoritmo, nos deja con menos datos todavía si queremos usar dicha variable, por lo que si ya el tamaño muestral era menos que el deseable para empezar, esto nos deja con mayores dificultades para nuestro proyecto.


## Procedimiento

En este archivo puedes encontrar una pequeña tabla que puede ayudar a ilustrar el flujo de trabajo.

[Tabla con el flujo de trabajo](../scripts_flow.md)


### Origen de los datos

Los datos han salido de la base de datos SABI, un servicio software que almacena y datos de diferente índole.


#### Criterios

Los criterios que se han seguido a la hora de filtrar la información de la base de datos de SABI han sido para respetar las recomendaciones para aplicar el algoritmo para la clasificación de si una empresa se trata de una empresa familiar o no.

* CNAE: 1102
* Estados España: Activa (Para que los datos este actualizados)
* Código consolidación: C1, C2/U2, U1 (para tener datos asegurar que tenemos los datos de las empresas)
* Años con cuentas disponibles: 2022, 2024
* Aquellas empresas en las que un <=50% de los accionistas son extranjeros, debido a la posible falta de información
* Resultado de explotación de todos los años conocidos como mínimo conocido (2022, 2024)

> Como hemos indicado previamente el COVID-19 supone una gran interferencia en los datos, por lo que los datos con las variables de entrada serán del **2022** y los datos a predecir (dos años después) serán del **2024**.


### Trabajo con los datos

Es importante destacar que vamos a seguir el principio de que cada script se dedica específicamente a una tarea, y además, cada uno de ellos generará una salida. Esto nos facilitará no tener que ejecutar todo el código por cada cambio.

Adicionalmente, en cada script tendremos una estructura similar, donde habrán ajustes que nos permitan modificar aspectos del comportamiento del script mediante constantes, una zona de "adjustments" donde se hará con dichas constantes los ajustes pertinentes; una zona de preparativos, con cosas como la importaciones, cargar constantes que se usen entre archivos, herramientas como funciones y demás. Tras esto vendrán funciones que se usen específicamente en el código, estructuras de datos y lógica.

Acto seguido, vendrá la parte principal, donde se cargan los datos, se ejecuta la acción a realizar, se hacen comprobaciones varias y, por ultimo, se guarda el dataframe en un nuevo archivo, tanto para trabajar con el en el siguiente script, como para poder ver de forma sencilla los datos resultantes.

Además, destacar que se han usado estructuras de datos propias, variables y constantes, a lo largo de diversos archivos. Esto con el objetivo de estandarizar algunas cosas y de que algunos parámetros sean más fácilmente modificables, así como, aislar los errores y evitar fallos por repetición (siguiendo principios como DRY).


#### Uniendo los datos

Debido a que no podemos descargar todos los datos de una tanda, lo primero es unir los diferentes archivos generados en un solo archivo para poder trabajar con los datos. Dependiendo de como vengan los datos originalmente (ya que se pueden descargar en 2 formatos diferentes también tendremos que modificar los datos para que se utilice el formato de una empresa por línea).


#### Tomando solo aquello que necesitamos
> db_reader.ipynb

En este script buscamos tomar solo aquellas columnas que necesitamos para trabajar con ellas, simplificando así los pasos siguientes, y especialmente haciendo mas ligera la carga y el uso de los datos.


#### Calculando columnas nuevas
> cal_columns.ipynb

En este paso vamos a calcular las columnas nuevas con las que vamos a trabajar, en el capitulo dedicado a ello se explica cuales y por que. Aquí también se implementa el algoritmo que intenta calcular si se trata de una empresa familiar o no.


#### Filtrando las columnas
> filter_indexes.ipynb
 
En este script buscamos quedarnos solo que aquellos indices o columnas con los que vamos a trabajar. Debido a que en el paso anterior generamos algunas columnas como pasos intermedios, tenemos columnas que no necesitamos de ahora en adelante.


#### Converters
> convert-ffu.ipynb
> convert-nfv.ipynb

Como se han usado varias aproximaciones en cuanto a uso de indices se refiere, hemos optado por crear una tabla para cada una de las configuraciones de datos se refiere, estas divisiones se han creado debido a que el algoritmo que discierne entre empresas familiares o no tiene no siempre arroja un resultado binario, es decir, a veces no se sabe con certeza por falta de datos o certeza. Las aproximaciones que se han seguido son las siguientes:

* **No familiar var (nfv)**: Quitamos la columna de la variable familiar.
* **Filtered familiar unknowns (ffu)**: Quitamos aquellas filas del conjunto de datos en las que no se pueda discernir si se trata de una empresa familiar o no. El problema de esta aproximación es que tenemos muy pocos datos disponibles.

Existe una última tabla para la que no se utilizó un converter ni tiene conjunto de datos propio. **No familiar var - ffu** que, partiendo de la tabla **Filteded familiar unknowns**, se le eliminó la columna de la variable familiar. Esto se ha hecho para comparar **nfv** respecto de **ffu** y saber si el uso de la variable familiar supone alguna ventaja notable frente a no usarla, o si la diferencia en las métricas se debe solamente a el tamaño de la muestra.


#### Reordering the data
> reorder_data.ipynb

Este procedimiento esta encargado de preparar cada una de las entradas ("entries") o filas que se le pasarán a los modelos en el formato que estos lo recibirán, esto es, tomar los indices de entrada y relacionarlos con las salidas a predecir.

> Cabe destacar que como ahora tenemos 3 tablas de datos diferentes, se han hecho ajustes que permiten la reutilización de este código con las diferentes tablas simplemente modificando unos parámetros.


#### Modelos
> aicode-ffu.ipynb
> aicode-nfv.ipynb

En los pasos anteriores hemos preparados los datos para este momento, aquí vamos a: entrenar los modelos, ver las métricas, ver la importancia de las variables, el "permutation importance" y compararlos. Las comparaciones son entre varios modelos, varias configuraciones de datos y otros parámetros diferentes.

Los pasos que se han seguido son los siguientes:
* Preparar un pipeline con un scaler para hacer uso del modelo.
* Averiguar los mejores parámetros.
* Calcular el "permutation importance"
* Entrenar el modelo, sabiendo ya los mejores parámetros.
* Averiguar la importancia de las variables en el caso de que sea posible.

Se han hecho pruebas con 2 scalers diferentes, StandardScaler y MinMaxScaler, teniendo unos resultados claramente mejores con este último.

Los modelos elegidos son:
* Regresión logística
* Random forest
* KNN
* SVC

Las métricas son:
* accuracy
* f1 score
* precision
* recall
* specificity
* roc


La métrica que hemos buscado optimizar ha sido el f1 score. Para la optimización de los modelos nos hemos servido de la implementación de GridSearchCV. Para los diferentes KFolds que se han usado en toda esta última parte hemos optado por usar Stratified KFolds.
