class Estado:   

    def __init__(self, id, nome, uf,img,noticia):
        self.__id = id
        self.__nome = nome
        self.__uf = uf
        self.__img = img
        self.__noticia_lista = noticia
    
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_uf(self):
        return self.__uf

    def get_noticia_lista(self):
        return self.__noticia_lista

    def get_img(self):
        return self.__img
    
    def get_noticia_lista(self):
        return self.__noticia_lista