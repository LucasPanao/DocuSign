import db_docu

CODCOLIGADA = [];RA = [];IDPERLET = [];IDHABILITACAOFILIAL = [];CODCONTRATO=[]
CIDADE = [];RG = [];NOMEALUNO = []; UNIDADE = []; SEXO = []; LOCALNASC = []; NOMERESPF = []
ENDERECO = []; CURSO = []; CEP = []; SERIE = []; PERIODO = []; NATURALIDADE = []; DATANASC = []
TELR = []; TELC = []; UF = []; BAIRRO = []; PAI = []; MAE = []; RA_ALUNO = []; CPF = []
def start_variables_envelope():
    db_docu.select = '''SELECT TOP (5) 
        CT.CODCOLIGADA
    ,	CT.IDHABILITACAOFILIAL
    ,	CT.IDPERLET
    ,	CT.RA
    ,	CT.CODCONTRATO
    FROM
        BD20200619_DSV.DBO.SCONTRATO CT INNER JOIN BD20200619_DSV.dbo.VW_ZZ_ALUNO_CONTRATO VW	ON
                                        CT.CODCOLIGADA			=	VW.CODCOLIGADA
                                    AND CT.IDHABILITACAOFILIAL	=	VW.IDHABILITACAOFILIAL
                                    AND CT.IDPERLET				=	VW.IDPERLET
                                    AND CT.RA					=	VW.RA
                                    AND	CT.CODCONTRATO			=	VW.CODCONTRATO
                                        INNER JOIN BD20200619_DSV.dbo.PPESSOA PP				ON
                                        VW.CODPESSOA			=	PP.CODIGO
                                        INNER JOIN BD20200619_DSV.dbo.FCFO	FC					ON
										FC.CODCFO				=	VW.CODCFO
    WHERE
        CT.IDPERLET				=	'44'
    AND CT.ASSINADO				=	'N'
                        '''
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
    db_docu.select = '''SELECT TOP (5) 
    	VW.CIDADE_ALUNO		[CIDADE]
    ,   PP.CARTIDENTIDADE	[RG]
    ,	VW.ALUNO			[NOMEALUNO]
    ,	VW.UNIDADE
    ,	VW.SEXO
    ,	VW.NATURALIDADE		[LOCALNASC]
    ,	VW.RESPFIN			[NOMERESPF]
    ,	FC.RUA + ' '+ FC.NUMERO + ' ' + FC.COMPLEMENTO [ENDERECO]
    ,	VW.NOME_CURSO		[CURSO]
    ,	VW.CEP_ALUNO		[CEP]
    ,	VW.NOME_SERIE		[SEIRE]
    ,	VW.PERIODO
    ,	VW.NATURALIDADE		
    ,	CONVERT(VARCHAR(10),PP.DTNASCIMENTO,103)		[DATANASC]
    ,	VW.RESPFIN_TEL		[TELR]
    ,	VW.TEL1_ALUNO		[TELC]
    ,	VW.ESTADONATAL		[UF]
    ,	VW.BAIRRO_ALUNO		[BAIRRO]
    ,	VW.NOME_PAI			[PAI]
    ,	VW.NOME_MAE			[MAE]
    ,	CT.RA
    ,	VW.RESPFIN_CPF
    FROM
        BD20200619_DSV.DBO.SCONTRATO CT INNER JOIN BD20200619_DSV.dbo.VW_ZZ_ALUNO_CONTRATO VW	ON
                                        CT.CODCOLIGADA			=	VW.CODCOLIGADA
                                    AND CT.IDHABILITACAOFILIAL	=	VW.IDHABILITACAOFILIAL
                                    AND CT.IDPERLET				=	VW.IDPERLET
                                    AND CT.RA					=	VW.RA
                                    AND	CT.CODCONTRATO			=	VW.CODCONTRATO
                                        INNER JOIN BD20200619_DSV.dbo.PPESSOA PP				ON
                                        VW.CODPESSOA			=	PP.CODIGO
                                        INNER JOIN BD20200619_DSV.dbo.FCFO	FC					ON
										FC.CODCFO				=	VW.CODCFO
    WHERE
        CT.IDPERLET				=	'44'
    AND CT.ASSINADO				=	'N'
                    '''
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
