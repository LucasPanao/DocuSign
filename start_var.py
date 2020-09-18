import db_docu

CODCOLIGADA = []
RA = []
IDPERLET = []
IDHABILITACAOFILIAL = []
CODCONTRATO = []
CIDADE = []
RG = []
NOMEALUNO = []
UNIDADE = []
SEXO = []
LOCALNASC = []
NOMERESPF = []
ENDERECO = []
CURSO = []
CEP = []
SERIE = []
PERIODO = []
NATURALIDADE = []
DATANASC = []
TELR = []
TELC = []
UF = []
BAIRRO = []
PAI = []
MAE = []
RA_ALUNO = []
CPF = []
CODCONTRATO_ALUNO = []
ANOLETIVO = []
RESP_EMAIL = []
VALORT = []
VALORTEX = []
VALORP = []
VALORPEX = []
CIDADE_COLIGADA = []
NOMEFANTASIA = []
RESPFIN_RG = []
VALORT_MD = []
NUMEROPARCELAS_MD = []
NUMEROPARCELAS_MD_EX = []
VALORP_MD = []

### ARRAYS ADITIVO ###
BOLSA1 = []
BOLSA2 = []
BOLSA3 = []
BOLSA4 = []
BOLSA5 = []
BOLSA6 = []
BOLSA7 = []
BOLSA8 = []
BOLSA9 = []
BOLSA10 = []
BOLSA11 = []
BOLSA12 = []
BOLSA13 = []
VALB = []
VALB2 = []
VALB3 = []
VALB4 = []
VALB5 = []
VALB6 = []
VALB7 = []
VALB8 = []
VALB9 = []
VALB10 = []
VALB11 = []
VALB12 = []
VALB13 = []
VALDESC1 = []
VALDESC2 = []
VALDESC3 = []
VALDESC4 = []
VALDESC5 = []
VALDESC6 = []
VALDESC7 = []
VALDESC8 = []
VALDESC9 = []
VALDESC10 = []
VALDESC11 = []
VALDESC12 = []
VALDESC13 = []
VALLQ1 = []
VALLQ2 = []
VALLQ3 = []
VALLQ4 = []
VALLQ5 = []
VALLQ6 = []
VALLQ7 = []
VALLQ8 = []
VALLQ9 = []
VALLQ10 = []
VALLQ11 = []
VALLQ12 = []
VALLQ13 = []
RA_AD = []
IDHABILITACAOFILIAL_AD = []
CODCOLIGADA_AD = []
IDPERLET_AD = []
CODCONTRATO_AD = []
NOME_AD = []
ANOLETIVO_AD = []
CPF_AD = []
RG_AD = []
RESP_AD = []
UNIDADE_AD = []
CURSO_AD = []
NOMEFANTASIA_AD = []


def start_variables_envelope():
    db_docu.select = "SELECT * FROM VW_DOCU_TOTVS_ENVOLOPE ORDER BY	CODCONTRATO,	RA,	IDHABILITACAOFILIAL,	IDPERLET ,	CODCOLIGADA"
    db_docu.select_sql(db_docu.select)
    for rows in db_docu.rows:
        row = rows.rstrip()
        arrRow = row.split(",")
        CODCOLIGADA.append(arrRow[0])
        RA.append(arrRow[1])
        IDPERLET.append(arrRow[2])
        IDHABILITACAOFILIAL.append(arrRow[3])
        CODCONTRATO.append(arrRow[4])


def start_variables_template():
    db_docu.select = "SELECT * FROM VW_DOCU_TOTVS_CONTRATOS_MD ORDER BY	CODCONTRATO,	RA,	IDHABILITACAOFILIAL,	IDPERLET,	CODCOLIGADA"
    db_docu.select_sql(db_docu.select)
    for rows in db_docu.rows:
        row = rows.rstrip()
        arrRow = row.split(",")
        CIDADE.append(arrRow[0])
        RG.append(arrRow[1])
        NOMEALUNO.append(arrRow[2])
        UNIDADE.append(arrRow[3])
        SEXO.append(arrRow[4])
        LOCALNASC.append(arrRow[5])
        NOMERESPF.append(arrRow[6])
        ENDERECO.append(arrRow[7])
        CURSO.append(arrRow[8])
        CEP.append(arrRow[9])
        SERIE.append(arrRow[10])
        PERIODO.append(arrRow[11])
        NATURALIDADE.append(arrRow[12])
        DATANASC.append(arrRow[13])
        TELR.append(arrRow[14])
        TELC.append(arrRow[15])
        UF.append(arrRow[16])
        BAIRRO.append(arrRow[17])
        PAI.append(arrRow[18])
        MAE.append(arrRow[19])
        RA_ALUNO.append(arrRow[20])
        CPF.append(arrRow[21])
        CODCONTRATO_ALUNO.append(arrRow[22])
        ANOLETIVO.append(arrRow[23])
        RESP_EMAIL.append(arrRow[24])
        VALORT.append(arrRow[25].replace('.', ','))
        VALORTEX.append(arrRow[26])
        VALORP.append(arrRow[27].replace('.', ','))
        VALORPEX.append(arrRow[28])
        CIDADE_COLIGADA.append(arrRow[29])
        NOMEFANTASIA.append(arrRow[30])
        RESPFIN_RG.append(arrRow[31])
        VALORT_MD.append(arrRow[32].replace('.', ','))
        NUMEROPARCELAS_MD.append(arrRow[33])
        NUMEROPARCELAS_MD_EX.append(arrRow[34])
        VALORP_MD.append(arrRow[35].replace('.', ','))


def start_variables_template_aditivo():
    db_docu.select = "SELECT * FROM VW_DOCU_TOTVS_CONTRATOS_ADICIONAL ORDER BY	CODCONTRATO,	RA,	IDHABILITACAOFILIAL,	IDPERLET,	CODCOLIGADA"
    db_docu.select_sql(db_docu.select)
    for rows in db_docu.rows:
        row = rows.rstrip()
        arrRow = row.split(",")
        VALB.append(arrRow[0].replace('.', ','))
        RA_AD.append(arrRow[1])
        IDHABILITACAOFILIAL_AD.append(arrRow[2])
        CODCOLIGADA_AD.append(arrRow[3])
        IDPERLET_AD.append(arrRow[4])
        CODCONTRATO_AD.append(arrRow[5])
        NOME_AD.append(arrRow[6])
        ANOLETIVO_AD.append(arrRow[7])
        RESP_AD.append(arrRow[8])
        CPF_AD.append(arrRow[9])
        RG_AD.append(arrRow[10])
        UNIDADE_AD.append(arrRow[11])
        CURSO_AD.append(arrRow[12])
        BOLSA1.append(arrRow[13])
        BOLSA2.append(arrRow[14])
        BOLSA3.append(arrRow[15])
        BOLSA4.append(arrRow[16])
        BOLSA5.append(arrRow[17])
        BOLSA6.append(arrRow[18])
        BOLSA7.append(arrRow[19])
        BOLSA8.append(arrRow[20])
        BOLSA9.append(arrRow[21])
        BOLSA10.append(arrRow[22])
        BOLSA11.append(arrRow[23])
        BOLSA12.append(arrRow[24])
        BOLSA13.append(arrRow[25])
        VALDESC1.append(arrRow[26].replace('.', ','))
        VALDESC2.append(arrRow[27].replace('.', ','))
        VALDESC3.append(arrRow[28].replace('.', ','))
        VALDESC4.append(arrRow[29].replace('.', ','))
        VALDESC5.append(arrRow[30].replace('.', ','))
        VALDESC6.append(arrRow[31].replace('.', ','))
        VALDESC7.append(arrRow[32].replace('.', ','))
        VALDESC8.append(arrRow[33].replace('.', ','))
        VALDESC9.append(arrRow[34].replace('.', ','))
        VALDESC10.append(arrRow[35].replace('.', ','))
        VALDESC11.append(arrRow[36].replace('.', ','))
        VALDESC12.append(arrRow[37].replace('.', ','))
        VALDESC13.append(arrRow[38].replace('.', ','))
        VALLQ1.append(arrRow[39].replace('.', ','))
        VALLQ2.append(arrRow[40].replace('.', ','))
        VALLQ3.append(arrRow[41].replace('.', ','))
        VALLQ4.append(arrRow[42].replace('.', ','))
        VALLQ5.append(arrRow[43].replace('.', ','))
        VALLQ6.append(arrRow[44].replace('.', ','))
        VALLQ7.append(arrRow[45].replace('.', ','))
        VALLQ8.append(arrRow[46].replace('.', ','))
        VALLQ9.append(arrRow[47].replace('.', ','))
        VALLQ10.append(arrRow[48].replace('.', ','))
        VALLQ11.append(arrRow[49].replace('.', ','))
        VALLQ12.append(arrRow[50].replace('.', ','))
        VALLQ13.append(arrRow[51].replace('.', ','))
        VALB2.append(arrRow[52].replace('.', ','))
        VALB3.append(arrRow[53].replace('.', ','))
        VALB4.append(arrRow[54].replace('.', ','))
        VALB5.append(arrRow[55].replace('.', ','))
        VALB6.append(arrRow[56].replace('.', ','))
        VALB7.append(arrRow[57].replace('.', ','))
        VALB8.append(arrRow[58].replace('.', ','))
        VALB9.append(arrRow[59].replace('.', ','))
        VALB10.append(arrRow[60].replace('.', ','))
        VALB11.append(arrRow[61].replace('.', ','))
        VALB12.append(arrRow[62].replace('.', ','))
        VALB13.append(arrRow[63].replace('.', ','))
        NOMEFANTASIA_AD.append(arrRow[64])