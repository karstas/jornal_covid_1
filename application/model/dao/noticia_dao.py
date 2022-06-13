from application.model.entity.noticia import Noticia
from application.model.dao.estado_dao import EstadoDao
estados = EstadoDao

class NoticiaDao:
  def __init__(self):
    self.noticia_rio_lista = [
        Noticia(1, "Covid-19: Rio registra mais de 2,9 mil casos na últimas 24h", "A taxa de letalidade para a doença no estado continua estabilizada em 3,47%", estados.estado_rio),
        Noticia(35, "Covid-19: Rio registra mais de 2,9 mil casos na últimas 24h", "A taxa de letalidade para a doença no estado continua estabilizada em 3,47%", estados.estado_rio),
        Noticia(45, "Covid-19: Rio registra mais de 2,9 mil casos na últimas 24h", "A taxa de letalidade para a doença no estado continua estabilizada em 3,47%", estados.estado_rio),
    ]
    self.noticia_acre_lista = [
        Noticia(2, "Covid-19: Acre registra apenas um caso nesta quinta-feira", "O número de infectados subiu para 123.820 em todo o estado", estados.estado_acre)
    ]
    self.noticia_alagoas_lista = [
        Noticia(3, "Alagoas registra mais 2 mortes por Covid", "Secretaria da Saúde informou que contabilizou casos acumulados que foram inseridos no sistema fora do prazo.", estados.estado_alagoas)
    ]
    self.noticia_amapa_lista = [
        Noticia(4, "Covid-19: Amapá registra 2 novos casos e contabiliza uma morte; óbitos chegam a 2.128", "A morte registrada no boletim desta quinta-feira ocorreu no município de Santana. O homem de 51 anos, sem comorbidades, faleceu no domingo", estados.estado_amapa)
    ]  
    self.noticia_amazonas_lista = [
        Noticia(5, "Apesar de 72 novos casos, Amazonas não registra mortes por Covid-19", "De acordo com o boletim, o total de casos registrados chega a 581.566 desde o início da pandemia e o total de mortes permanece em 14.160.", estados.estado_amazonas)
    ]
    self.noticia_bahia_lista = [
        Noticia(6, "Bahia registra 1.092 casos ativos de Covid-19 e 14 óbitos; veja taxas de ocupação dos leitos", "Nas últimas 24h, estado registrou 879 casos conhecidos de coronavírus.", estados.estado_bahia)
    ]
    self.noticia_ceara_lista = [
        Noticia(7, "Número de casos graves e óbitos por Covid caem 99% no Ceará, diz secretaria", "O número de mortes caiu de 934 para 122 entre janeiro e março.", estados.estado_ceara)
    ]
    self.noticia_espirito_santo_lista = [
        Noticia(8, "Máscaras não são mais obrigatórias no Espírito Santo", "Informação foi divulgada pelo governador Renato Casagrande, na tarde desta quarta-feira (6). Máscaras já não eram obrigatórias em locais abertos e academias. Uso ainda será obrigatório em unidades de saúde.", estados.estado_espirito_santo)
    ]
    self.noticia_goias_lista = [
        Noticia(9, "Atualização sobre a Covid-19 em Goiás e doses da vacina já aplicadas", "Levantamento realizado pela SES-GO apurou que, referente à primeira dose, foram aplicadas 5.686.868 doses das vacinas contra a Covid-19 em todo o Estado. Em relação à segunda dose e a dose única, foram vacinadas 4.955.900 pessoas, e 1.882.544 pessoas já receberam a dose de reforço.  Entre as crianças de 5 a 11 anos, 40,08% já receberam uma dose da vacina.", estados.estado_goias)
    ]
    self.noticia_maranhao_lista = [
        Noticia(10, "Vacinação contra a Covid: 161,6 milhões de pessoas estão totalmente imunizadas; quase 80 milhões tomaram a dose de reforço", "No maranhão já é permitido o uso de máscaras", estados.estado_maranhao)
    ]
    self.noticia_mato_grosso_lista = [
        Noticia(11, "A Secretaria de Estado de Saúde (SES-MT) notificou, até a tarde desta quinta-feira (07.04), 728.911 casos confirmados da Covid-19 em Mato Grosso, sendo registrados 14.877 óbitos em decorrência do coronavírus no Estado.", "Foram notificadas 273 novas confirmações de casos de coronavírus no Estado. Dos 728.911 casos confirmados da Covid-19 em Mato Grosso, 253 estão em isolamento domiciliar e 713.213 estão recuperados.", estados.estado_mato_grosso)
    ]
    self.noticia_mato_grosso_sul_lista = [
        Noticia(12, "Imunização contra Covid continua para vários grupos em Campo Grande nesta quinta", "Da 1ª à 4ª dose, a imunização será das 7h30 às 16h45, na Seleta e também nas unidades de saúde da capital.", estados.estado_mato_grosso_sul)
    ]
    self.noticia_minas_gerais_lista = [
        Noticia(13, "Minas Gerais registra 510 casos conhecidos e 8 mortes por Covid em 24 horas", "Atualmente, 53.704 pacientes com a doença estão em acompanhamento no estado.", estados.estado_minas_gerais)
    ]
    self.noticia_para_lista = [
        Noticia(14, "Vacinação contra a Covid-19: Pará recebe remessas com mais 211,9 mil doses", "Chegaram 60 mil doses da vacina Janssen, 91.900 doses da Pfizer pediátrica e outras 60 mil doses de Astrazeneca.", estados.estado_para)
    ]
    self.noticia_paraiba_lista = [
        Noticia(15, "Paraíba registra 254 novos casos de Covid-19 nas últimas 24h; nenhum óbito foi confirmado", "A Secretaria de Estado da Saúde (SES) registrou, nesta quinta-feira (07), 254 casos de Covid-19. Entre os casos confirmados nesse boletim 01 (0,39%) é moderado ou grave e 253 (99,61%) são leves. Agora, a Paraíba totaliza 598.826 casos confirmados da doença, que estão distribuídos por todos os 223 municípios. Até o momento, já foram realizados 1.500.333 testes para diagnóstico da Covid-19.", estados.estado_paraiba)
    ]
    self.noticia_parana_lista = [
        Noticia(16, "O estado do Paraná divulgou nesta quinta-feira (7), 1.605 novos casos de Covid-19 e 19 mortes provocadas pelo coronavírus. 2.249.760 pacientes se recuperaram.", "De acordo com a Secretaria Estadual de Saúde, 10.145.579 milhões de paranaenses receberam, ao menos, uma dose da vacina; 9.144.002 milhões receberam duas doses ou imunizante de dose única.", estados.estado_parana)
    ]
    self.noticia_pernambuco_lista = [
        Noticia(17, "Com mais 1.727 infectados e quatro óbitos por Covid-19, Pernambuco totaliza 903.941 casos e 21.454 mortes", "Entre março de 2020 e esta quarta-feira (6), estado contabilizou 58.379 quadros graves e 845.562 formas leves da doença provocada pelo novo coronavírus.", estados.estado_pernambuco)
    ]
    self.noticia_piaui_lista = [
        Noticia(18, "Mulher de 64 anos morre vítima da Covid e Piauí chega a 7.732 óbitos pela doença desde o início da pandemia", "Os casos confirmados no estado somam 367.852 em todos os municípios piauienses. Já os óbitos pelo novo coronavírus chegam 7.732 casos e foram registrados em 224 municípios.", estados.estado_piaui)
    ]
    self.noticia_rio_grande_do_norte_lista = [
        Noticia(19, "Rio Grande do Norte registra 1.824 casos confirmados e 1.824 óbitos por Covid-19", "muito covid aqui", estados.estado_rio_grande_do_norte)
    ]

    self.noticia_rondonia_lista = [
        Noticia(20, "rondonia não tem informação o suficiente porque o estado é uma ilha, aparentemente", "covid covid covid", estados.estado_randonia)
    ] 
    self.noticia_roraima_lista = [
        Noticia(21, "Roraima registra mais uma morte e confirma 17 novos casos conhecidos de Covid", "Número de vítimas da pandemia chegou a 2.146. Desde o início da pandemia, estado já registrou mais de 155,2 mil infectados. As informações são do boletim dessa segunda-feira (4).", estados.estado_roraima)
    ]
    self.noticia_santa_catarina_lista = [
        Noticia(22, "Coronavírus em SC: Estado confirma 1.683.023 casos, 1.657.649 recuperados e 21.692 mortes", "O Governo do Estado relatou que há um total de 1.683.023 casos confirmados de infecção pelo novo coronavírus em Santa Catarina. Desses, 1.657.649 são considerados recuperados e 3.682 continuam em acompanhamento. O balanço foi divulgado nesta quinta-feira, 7. A doença respiratória causou 21.692 óbitos no estado desde o início da pandemia", estados.estado_santa_catarina)
    ]
    self.noticia_sao_paulo_lista = [
        Noticia(23, "Cidade de São Paulo vê internações em UTI Covid triplicar em 24 horas", "O número de internados em Unidade de Terapia Intensiva (UTI) por Covid-19 em hospitais municipais quase triplicou em apenas 24 horas na capital paulista. Desde dezembro do ano passado, São Paulo enfrenta o surto de influenza H3N2, além do crescimento de casos de coronavírus com o surgimento da variante Ômicron", estados.estado_sao_paulo)
    ]
    self.noticia_sergipe_lista = [
        Noticia(24, "Sergipe registra 52 novos casos conhecidos de Covid-19 e duas mortes", "Desde o início da pandemia, 326.638 pessoas testaram positivo para a doença e 6.329 morreram.", estados.estado_sergipe)
    ]
    self.noticia_tocantins_lista = [
        Noticia(25, "tocantins teve covid também, e é mais ou menos isso", "porque não tem notícias decentes sobre covid de tocantins na internet? descubra aqui", estados.estado_tocantins)
    ]
    self.noticia_rio_grande_do_sul_lista = [
        Noticia(26, "Rio Grande do Sul registra 1.824 casos confirmados e 1.824 óbitos por Covid-19", "muitas mortes nesse lugar", estados.estado_rio_grande_do_sul)
    ]
