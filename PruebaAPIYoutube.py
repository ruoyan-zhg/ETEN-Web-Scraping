import csv
from googleapiclient.discovery import build
import os
import json
from googleapiclient.errors import HttpError
import pandas as pd
import AnalisisSentimiento


# NO FUNCIONALES
# API_KEY = 'AIzaSyD8vdwq8_SmkGaTSSVJGc4Fzs2w7OGfc7U' PERMISO DENEGADO # Loffel
# API_KEY = 'AIzaSyBDkbGwmJ7siXkT9l6q7CMaz_IYB2jPJZ4' NO USAR ESTA NO FUNCIONA 
# API_KEY = 'AIzaSyDu24NEirW1WDcMk564p8o8XALiLDU6jEM' NO USAR ESTA NO FUNCIONA  #ETEN 2 
# API_KEY = 'AIzaSyD4Dx59fJ4SkuYo4cdmNFLiqa4aRgVDThg' NO USAR ESTA NO FUNCIONA  #ETEN 3
# API_KEY = 'AIzaSyDJnC9nAKtb9PUwXNccit-YtrJXmSxXfLo' NO USAR ESTA NO FUNCIONA  #ETEN 4
# API_KEY = 'AIzaSyBrk6zx8jN9ffdkbyQZv6f0cVqXPizvK-Q' NO USAR ESTA NO FUNCIONA  #ETEN 5
# API_KEY = 'AIzaSyDDcMR8_oddrAIxJjHxL1cVcc66Ni6g5dU' NO USAR ESTA NO FUNCIONA  #ETEN 6
# API_KEY = 'AIzaSyCqFAJMVEkkLXVXq9NzgvCK4cmEC_VhUrs' NO USAR ESTA NO FUNCIONA  #ETEN 7
# API_KEY = 'AIzaSyAD9mv54ByCNWHKxkW4hAVUJCRGGVaizV4' NO USAR ESTA NO FUNCIONA  #ETEN 8
# API_KEY = 'AIzaSyDiUygE5PWK2A_1LkWhZDQo6ORZNgc8D9Y' NO USAR ESTA NO FUNCIONA  #ETEN 9
# API_KEY = 'AIzaSyB93IGtw5_nuRhcImpAGWRhUc7ranbg6LE' NO USAR ESTA NO FUNCIONA   #ETEN 11
# API_KEY = 'AIzaSyDNIAo7tZbaWzv2wPZfsSybzjmEIn8Irbg'  #ETEN 10
# API_KEY = 'AIzaSyDWHjnOU4-mTntPZHd4-C8qYuYnUGHzW9Y' NO USAR ESTA NO FUNCIONA #ETEN 12
# API_KEY = 'AIzaSyD6ekizqDFNazha_sNZd-00-KcaKnp_tNc' NO USAR ESTA NO FUNCIONA #ETEN 1 V2
# API_KEY = 'AIzaSyBHmAby7HWddjhSfJLgio3STSQZ9q4aQOs' #ETEN 2 V2
# API_KEY = 'AIzaSyBiE65QyeOcEB1J3OkbwaKnOaZCWv7IBOc' #ETEN 3 V2
# API_KEY = 'AIzaSyC4asSJjbO32e0uySXNphACZwohx9DYpug' #ETEN 4 V2
# API_KEY = 'AIzaSyBiDR8IBpQJIkh-cDqEDQpQ86TO-qPFs_U' #ETEN 5 V2
# API_KEY = 'AIzaSyAQexx10CmLOAAyqwm1E9lt7XcksWDuB8I' #ETEN 6 V2
# API_KEY = 'AIzaSyA8wfXv49JRIExaqxij2rCCfW27czY7PyI' #ETEN 7 V2
# API_KEY = 'AIzaSyDYIw9k9YvZyd5b0RxQ6-_NSqbFgFuhAkw' #ETEN 8 V2
# API_KEY = 'AIzaSyCopAl4t4oVUjYhQXyiH1tb2tuFYHa1KYo' #ETEN 9 V2
# API_KEY = 'AIzaSyCeSejd5nETIuEQkrahRHxZ46GLL_DK0YQ' #ETEN 10 V2
# API_KEY = 'AIzaSyAHh7-4RzVrRNqab-3iaU2KOlOalpeaSsA' #ETEN 11 V2
# API_KEY = 'AIzaSyAxj5mMSqMDkZS7eXm1zS_0trbQxhqFox8' #ETEN 12 V2
# API_KEY = 'AIzaSyDb-86QdtAwrZCJMkhgcJ7w_tZqzQz-stA' #ETEN 1 V3
# API_KEY = 'AIzaSyB2BeWLY8wcgfsemfNYt1MS7D6TgVe0abw' #ETEN 2 V3
# API_KEY = 'AIzaSyBM_DJJpFbivg_puvK2dvEkRGhm2Bc95X0' #ETEN 3 V3
# API_KEY = 'AIzaSyCVCmvfHJSAFJCyZAh3y1Gm6aWCqQY0kLc' #ETEN 4 V3
# API_KEY = 'AIzaSyACv6RqbK6ZpnO63s_4FTqcX067zk5zqlQ' #ETEN 5 V3
# API_KEY = 'AIzaSyC86hUyS-otknYht8lSvTzMNwr-fj36j6A' #ETEN 6 V3
# API_KEY = 'AIzaSyA961vapEzZja2d12bf6wqHIgm_SmIOa6A' #ETEN 7 V3
# API_KEY = 'AIzaSyCW2CQIn54WiFI5WnYiJZIN2yVpRNsVXs8' #ETEN 8 V3


# FUNCIONALES
# API_KEY = 'AIzaSyCp9wr43CLpp02FnZPYF4aTi8SuIZ3sE_E'
# API_KEY = 'AIzaSyDSYGd1W9HHIofRBr-DjZLG_GUlbDqLNxQ' # Rober
# API_KEY = 'AIzaSyCs6FGPDPU_EwzwZ-t9rLimZMUcW4BNj80'
# API_KEY = 'AIzaSyBSamf7FvHUAkOkWMKsZmy0uaXXgEEJ7xI'
# API_KEY = 'AIzaSyDfGzMMQi5Kk2c-5fmVlOJHu8HWW2iZO6Y' #ETEN 9 V3
# API_KEY = 'AIzaSyBnruy1PukSyB5r_aAoZmQ7UtmtvuZgRSw' #ETEN 10 V3
# API_KEY = 'AIzaSyCGGupT8tR4QNhDzEuBwWUmoggd8E2W3KM' #ETEN 11 V3
# API_KEY = 'AIzaSyA8uGQQEUvLfenpgyi20GKUAOYlgOfCT6U' #ETEN 12 V3
# API_KEY = 'AIzaSyArVm4ZLq8YdXAIzA3j-qTQ1VEwnrK--fg' #ETEN 1 V4
# API_KEY = 'AIzaSyCpJd-1d941mrg1BAgHf2dMrOJxFv-rtCc' #ETEN 2 V4
# API_KEY = 'AIzaSyDo3cO16DZ5Na9xQ9eA6tZKkqYPYiNpJRM' #ETEN 3 V4
# API_KEY = 'AIzaSyAelcnQ7ingeJj-DVRv1b1SK1Sqy47wX_Y' #ETEN 4 V4
# API_KEY = 'AIzaSyAK99V7N8gNxYKjtYBUApVV8GlZ24uQqtQ' #ETEN 5 V4
API_KEY = 'AIzaSyDofqndIUq4f9Ghni8WPxTRGDT966bVBJg' #ETEN 6 V4
# API_KEY = '' #ETEN 7 V4
# API_KEY = '' #ETEN 8 V4
# API_KEY = '' #ETEN 9 V4
# API_KEY = '' #ETEN 10 V4
# API_KEY = '' #ETEN 11 V4
# API_KEY = '' #ETEN 12 V4



def obtenerComentarios(recetaBuscar):

    # Variable con el texto a buscar en YouTube
    datoBuscar = recetaBuscar

    # Inicializamis nuestr variable youtube con la conexion a youtube, utilizamos la version 3 de la api y nuestra clave o key
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Hacemos la busqueda en youtube la cual nos devuelve una lista con los videos buscados
    # La variable q contiene lo que queremos buscar en youtube
    # La variable part nos devuelve lo que estamos buscando de cada video en nuestro caso el id y el snippet
    # El snippet contiene los metadatos basicos del video, titulo, descripcion, comentarios...
    # La variable type es el tipo de elemento que queremos buscar en nuestro caso video
    # La variable order ordena los videos que estamos buscando en nuestro caso por relevancia,
    # aunque tambien podemos hacerlo por visualizaciones: order='viewCount'
    # La variable maxResults indica la cantidad de videos que queremos buscar
    todosVideos = youtube.search().list(q=datoBuscar, part='id,snippet', type='video', order='relevance',
                                        maxResults=5).execute()

    # Esto se modificara por una BBDD
    rutaJson = 'comentarios.json'
    if os.path.exists(rutaJson):
        if not rutaJson:
            with open(rutaJson, 'r', encoding="utf8") as f:
                data = json.load(f)
        else:
            data = {}
    else:
        data = {}

    # Iteramos por cada uno de los videos obtenidos anteriormente
    for video in todosVideos.get('items', []):
        # Sacamos el id del video (es un string no un int)
        video_id = video['id']['videoId']

        # Guardamos en una variable la url del video al anadirle el id
        video_url = 'https://www.youtube.com/watch?v=' + video_id

        # Variable que contendra todos los comentarios ya tratados
        todosComentarios = []
        # Variable en la que se iran anadiendo cada uno de los comentarios en bruto
        sumaComentarios = []
        try:
            # Guardamos los 100 primeros comentarios en la variable comentariosVideo con formato de texto plano
            # no son realmente los comentarios sino una lista con toda la informacion y metadatos de los comentarios
            comentariosVideo = youtube.commentThreads().list(part="snippet", videoId=video_id, textFormat="plainText",
                                                             maxResults=100).execute()

            # Variable que comprueba si hay mas comentarios
            banderaHayMasComentarios = True

            # Si hay mas de 100 comentarios entrara en el while para sacar todos los comentarios,
            # esto lo hacemos ya que hay un maximo de comentarios asique hay que ir extrayendolos de 100 en 100 para
            # el buen funcionamiento de la API
            while banderaHayMasComentarios:
                sumaComentarios += comentariosVideo["items"]

                # Revisa si hay mas paginas de comentarios, es decir si hay mas comentarios de los que acabamos
                # de anadir a sumaComentarios. Si es asi se vuelven a coger los 100 siguientes como antes, sino
                # se pone en false la banderaHayMasComentarios, para no volver a entrar al bucle, es decir que
                # ya no hay mas comentarios
                if "nextPageToken" in comentariosVideo:
                    comentariosVideo = youtube.commentThreads().list(part="snippet", videoId=video_id,
                                                                     textFormat="plainText", maxResults=100,
                                                                     pageToken=comentariosVideo["nextPageToken"]).execute()
                else:
                    banderaHayMasComentarios = False

            # Por ultimo recorremos la variable de sumaComentarios con todos los metadatos de los comentarios para
            # seleccionar unicamente el texto de estos
            for sumaCom in sumaComentarios:
                # Con la siguiente linea apuntamos a la informacion del comentario gracias a:["snippet"]["topLevelComment"],
                # y extraemos el contenido del cometario con ["snippet"]["textDisplay"]
                comentariosIndividuales = sumaCom["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                # seguidamente la anadimos a nuestra variable que contiene todos los comentarios del video
                todosComentarios.append(comentariosIndividuales)
            # Al terminar de guardar todos los comentarios los metemos en cada uno de los videos dentro de la variable data,
            # creando una estructura json.
            data[video_url] = todosComentarios
            # print(todosComentarios)
        except HttpError as error:
            # Con este except evitamos que falle la busqueda de los videos con un error de http
            # En este if comprobamos la respuesta 403 para ver si el video tiene o no comentarios habilitados
            if error.resp.status == 403 and b"commentsDisabled" in error.content:
                print("Los comentarios estan deshabilitados para el video: " + video_url)
            else:
                print(
                    "Ocurrio un error al obtener los comentarios para el video: " + video_url)

    # Esto se modificara por una BBDD
    with open(rutaJson, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

    print('Comentarios almacenados en el archivo: ' + rutaJson)


# pip install clean-text
# clean(text,no_emoji=True)


datos = pd.read_csv('recetas_csv/df_recetas_gratis_v2.csv',
                    delimiter=';')

# Esto se utiliza para no exceder las peticiones de la api y que no de error
# Se van ejecutando por tramos los csv
# empieza 2 mas que el primero y acaba uno menos que el ultimo
datos_seleccionados = datos.iloc[3240:3250]

for indice, fila in datos_seleccionados.iterrows():

    titulo_recetas = fila['titulo']
    print(titulo_recetas)
    obtenerComentarios(titulo_recetas)

    sentimientoPos, sentimientoNeg = AnalisisSentimiento.analisisSentimiento()
    datos.at[indice, 'sentimientoPos'] = sentimientoPos
    datos.at[indice, 'sentimientoNeg'] = sentimientoNeg


datos.to_csv('recetas_csv/df_recetas_gratis_v2.csv', sep=";", index=False)
