from application.model.entity.estado import Estado
from application.model.dao.noticia_dao import NoticiaDao
noticias = NoticiaDao()
class EstadoDao:
  def __init__(self):
    self.estado_rio = Estado(1, "Rio de Janeiro", "RJ",
        'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-rio-de-janeiro.png',noticias.noticia_rio_lista)

    self.estado_acre = Estado(
      2, "Acre", "AC", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-acre.png',noticias.noticia_acre_lista)

    self.estado_alagoas = Estado(
      3, "Alagoas", "AL", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-alagoas.png',noticias.noticia_alagoas_lista)

    self.estado_amapa = Estado(
      4, "Amapá", "AP", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-amapa.png',noticias.noticia_amapa_lista)

    self.estado_amazonas = Estado(
      5, "Amazonas", "AM", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-amazonas.png',noticias.noticia_amazonas_lista)

    self.estado_bahia = Estado(
      6, "Bahia", "BA", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-bahia.png',noticias.noticia_bahia_lista)

    self.estado_ceara = Estado(
      7, "Ceará", "CE", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-ceara.png',noticias.noticia_ceara_lista)

    self.estado_espirito_santo = Estado(
      8, "Espírito Santo", "ES", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-espirito-santo.png',noticias.noticia_espirito_santo_lista)

    self.estado_goias = Estado(
      9, "Goiás", "GO", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-goias.png',noticias.noticia_goias_lista)

    self.estado_maranhao = Estado(
      10, "Maranhão", "MA", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-do-maranhao.png',noticias.noticia_maranhao_lista)

    self.estado_mato_grosso = Estado(
      11, "Mato Grosso", "MT", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-mato-grosso.png',noticias.noticia_mato_grosso_lista)

    self.estado_mato_grosso_sul = Estado(
      12, "Mato Grosso do Sul", "MS", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-mato-grosso-do-sul.png',noticias.noticia_mato_grosso_sul_lista)

    self.estado_minas_gerais = Estado(
      13, "Minas Gerais", "MG", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-minas-gerais.png',noticias.noticia_minas_gerais_lista)

    self.estado_para = Estado(
      14, "Pará", "PA", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-pa.png',noticias.noticia_para_lista)

    self.estado_paraiba = Estado(
      15, "Paraíba", "PB", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-paraiba.png',noticias.noticia_paraiba_lista)

    self.estado_parana = Estado(
      16, "Paraná", "PR", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-parana.png',noticias.noticia_parana_lista)

    self.estado_pernambuco = Estado(
      17, "Pernambuco", "PE", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-pernambuco.png',noticias.noticia_pernambuco_lista)

    self.estado_piaui = Estado(
      18, "Piauí", "PI", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-piaui.png',noticias.noticia_piaui_lista)

    self.estado_rio_grande_do_norte = Estado(
      19, "Rio Grande do Norte", "RN", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-rio-grande-do-norte.png',noticias.noticia_rio_grande_do_norte_lista)

    self.estado_rio_grande_do_sul = Estado(
      20, "Rio Grande do Sul", "RS", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-rio-grande-do-sul.png',noticias.noticia_rio_grande_do_sul_lista)

    self.estado_randonia = Estado(
      21, "Rondônia", "RO", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-rondonia.png',noticias.noticia_randonia_lista)

    self.estado_roraima = Estado(
      22, "Roraima", "RR", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-de-roraima.png',noticias.noticia_roraima_lista)

    self.estado_santa_catarina = Estado(
      23, "Santa Catarina", "SC", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-santa-catarina.png',noticias.noticia_santa_catarina_lista)

    self.estado_sao_paulo = Estado(
      24, "São Paulo", "SP", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-sao-paulo.png',noticias.noticia_sao_paulo_lista)

    self.estado_sergipe = Estado(
      25, "Sergipe", "SE", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-sergipe.png',noticias.noticia_sergipe_lista)

    self.estado_tocantins = Estado(
      26, "Tocantins", "TO", 'https://www.infoescola.com/wp-content/uploads/2021/02/bandeira-tocantins.png',noticias.noticia_tocantins_lista)

    self.estado_lista = [
      self.estado_rio,
      self.estado_acre,
      self.estado_alagoas,
      self.estado_amapa,
      self.estado_amazonas,
      self.estado_bahia,
      self.estado_ceara,
      self.estado_espirito_santo,
      self.estado_goias,
      self.estado_maranhao,
      self.estado_mato_grosso,
      self.estado_mato_grosso_sul,
      self.estado_minas_gerais,
      self.estado_para,
      self.estado_paraiba,
      self.estado_parana,
      self.estado_pernambuco,
      self.estado_piaui,
      self.estado_rio_grande_do_norte,
      self.estado_rio_grande_do_sul,
      self.estado_randonia,
      self.estado_roraima,
      self.estado_santa_catarina,
      self.estado_sao_paulo,
      self.estado_sergipe,
      self.estado_tocantins
    ]
  
  def get_estado_lista(self):
    return self.estado_lista
