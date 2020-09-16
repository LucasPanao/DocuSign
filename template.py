import os
import requests
import yaml
import json
import pyodbc
from docusign_esign import EnvelopesApi, EnvelopeDefinition, TemplateRole
import base64
import time
from datetime import datetime, timedelta, date
from docusign_esign.client.api_client import ApiClient
import start_var


#### START FUNCTIONS
def get(url,hdr):
    global data
    response = requests.get(url, headers = hdr)
    data = response.json()
    with open('envelope.json', 'w') as f:json.dump(data, f)

def post(url,dataEnv,hdr):
  global envelopeId
  r = requests.post(url,json= dataEnv, headers = hdr)
  print(r.json())
  data = r.json()
  envelopeId = data['envelopeId']
  print(envelopeId)
  return envelopeId

def put():
  url = 'https://demo.docusign.net/restapi/v2.1/accounts/{0}/templates/{1}/recipients/{2}/tabs'.format(signer_client_id,template_id,recipient_id)
  requests.put(url,json= dataTemplate,headers = hdr)
  print('criado com sucesso')

def update_template(i):
  global dataTemplate
  global nome_mes
  nome_mes = ['','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
  dataTemplate = {
    "textTabs": [
        {
          "tabId": "c0d8c73b-fa10-4b0f-b837-f213c520ddd5",
          "tabLabel": "Cidade",
          "value": ""+start_var.CIDADE[i]+""
        },
        {
          "tabId": "ff3f1e19-0a35-4c27-abc2-97a82e6c9ecb",
          "tabLabel": "RG",
          "value": ""+start_var.RESPFIN_RG[i]+""
        },
        {
          "tabId": "691122e1-158d-4ef6-9c7c-56ab2e6e7bb7",
          "tabLabel": "Nome Aluno",
          "value": ""+start_var.NOMEALUNO[i]+""
        },
        {
          "tabId": "df6c1d81-98ba-4d60-b13c-c5886d4ba5f5",
          "tabLabel": "Unidade",
          "value": ""+start_var.UNIDADE[i]+""
        },
        {
          "tabId": "a75c73e3-422b-4aa5-9f8f-fd10cc6c54a4",
          "tabLabel": "Sexo",
          "value": ""+start_var.SEXO[i]+""
        },
        {
          "tabId": "0176bcc5-bce5-4e93-8abe-35a27cfd8114",
          "tabLabel": "Local Nascimento",
          "value": ""+start_var.LOCALNASC[i]+""
        },
        {
          "tabId": "a20d08ae-d5bf-4822-9bfa-b5e0d75fd292",
          "tabLabel": "Nome Resp. Financeiro",
          "value": ""+start_var.NOMERESPF[i]+""
        },
        {
          "tabId": "f7e9ed6f-019c-43b7-a7ae-28b5ac57d2fd",
          "tabLabel": "Endere\u00e7o",
          "value": ""+start_var.ENDERECO[i]+""
        },
        {
          "tabId": "0d09fe4c-4bce-4452-b263-24c8086b6c88",
          "tabLabel": "Curso",
          "value": ""+start_var.CURSO[i]+""
        },
        {
          "tabId": "f4330639-c935-4f47-b966-bdcff568b34d",
          "tabLabel": "CEP",
          "value": ""+start_var.CEP[i]+""
        },
        {
          "tabId": "5ce4531c-cd85-4cb9-bdb5-bd5bab991952",
          "tabLabel": "S\u00e9rie",
          "value": ""+start_var.SERIE[i]+""
        },
        {
          "tabId": "6c2f02de-9d6f-4a37-82bd-dd610f259bd7",
          "tabLabel": "Periodo",
          "value": ""+start_var.PERIODO[i]+""
        },
        {
          "tabId": "f4d5635a-6f17-4d58-9733-2561840a57f5",
          "tabLabel": "Naturalidade",
          "value": ""+start_var.NATURALIDADE[i]+""
        },
        {
          "tabId": "0253e5d4-dbc9-4eab-aa3d-3117a949c3a2",
          "tabLabel": "Data Nasc",
          "value": ""+start_var.DATANASC[i]+""
        },
        {
          "tabId": "9d82230f-c28f-4801-8372-2c5bd8233adf",
          "tabLabel": "Tel Recado",
          "value": ""+start_var.TELR[i]+""
        },
        {
          "tabId": "11a39b1a-ddb9-416f-babf-18b77c22d097",
          "tabLabel": "Telefone C.",
          "value": ""+start_var.TELC[i]+""
        },
        {
          "tabId": "f5ba33d0-dead-4418-bc36-6923c08da655",
          "tabLabel": "UF",
          "value": ""+start_var.UF[i]+""
        },
        {
          "tabId": "04ca7fcb-1816-49ae-8980-c903bb0598f5",
          "tabLabel": "Bairro",
          "value": ""+start_var.BAIRRO[i]+""
        },
        {
          "tabId": "2c835c90-b02b-478e-afb1-112a64def3a6",
          "tabLabel": "Pai",
          "value": ""+start_var.PAI[i]+""
        },
        {
          "tabId": "056fe630-a7e8-440c-8969-e7e4848059c8",
          "tabLabel": "Mae",
          "value": ""+start_var.MAE[i]+""
        },
        {
          "tabId": "146e30de-3592-476d-950a-0becb477dec8",
          "tabLabel": "RA",
          "value": ""+start_var.RA_ALUNO[i]+""
        },
        {
          "tabId": "929009c1-39bd-4dfd-9d85-805f411d3dbc",
          "tabLabel": "Endere\u00e7o",
          "value": ""+start_var.ENDERECO[i]+""
        },
        {
          "tabId": "cd5f8aa9-1d40-42ee-a018-dd1995a9f22f",
          "tabLabel": "ValorBrutoC",
          "value": ""+start_var.VALORT[i]+""
        },
        {
          "tabId": "fd6640aa-0474-4013-8b11-ef453f2be50d",
          "tabLabel": "ValorBrutoCEX",
          "value": ""+start_var.VALORTEX[i]+""
        },
        {
          "tabId": "53d8fdc2-f63d-4928-a427-307af6b45102",
          "tabLabel": "ValorParcelaC",
          "value": ""+start_var.VALORP[i]+""
        },
        {
          "tabId": "2e98660d-86f4-4bfa-9b10-07fc41eede28",
          "tabLabel": "ValorParcelaCEX",
          "value": ""+start_var.VALORPEX[i]+""
        },
        {
          "tabId": "4a98c742-6ca6-4cbb-87a9-4eb49a8615d0",
          "tabLabel": "Nome Resp. Financeiro",
          "value": ""+start_var.NOMERESPF[i]+""
        },
        {
          "tabId": "28e6eede-dd3f-4574-9294-f5d49d91e97a",
          "tabLabel": "CPF",
          "value": ""+start_var.CPF[i]+""
        },
        {
          "tabId": "3ab10a48-a5c5-4a80-a2f1-c793df800468",
          "tabLabel": "Nome Aluno",
          "value": ""+start_var.NOMEALUNO[i]+""
        },
        {
          "tabId": "ce7b0957-887c-4fa3-8fcb-c849bd98d409",
          "tabLabel": "CIDADECOLIGADA",
          "value": ""+start_var.CIDADE_COLIGADA[i]+""
        },
        {
          "tabId": "5cb7f519-f1a1-45c4-b1d9-1418538ff113",
          "tabLabel": "NOMEFANTASIA",
          "value": ""+start_var.NOMEFANTASIA[i]+""
        },
        {
          "tabId": "a409b4a7-6586-4d39-b6a8-9732353ef5cb",
          "tabLabel": "RG",
          "value": ""+start_var.RESPFIN_RG[i]+""
        },
        {
          "tabId": "95acaa1b-0f87-46bc-a152-82751668032a",
          "tabLabel": "CURSO",
          "value": ""+start_var.CURSO[i]+""
        },
        {
          "tabId": "4d638d5f-70d0-4099-8ee6-1dcec98efcb5",
          "tabLabel": "ANOLETIVO",
          "value": ""+start_var.ANOLETIVO[i]+""
        },
        
        ## MATERIAL DIDÁTICO ##
        ## MATERIAL DIDÁTICO ##
        {
          "tabId": "4b56506d-f591-4122-a6b0-c5c4557b7486",
          "tabLabel": "Cidade",
          "value": ""+start_var.CIDADE[i]+""
        },
        {
          "tabId": "039825b0-454f-4773-8b42-e49a55d26cdf",
          "tabLabel": "RG",
          "value": ""+start_var.RESPFIN_RG[i]+""
        },
        {
          "tabId": "7b75e723-4476-4a1f-9cc5-34d9cca3cde4",
          "tabLabel": "Nome Aluno",
          "value": ""+start_var.NOMEALUNO[i]+""
        },
        {
          "tabId": "6d16db9f-7f37-4713-b239-a517b8419660",
          "tabLabel": "Unidade",
          "value": ""+start_var.UNIDADE[i]+""
        },
        {
          "tabId": "b0bd9d74-1963-4bee-9f92-64a8708ab11a",
          "tabLabel": "Endere\u00e7o",
          "value": ""+start_var.ENDERECO[i]+""
        },
        {
          "tabId": "df92885b-9b5b-4fe7-868d-7704a6dbe84b",
          "tabLabel": "CEP",
          "value": ""+start_var.CEP[i]+""
        },
        {
          "tabId": "706a49ef-09d5-44ff-a111-32014bfcdaa4",
          "tabLabel": "S\u00e9rie",
          "value": ""+start_var.SERIE[i]+""
        },
        {
          "tabId": "471aa8f2-7d7e-43d5-b6df-5809d9a1fe6a",
          "tabLabel": "UF",
          "value": ""+start_var.UF[i]+""
        },
        {
          "tabId": "06543537-50b4-42cb-be50-8aa6b35a9de9",
          "tabLabel": "Bairro",
          "value": ""+start_var.BAIRRO[i]+""
        },
        {
          "tabId": "8614728c-e722-436f-8cb2-b7fe5ccbbb3a",
          "tabLabel": "Pai",
          "value": ""+start_var.PAI[i]+""
        },
        {
          "tabId": "9c811b5b-aa2e-4750-ba1b-85f598ca189c",
          "tabLabel": "Mae",
          "value": ""+start_var.MAE[i]+""
        },
        {
          "tabId": "f750ead6-0d19-4bfa-9e39-3bc9ef606885",
          "tabLabel": "RA",
          "value": ""+start_var.RA_ALUNO[i]+""
        },
        {
          "tabId": "9fbc4b26-1c0b-4c59-8dde-f9b687fd2aa8",
          "tabLabel": "Curso",
          "value": ""+start_var.CURSO[i]+""
        },
        {
          "tabId": "260e42a3-fdb0-4278-8f70-6db362e410e0",
          "tabLabel": "Periodo",
          "value": ""+start_var.PERIODO[i]+""
        },
        {
          "tabId": "94d2888b-573a-4496-97f5-9457f70f6685",
          "tabLabel": "Nome Resp. Financeiro",
          "value": ""+start_var.NOMERESPF[i]+""
        },
        {
          "tabId": "aefef120-9085-4bde-90c1-4c009705a730",
          "tabLabel": "Telefone C.",
          "value": ""+start_var.TELC[i]+""
        },
        {
          "tabId": "8ca3a87b-299c-4f21-a27b-aef64582cd97",
          "tabLabel": "CPF",
          "value": ""+start_var.CPF[i]+""
        },
        {
          "tabId": "6d9f1565-cc04-4529-9281-a3700e0c5f2a",
          "tabLabel": "CPF",
          "value": ""+start_var.CPF[i]+""
        },
        {
          "tabId": "6658a652-25b0-4fd6-81cc-be580695d17b",
          "tabLabel": "CPF",
          "value": ""+start_var.CPF[i]+""
        },
        {
          "tabId": "8ef91347-d223-4b22-8d83-7742af1af8c4",
          "tabLabel": "Dia",
          "value": ""+str(date.today().day)+""
        },
        {
          "tabId": "89d8317c-415f-4a9c-a99f-b4dfc84d8b52",
          "tabLabel": "Dia",
          "value": ""+str(date.today().day)+""
        },
        {
          "tabId": "d5ede243-7168-4770-90df-8d17aa5daa47",
          "tabLabel": "Dia",
          "value": ""+str(date.today().day)+""
        },
        {
          "tabId": "8b9af311-4516-4577-83c3-96e16e5ac350",
          "tabLabel": "Mes",
          "value": ""+str(nome_mes[date.today().month])+""
        },
        {
          "tabId": "799f8ff4-1895-4619-9a8a-24db75edbcfe",
          "tabLabel": "Mes",
          "value": ""+str(nome_mes[date.today().month])+""
        },
        {
          "tabId": "80170ae5-6da5-4273-8600-9c4d68f9e344",
          "tabLabel": "Mes",
          "value": ""+str(nome_mes[date.today().month])+""
        },
        {
          "tabId": "ab833985-0b6b-4c9d-9b7f-a3a02d882604",
          "tabLabel": "Ano",
          "value": ""+str(date.today().year)+""
        },
        {
          "tabId": "233c9d4f-71c0-40a0-aec3-a8d36f588964",
          "tabLabel": "Ano",
          "value": ""+str(date.today().year)+""
        },
        {
          "tabId": "99d1e6ad-399b-46c2-8349-66610cf86bfa",
          "tabLabel": "ANOLETIVO",
          "value": ""+start_var.ANOLETIVO[i]+""
        },
        {
          "tabId": "bf806383-f974-4f3c-bef8-13cb6b9dd5e0",
          "tabLabel": "ValorBrutoMD",
          "value": ""+start_var.VALORT_MD[i]+""
        },
        {
          "tabId": "735aa650-e945-4191-9dbf-ef4b021fd4e9",
          "tabLabel": "NumeroParcelas",
          "value": ""+start_var.NUMEROPARCELAS_MD[i]+""
        },
        {
          "tabId": "0b080b65-a3a0-4f66-a975-b7174bff7d59",
          "tabLabel": "NumeroParcelasEX",
          "value": ""+start_var.NUMEROPARCELAS_MD_EX[i]+""
        },
        {
          "tabId": "67f5b2f7-3390-45a7-955b-44aa73510aad",
          "tabLabel": "ValorParcelaMD",
          "value": ""+start_var.VALORP_MD[i]+""
        },
        {
          "tabId": "fd827df3-18bf-42bd-9482-f97de7befe82",
          "tabLabel": "ANOLETIVO",
          "value": ""+start_var.ANOLETIVO[i]+""
        },
        

        ## Termo Aditivo ##
        {
          "tabId": "e5e2c3a3-f830-4e04-9ccb-f78680d63754",
          "tabLabel": "Unidade",
          "value": ""+start_var.UNIDADE_AD[i]+""
        },
        {
          "tabId": "7c32521a-2a9d-4b2f-b41e-dd736abb04fe",
          "tabLabel": "Curso",
          "value": ""+start_var.CURSO_AD[i]+""
        },
        {
          "tabId": "023223fb-3062-486b-b368-8a1b03383c09",
          "tabLabel": "RA",
          "value": ""+start_var.RA_AD[i]+""
        },
        {
          "tabId": "57039aff-fe69-49d6-b469-3659ec4833e9",
          "tabLabel": "Nome Aluno",
          "value": ""+start_var.NOME_AD[i]+""
        },
        {
          "tabId": "b59962f2-3d31-47da-ad25-70d12136fa91",
          "tabLabel": "Dia",
          "value": ""+str(date.today().day)+""
        },
        {
          "tabId": "2b0dcb22-1948-44ae-9439-c4a6280a4a50",
          "tabLabel": "Mes",
          "value": ""+str(nome_mes[date.today().month])+""
        },
        {
          "tabId": "1a5d1b01-8fc3-4c93-bdd4-d5f222f6341f",
          "tabLabel": "Ano",
          "value": ""+str(date.today().year)+""
        },
        {
          "tabId": "8db17200-a55d-4d8c-a95e-380522f821fa",
          "tabLabel": "Ano",
          "value": ""+str(date.today().year)+""
        },
        {
          "tabId": "a3ae4406-b400-43b1-90e1-f7ea7d05f959",
          "tabLabel": "Ano",
          "value": ""+str(date.today().year)+""
        },
        {
          "tabId": "5dea020e-c42d-4697-9925-dd4c446edafc",
          "tabLabel": "Nome Resp. Financeiro",
          "value": ""+start_var.RESP_AD[i]+""
        },
        {
          "tabId": "36a9fe99-189b-4b33-8644-d0ddb59c52f4",
          "tabLabel": "RG",
          "value": ""+start_var.RG_AD[i]+""
        },
        {
          "tabId": "3224c534-c673-427c-bdd8-1ec870ac67c6",
          "tabLabel": "CPF",
          "value": ""+start_var.CPF_AD[i]+""
        },
        {
          "tabId": "3e920a95-fad0-4d77-b9a6-22064e11dd1f",
          "tabLabel": "CodContrato",
          "value": ""+start_var.CODCONTRATO_AD[i]+""
        },
        {
          "tabId": "512f414d-2a37-47c9-a999-765869f276bc",
          "tabLabel": "NOMEFANTASIA",
          "value": ""+start_var.NOMEFANTASIA_AD[i]+""
        },
        {
          "tabId": "85bf6c7b-9dfd-4cf0-a6e2-61f59d769c63",
          "tabLabel": "NOMEFANTASIA",
          "value": ""+start_var.NOMEFANTASIA_AD[i]+""
        },
        {
          "tabId": "2af402f3-0f10-4d57-ab77-85895e965969",
          "tabLabel": "ANOLETIVO",
          "value": ""+start_var.ANOLETIVO[i]+""
        },        
        ### MATRIZ TERMO ADITIVO ###
        {
          "tabId": "901b0d1d-4cea-46e9-a894-0f4b7a81bb0e",
          "tabLabel": "BOLSA1",
          "value": ""+start_var.BOLSA1[i]+""
        },
        {
          "tabId": "e936594c-6ff3-48e8-bac1-b636353d644e",
          "tabLabel": "BOLSA2",
          "value": ""+start_var.BOLSA2[i]+""
        },
        {
          "tabId": "500efe86-17cc-4088-a2a0-57fec6487270",
          "tabLabel": "BOLSA3",
          "value": ""+start_var.BOLSA3[i]+""
        },
        {
          "tabId": "70f5a0e2-0015-44c3-8d3f-ebf36b62f740",
          "tabLabel": "BOLSA4",
          "value": ""+start_var.BOLSA4[i]+""
        },
        {
          "tabId": "49a7b18f-3a20-4e7f-b122-243a1450e257",
          "tabLabel": "BOLSA5",
          "value": ""+start_var.BOLSA5[i]+""
        },
        {
          "tabId": "27d18d83-d52e-4fd3-8840-b860497f7b6f",
          "tabLabel": "BOLSA6",
          "value": ""+start_var.BOLSA6[i]+""
        },
        {
          "tabId": "8b55a016-74f8-4478-bfc2-929d47818a64",
          "tabLabel": "BOLSA7",
          "value": ""+start_var.BOLSA7[i]+""
        },
        {
          "tabId": "21906dd0-ef2c-4618-843c-06128a3caea5",
          "tabLabel": "BOLSA8",
          "value": ""+start_var.BOLSA8[i]+""
        },
        {
          "tabId": "f55fc742-7d9f-46c7-af1f-ecd18a0c4997",
          "tabLabel": "BOLSA9",
          "value": ""+start_var.BOLSA9[i]+""
        },
        {
          "tabId": "74e924bb-4099-494d-a6ba-ad14064d171b",
          "tabLabel": "BOLSA10",
          "value": ""+start_var.BOLSA10[i]+""
        },
        {
          "tabId": "2903ff1b-0079-42c6-b793-9cec5c08f2db",
          "tabLabel": "BOLSA11",
          "value": ""+start_var.BOLSA11[i]+""
        },
        {
          "tabId": "406385e9-f0de-4a98-bf34-77857be762b4",
          "tabLabel": "BOLSA12",
          "value": ""+start_var.BOLSA12[i]+""
        },
        {
          "tabId": "ed1c882b-bb1a-42c2-8c80-859b766cbcb9",
          "tabLabel": "BOLSA13",
          "value": ""+start_var.BOLSA13[i]+""
        },
        {
          "tabId": "0cd339ec-bedb-417c-99c4-948f5c67aaa9",
          "tabLabel": "VALB1",
          "value": ""+start_var.VALB[i]+""
        },
        {
          "tabId": "8d2e806f-1940-4842-bf3a-56404b0462ab",
          "tabLabel": "VALB2",
          "value": ""+start_var.VALB2[i]+""
        },
        {
          "tabId": "f108764e-d3f8-47fe-b128-3f7fcf545161",
          "tabLabel": "VALB3",
          "value": ""+start_var.VALB3[i]+""
        },
        {
          "tabId": "a287e0e7-9f52-4bff-ab7d-6a56ec1281f7",
          "tabLabel": "VALB4",
          "value": ""+start_var.VALB4[i]+""
        },
        {
          "tabId": "7d7df6cf-b37d-4494-b0f6-2f653529cb81",
          "tabLabel": "VALB5",
          "value": ""+start_var.VALB5[i]+""
        },
        {
          "tabId": "7d66cffe-3d00-417e-833b-d8acbba22e71",
          "tabLabel": "VALB6",
          "value": ""+start_var.VALB6[i]+""
        },
        {
          "tabId": "76264a1c-5ea8-40b1-82a2-d298784778b6",
          "tabLabel": "VALB7",
          "value": ""+start_var.VALB7[i]+""
        },
        {
          "tabId": "0b073997-1969-4b20-9684-cd2b5be94942",
          "tabLabel": "VALB8",
          "value": ""+start_var.VALB8[i]+""
        },
        {
          "tabId": "14cfd4df-7b49-44f2-a144-b50af3365830",
          "tabLabel": "VALB9",
          "value": ""+start_var.VALB9[i]+""
        },
        {
          "tabId": "bb2d71f4-2b5d-4dee-a2e5-a7e35543702a",
          "tabLabel": "VALB10",
          "value": ""+start_var.VALB10[i]+""
        },
        {
          "tabId": "254ee055-faff-4363-a2fe-898484dded2d",
          "tabLabel": "VALB11",
          "value": ""+start_var.VALB11[i]+""
        },
        {
          "tabId": "437d73a2-8da8-40a6-a250-3e1a0432d85a",
          "tabLabel": "VALB12",
          "value": ""+start_var.VALB12[i]+""
        },
        {
          "tabId": "b7896fa3-f721-413f-b5f0-a07022ff918c",
          "tabLabel": "VALB13",
          "value": ""+start_var.VALB13[i]+""
        },
        {
          "tabId": "8152b4be-3dfb-4799-a65a-6749b3cd1e80",
          "tabLabel": "VALDESC1",
          "value": ""+start_var.VALDESC1[i]+""
        },
        {
          "tabId": "c4488ee6-a772-4202-9bbe-219c1feeedf9",
          "tabLabel": "VALDESC2",
          "value": ""+start_var.VALDESC2[i]+""
        },
        {
          "tabId": "c30f9ef1-78c9-416b-b347-2a3b08af1be4",
          "tabLabel": "VALDESC3",
          "value": ""+start_var.VALDESC3[i]+""
        },
        {
          "tabId": "cb72cb03-5445-4ece-88ae-e1a9ca2ecb7e",
          "tabLabel": "VALDESC4",
          "value": ""+start_var.VALDESC4[i]+""
        },
        {
          "tabId": "c9c06e2d-e33a-4ad8-b0a3-ad7e2d939f3f",
          "tabLabel": "VALDESC5",
          "value": ""+start_var.VALDESC5[i]+""
        },
        {
          "tabId": "2b7f53d6-222f-4d33-ae1f-4087d4d03402",
          "tabLabel": "VALDESC6",
          "value": ""+start_var.VALDESC6[i]+""
        },
        {
          "tabId": "ff590ac1-9ae5-45bc-8105-1a8509bc7934",
          "tabLabel": "VALDESC7",
          "value": ""+start_var.VALDESC7[i]+""
        },
        {
          "tabId": "a391b47c-0f95-4cd2-9acd-2a0794d0c8b4",
          "tabLabel": "VALDESC8",
          "value": ""+start_var.VALDESC8[i]+""
        },
        {
          "tabId": "1144f8b1-b5da-43b2-898b-bec44ee28c71",
          "tabLabel": "VALDESC9",
          "value": ""+start_var.VALDESC9[i]+""
        },
        {
          "tabId": "96cba413-6a34-47bd-8985-c0bc1df1da71",
          "tabLabel": "VALDESC10",
          "value": ""+start_var.VALDESC10[i]+""
        },
        {
          "tabId": "e153237b-03a2-4b32-8d13-816779bdc65b",
          "tabLabel": "VALDESC11",
          "value": ""+start_var.VALDESC11[i]+""
        },
        {
          "tabId": "eaf8899c-f4a3-4825-8f6b-b1ed7f8b73c8",
          "tabLabel": "VALDESC12",
          "value": ""+start_var.VALDESC12[i]+""
        },
        {
          "tabId": "69868a88-9a6a-41fe-a721-073ddc3c952f",
          "tabLabel": "VALDESC13",
          "value": ""+start_var.VALDESC13[i]+""
        },
        {
          "tabId": "9ccf14d8-2026-4d37-90e0-fcaf442ebe4b",
          "tabLabel": "VALLQ1",
          "value": ""+start_var.VALLQ1[i]+""
        },
        {
          "tabId": "25380beb-e23a-4d86-bad7-4d9d259dbc97",
          "tabLabel": "VALLQ2",
          "value": ""+start_var.VALLQ2[i]+""
        },
        {
          "tabId": "4321ac0b-fca0-4df0-886c-ad3a8f8c49a6",
          "tabLabel": "VALLQ3",
          "value": ""+start_var.VALLQ3[i]+""
        },
        {
          "tabId": "3413cae1-22f6-45c6-a76c-1e2a6154c630",
          "tabLabel": "VALLQ4",
          "value": ""+start_var.VALLQ4[i]+""
        },
        {
          "tabId": "e146bfb5-5176-40d0-9441-709446615e42",
          "tabLabel": "VALLQ5",
          "value": ""+start_var.VALLQ5[i]+""
        },
        {
          "tabId": "e518d37d-37ba-4dbb-98ca-2ceb15cb0800",
          "tabLabel": "VALLQ6",
          "value": ""+start_var.VALLQ6[i]+""
        },
        {
          "tabId": "69d9a206-735f-4a48-a892-a46a4ea52968",
          "tabLabel": "VALLQ7",
          "value": ""+start_var.VALLQ7[i]+""
        },
        {
          "tabId": "521fcb21-0a9d-4e6e-82e3-64c98fd20e81",
          "tabLabel": "VALLQ8",
          "value": ""+start_var.VALLQ8[i]+""
        },
        {
          "tabId": "5e9cebf7-334f-46fe-9354-e73e1ce08175",
          "tabLabel": "VALLQ9",
          "value": ""+start_var.VALLQ9[i]+""
        },
        {
          "tabId": "453eb037-3652-497a-acd9-0f5ac74d4786",
          "tabLabel": "VALLQ10",
          "value": ""+start_var.VALLQ10[i]+""
        },
        {
          "tabId": "16c10f24-5cf4-4279-9a0a-e24f54ffae4b",
          "tabLabel": "VALLQ11",
          "value": ""+start_var.VALLQ11[i]+""
        },
        {
          "tabId": "3227af0e-7a19-4304-8d36-2bb66575e15c",
          "tabLabel": "VALLQ12",
          "value": ""+start_var.VALLQ12[i]+""
        },
        {
          "tabId": "745c8fd2-7c5b-4cfb-9139-bf0ce2bcf713",
          "tabLabel": "VALLQ13",
          "value": ""+start_var.VALLQ13[i]+""
        },
      ]
    }
  return dataTemplate

#### END FUCTIONS   


#### CONFIG
with open('config.yml') as c:
    config = yaml.safe_load(c)
url = config['my-config']['url']
signer_client_id = config['my-config']['clientId']
basepath = config['my-config']['basepath']
token_only = config['my-config']['token_only']
hdr = config['my-config']['token']
status = config['envelope']['status']
template_id = config['envelope']['template_id']
recipient_id = config['template']['recipient_id']
signer_email = config['signer']['email']
signer_name = config['signer']['name']
cc_email = config['cc']['email']
cc_name = config['cc']['name']
#### END CONFIG

'''
start_var.start_variables_template()
update_template()
url = 'https://demo.docusign.net/restapi/v2.1/accounts/{0}/templates/{1}/recipients/{2}/tabs'.format(signer_client_id,template_id,recipient_id)
response = requests.put(url,json= dataTemplate,headers = hdr)
data = response.json()
with open('custom_tabs.json', 'w') as f:json.dump(data, f)
'''