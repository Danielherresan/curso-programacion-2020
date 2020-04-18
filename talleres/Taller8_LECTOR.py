from Funciones import readFile, writeFile, appendLines, showList

mi_opinion = [
    "Primero que nada hay que tener en cuenta que RT es financiada en parte o en su totalidad por el gobierno de la federacion rusa",
    "En mi opinion esta es una de las pocas cosas para las que el Covid-19 fue una buena noticia pues a mi parecer desde que empezo la pandemia las tensiones entre estados unidos e Iran se han ido desescalando, lo cual es bueno.",
    "Ya quedara ver como continuara la situacion luego de esta pandemia."
]

linea_a_anadir = "Esta noticia fue tomada de RT noticias: https://actualidad.rt.com/actualidad/350195-iran-planear-construir-submarinos-nucleares, el 16  de abril del 2020 a las 22:08 GMT "

lineas_noticia = readFile("Noticia.txt")
showList(lineas_noticia)

writeFile("Opinion.txt", mi_opinion)

appendLines("Noticia.txt", linea_a_anadir)