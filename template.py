import os
import requests
import yaml
import json
import pyodbc
import base64
import time
from datetime import datetime, timedelta, date
import start_var

def put(i):
  url = 'https://na2.docusign.net/restapi/v2.1/accounts/{0}/templates/{1}/recipients/{2}/tabs'.format(signer_client_id,template_id,recipient_id)
  requests.put(url,json= dataTemplate,headers = hdr)
  print('Template do aluno(a) {0} criado com sucesso'.format(start_var.NOMEALUNO[i]))

def update_template(i):
  global dataTemplate
  global nome_mes
  nome_mes = ['','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
  dataTemplate = {
    "textTabs": [
        {
          "tabId": "c4bab53f-6b42-49e2-abbc-184312432660",
          "tabLabel": "Cidade",
          "value": ""+start_var.CIDADE[i]+""
        },
        {
          "tabId": "d7843fe0-b736-4845-8baa-460719bc9ea9",
          "tabLabel": "RG",
          "value": ""+start_var.RESPFIN_RG[i]+""
        },
        {
          "tabId": "3c6ea88d-5b60-4dda-9602-1d2975dc2f43",
          "tabLabel": "Nome Aluno",
          "value": ""+start_var.NOMEALUNO[i]+""
        },
        {
          "tabId": "e5b48754-9e3a-42a5-ae72-4d1ada45a396",
          "tabLabel": "Unidade",
          "value": ""+start_var.UNIDADE[i]+""
        },
        {
          "tabId": "1f5c3403-6552-4044-bfac-45944362c093",
          "tabLabel": "Sexo",
          "value": ""+start_var.SEXO[i]+""
        },
        {
          "tabId": "d9f3f9a3-cef2-426e-9f6e-9ea93d7d0b88",
          "tabLabel": "Local Nascimento",
          "value": ""+start_var.LOCALNASC[i]+""
        },
        {
          "tabId": "ad2be82b-cfe2-4d3d-9c95-9dde2810de96",
          "tabLabel": "Nome Resp. Financeiro",
          "value": ""+start_var.NOMERESPF[i]+""
        },
        {
          "tabId": "eb9a784e-e8b9-421e-80a2-35aa9fe9f1b5",
          "tabLabel": "Endere\u00e7o",
          "value": ""+start_var.ENDERECO[i]+""
        },
        {
          "tabId": "f857b9f9-8dad-4c3b-9a22-6c7796bf66a6",
          "tabLabel": "Curso",
          "value": ""+start_var.CURSO[i]+""
        },
        {
          "tabId": "b31dce1d-f35d-4395-86cb-35de0dc6ae56",
          "tabLabel": "CEP",
          "value": ""+start_var.CEP[i]+""
        },
        {
          "tabId": "90d7efb6-aa0e-4fb3-b9ff-d971a863d23c",
          "tabLabel": "S\u00e9rie",
          "value": ""+start_var.SERIE[i]+""
        },
        {
          "tabId": "30961f12-e42d-4901-8ea5-c967bf55de02",
          "tabLabel": "Periodo",
          "value": ""+start_var.PERIODO[i]+""
        },
        {
          "tabId": "f21b0f26-b4be-4e76-a474-daf49e5b4c7b",
          "tabLabel": "Naturalidade",
          "value": ""+start_var.NATURALIDADE[i]+""
        },
        {
          "tabId": "7020834c-6716-465e-a159-40554509ae76",
          "tabLabel": "Data Nasc",
          "value": ""+start_var.DATANASC[i]+""
        },
        {
          "tabId": "97e78851-8748-4bf3-bc14-60e410fd8c4f",
          "tabLabel": "Tel Recado",
          "value": ""+start_var.TELR[i]+""
        },
        {
          "tabId": "b41d3dbb-e69f-4b5c-b434-2ed9afe34603",
          "tabLabel": "Telefone C.",
          "value": ""+start_var.TELC[i]+""
        },
        {
          "tabId": "d2031b37-8381-4fd6-a57d-cd0741ae64af",
          "tabLabel": "UF",
          "value": ""+start_var.UF[i]+""
        },
        {
          "tabId": "b593aff9-b513-4641-a721-77932d775538",
          "tabLabel": "Bairro",
          "value": ""+start_var.BAIRRO[i]+""
        },
        {
          "tabId": "82cdbfd5-1263-41df-b35d-ce37fc03cbb9",
          "tabLabel": "Pai",
          "value": ""+start_var.PAI[i]+""
        },
        {
          "tabId": "99cafb43-4ea1-41dd-bf4f-6a22b244dbba",
          "tabLabel": "Mae",
          "value": ""+start_var.MAE[i]+""
        },
        {
          "tabId": "cf0d304e-4e88-42d1-80c5-d38f674e2c6e",
          "tabLabel": "RA",
          "value": ""+start_var.RA_ALUNO[i]+""
        },
        {
          "tabId": "bb83b0f7-d1f1-4361-9cdf-2d1c9d195916",
          "tabLabel": "Endere\u00e7o",
          "value": ""+start_var.ENDERECO[i]+""
        },
        {
          "tabId": "1499342e-f90f-4bee-befc-4c8f42d5bdbb",
          "tabLabel": "ValorBrutoC",
          "value": ""+start_var.VALORT[i]+""
        },
        {
          "tabId": "9384c335-8ace-4999-85fc-f5ec8c4b0360",
          "tabLabel": "ValorBrutoCEX",
          "value": ""+start_var.VALORTEX[i]+""
        },
        {
          "tabId": "cfece8f6-69d8-46fd-a612-b22ccabd40ba",
          "tabLabel": "ValorParcelaC",
          "value": ""+start_var.VALORP[i]+""
        },
        {
          "tabId": "bd219605-ea9f-4f3c-a7de-19f1e54e63c7",
          "tabLabel": "ValorParcelaCEX",
          "value": ""+start_var.VALORPEX[i]+""
        },
        {
          "tabId": "4a98c742-6ca6-4cbb-87a9-4eb49a8615d0",
          "tabLabel": "Nome Resp. Financeiro",
          "value": ""+start_var.NOMERESPF[i]+""
        },
        {
          "tabId": "b43a1008-90a2-4b84-8cbf-c4421c9ec5db",
          "tabLabel": "CPF",
          "value": ""+start_var.CPF[i]+""
        },
        {
          "tabId": "621364a4-4974-4e2c-9326-c8c978e512d8",
          "tabLabel": "Nome Aluno",
          "value": ""+start_var.NOMEALUNO[i]+""
        },
        {
          "tabId": "473ad2e7-a19b-4fb3-aa45-bc3d473014ec",
          "tabLabel": "CIDADECOLIGADA",
          "value": ""+start_var.CIDADE_COLIGADA[i]+""
        },
        {
          "tabId": "91d7df26-b524-42bd-aa71-9cf3a32820b8",
          "tabLabel": "NOMEFANTASIA",
          "value": ""+start_var.NOMEFANTASIA[i]+""
        },
        {
          "tabId": "31cf3527-3a34-4be2-83dd-9c5a7591db98",
          "tabLabel": "RG",
          "value": ""+start_var.RESPFIN_RG[i]+""
        },
        {
          "tabId": "dbcd497d-fc7d-435d-a6d7-613f2cc570da",
          "tabLabel": "CURSO",
          "value": ""+start_var.CURSO[i]+""
        },
        {
          "tabId": "d2caaa3f-fce6-4f38-99fd-51a8a74ffc5b",
          "tabLabel": "ANOLETIVO",
          "value": ""+start_var.ANOLETIVO[i]+""
        },
        
        ## MATERIAL DIDÁTICO ##
        ## MATERIAL DIDÁTICO ##
        {
          "tabId": "55a6aaac-b4ed-4f64-830f-15b7b30b871b",
          "tabLabel": "Cidade",
          "value": ""+start_var.CIDADE[i]+""
        },
        {
          "tabId": "cf49fd62-025e-4af9-842d-7079df6de789",
          "tabLabel": "RG",
          "value": ""+start_var.RESPFIN_RG[i]+""
        },
        {
          "tabId": "2c91f735-8795-474a-9553-3e99ee4336a3",
          "tabLabel": "Nome Aluno",
          "value": ""+start_var.NOMEALUNO[i]+""
        },
        {
          "tabId": "3f306232-1696-44fe-8ea3-1f0852399f7c",
          "tabLabel": "Unidade",
          "value": ""+start_var.UNIDADE[i]+""
        },
        {
          "tabId": "185612e8-3118-4900-8c8f-941465d08f1c",
          "tabLabel": "Endere\u00e7o",
          "value": ""+start_var.ENDERECO[i]+""
        },
        {
          "tabId": "853df0f2-3bd4-4a1b-bc72-11b4978d7638",
          "tabLabel": "CEP",
          "value": ""+start_var.CEP[i]+""
        },
        {
          "tabId": "60efe4a1-77c2-46a6-9831-52eda14fec26",
          "tabLabel": "S\u00e9rie",
          "value": ""+start_var.SERIE[i]+""
        },
        {
          "tabId": "1b8320b0-ff86-463c-94da-c3c2a123512b",
          "tabLabel": "UF",
          "value": ""+start_var.UF[i]+""
        },
        {
          "tabId": "62ff1952-e951-4c71-b009-302f928a7767",
          "tabLabel": "Bairro",
          "value": ""+start_var.BAIRRO[i]+""
        },
        {
          "tabId": "4fb0d893-0171-46e2-a9d1-a9d039a5deb5",
          "tabLabel": "Pai",
          "value": ""+start_var.PAI[i]+""
        },
        {
          "tabId": "d1a06467-cf5e-466c-b576-efe58f096ce0",
          "tabLabel": "Mae",
          "value": ""+start_var.MAE[i]+""
        },
        {
          "tabId": "55bc4dbe-0c4e-48cc-9772-8f43ae7f80df",
          "tabLabel": "RA",
          "value": ""+start_var.RA_ALUNO[i]+""
        },
        {
          "tabId": "821e933f-c5aa-420c-ac61-c0bf12cb227c",
          "tabLabel": "Curso",
          "value": ""+start_var.CURSO[i]+""
        },
        {
          "tabId": "1f1cedaf-b506-450d-83fd-32f05f4b4002",
          "tabLabel": "Periodo",
          "value": ""+start_var.PERIODO[i]+""
        },
        {
          "tabId": "06a41ff3-60c5-45b0-9ab7-813656a5655b",
          "tabLabel": "Nome Resp. Financeiro",
          "value": ""+start_var.NOMERESPF[i]+""
        },
        {
          "tabId": "596201a9-fbe8-49bd-9757-60bf2c0dc7fa",
          "tabLabel": "Telefone C.",
          "value": ""+start_var.TELC[i]+""
        },
        {
          "tabId": "1b1540f6-a89e-4838-95fb-8ce45b6c34dc",
          "tabLabel": "CPF",
          "value": ""+start_var.CPF[i]+""
        },
        {
          "tabId": "3e67efa4-d967-4962-8a6d-af89db5abe81",
          "tabLabel": "CPF",
          "value": ""+start_var.CPF[i]+""
        },
        {
          "tabId": "be452647-4e01-42b5-9b33-28b7e237a176",
          "tabLabel": "CPF",
          "value": ""+start_var.CPF[i]+""
        },
        {
          "tabId": "85fbb024-6e6d-43ef-8e5a-5c816fc1fca3",
          "tabLabel": "Dia",
          "value": ""+str(date.today().day)+""
        },
        {
          "tabId": "904af196-2afc-4c14-96f0-d8937bfd8827",
          "tabLabel": "Dia",
          "value": ""+str(date.today().day)+""
        },
        {
          "tabId": "11b16376-764d-4508-a70b-4ea591b12e9b",
          "tabLabel": "Dia",
          "value": ""+str(date.today().day)+""
        },
        {
          "tabId": "09fba5e4-60d3-46cd-909d-5db4a685c400",
          "tabLabel": "Mes",
          "value": ""+str(nome_mes[date.today().month])+""
        },
        {
          "tabId": "84e51fa1-0920-418e-b407-e535258670d4",
          "tabLabel": "Mes",
          "value": ""+str(nome_mes[date.today().month])+""
        },
        {
          "tabId": "d51143b1-4a34-4c66-88fb-e28ae4dd8526",
          "tabLabel": "Mes",
          "value": ""+str(nome_mes[date.today().month])+""
        },
        {
          "tabId": "c7d2a493-22df-463e-a49b-87399f521a4b",
          "tabLabel": "Ano",
          "value": ""+str(date.today().year)+""
        },
        {
          "tabId": "7942e0c4-5cde-46e0-a3b3-228fed57195a",
          "tabLabel": "Ano",
          "value": ""+str(date.today().year)+""
        },
        {
          "tabId": "18f389d9-4eb7-4094-b585-df1d54d0351a",
          "tabLabel": "ANOLETIVO",
          "value": ""+start_var.ANOLETIVO[i]+""
        },
        {
          "tabId": "f8172c50-40fc-4096-85ac-4c3ed80c85fb",
          "tabLabel": "ValorBrutoMD",
          "value": ""+start_var.VALORT_MD[i]+""
        },
        {
          "tabId": "b338eb00-97d9-4fe6-9fad-5f891c51400a",
          "tabLabel": "NumeroParcelas",
          "value": ""+start_var.NUMEROPARCELAS_MD[i]+""
        },
        {
          "tabId": "11077707-a0f9-455f-ac1e-54b872e61905",
          "tabLabel": "NumeroParcelasEX",
          "value": ""+start_var.NUMEROPARCELAS_MD_EX[i]+""
        },
        {
          "tabId": "4e104f77-26aa-4e2c-9031-aa1c31a024b1",
          "tabLabel": "ValorParcelaMD",
          "value": ""+start_var.VALORP_MD[i]+""
        },
        {
          "tabId": "11d63eb0-a17c-4e87-9903-ad682d02035a",
          "tabLabel": "ANOLETIVO",
          "value": ""+start_var.ANOLETIVO[i]+""
        },
        

        ## Termo Aditivo ##
        {
          "tabId": "c202b94f-7c3c-4946-aeab-684f491a9f07",
          "tabLabel": "Unidade",
          "value": ""+start_var.UNIDADE_AD[i]+""
        },
        {
          "tabId": "50e2efde-603c-43a4-bbfd-11ac3fdfafc3",
          "tabLabel": "Curso",
          "value": ""+start_var.CURSO_AD[i]+""
        },
        {
          "tabId": "e613ca6c-0f1e-4a3d-aa4f-513cf8d4e9db",
          "tabLabel": "RA",
          "value": ""+start_var.RA_AD[i]+""
        },
        {
          "tabId": "f4bd6a9b-03fe-42df-b2e5-1412d88d6201",
          "tabLabel": "Nome Aluno",
          "value": ""+start_var.NOME_AD[i]+""
        },
        {
          "tabId": "8be33873-e073-4ff7-aaaf-62f6df16bd75",
          "tabLabel": "Dia",
          "value": ""+str(date.today().day)+""
        },
        {
          "tabId": "c8399881-2877-427b-8131-2df8725f276a",
          "tabLabel": "Mes",
          "value": ""+str(nome_mes[date.today().month])+""
        },
        {
          "tabId": "53c4113c-b0bf-4691-bc48-660451aaad2a",
          "tabLabel": "Ano",
          "value": ""+str(date.today().year)+""
        },
        {
          "tabId": "743f76cb-2615-41f7-80fd-fdca424296e8",
          "tabLabel": "Ano",
          "value": ""+str(date.today().year)+""
        },
        {
          "tabId": "d0374d8f-70bf-40ac-a007-db18acf672a9",
          "tabLabel": "Ano",
          "value": ""+str(date.today().year)+""
        },
        {
          "tabId": "39404c20-ac9b-4946-b4b5-f272de6ec54d",
          "tabLabel": "Nome Resp. Financeiro",
          "value": ""+start_var.RESP_AD[i]+""
        },
        {
          "tabId": "5f409bb7-195a-4fe0-b5b5-85b638d64262",
          "tabLabel": "RG",
          "value": ""+start_var.RG_AD[i]+""
        },
        {
          "tabId": "20bb3f5e-9ab5-429f-ae74-a262aeb8f2d1",
          "tabLabel": "CPF",
          "value": ""+start_var.CPF_AD[i]+""
        },
        {
          "tabId": "7335257a-e0eb-4729-b052-a1fc4c3e176a",
          "tabLabel": "CodContrato",
          "value": ""+start_var.CODCONTRATO_AD[i]+""
        },
        {
          "tabId": "2ccabb10-850a-4ce2-b037-67ec4165a493",
          "tabLabel": "NOMEFANTASIA",
          "value": ""+start_var.NOMEFANTASIA_AD[i]+""
        },
        {
          "tabId": "d14513f2-934b-4d99-b6ce-2cf479e4cc3c",
          "tabLabel": "NOMEFANTASIA",
          "value": ""+start_var.NOMEFANTASIA_AD[i]+""
        },
        {
          "tabId": "18f389d9-4eb7-4094-b585-df1d54d0351a",
          "tabLabel": "ANOLETIVO",
          "value": ""+start_var.ANOLETIVO[i]+""
        },        
        ### MATRIZ TERMO ADITIVO ###
        {
          "tabId": "3660bd06-4b0c-479c-90f2-25bada89f909",
          "tabLabel": "BOLSA1",
          "value": ""+start_var.BOLSA1[i]+""
        },
        {
          "tabId": "83dc1e8b-f4c6-436c-82d3-4f26f1f55c51",
          "tabLabel": "BOLSA2",
          "value": ""+start_var.BOLSA2[i]+""
        },
        {
          "tabId": "caa24a83-2eb1-4e76-a8dc-ed075726e174",
          "tabLabel": "BOLSA3",
          "value": ""+start_var.BOLSA3[i]+""
        },
        {
          "tabId": "499dd14c-88bf-49e2-9d67-b7491b80d997",
          "tabLabel": "BOLSA4",
          "value": ""+start_var.BOLSA4[i]+""
        },
        {
          "tabId": "e722ff0b-e5bc-4291-b528-77c25eface33",
          "tabLabel": "BOLSA5",
          "value": ""+start_var.BOLSA5[i]+""
        },
        {
          "tabId": "9f5caeb5-2a78-4c0d-beb6-524bbe6a691d",
          "tabLabel": "BOLSA6",
          "value": ""+start_var.BOLSA6[i]+""
        },
        {
          "tabId": "1728b3ee-9241-4ae7-96cc-818c592b5fbf",
          "tabLabel": "BOLSA7",
          "value": ""+start_var.BOLSA7[i]+""
        },
        {
          "tabId": "8a5bb6d8-53cb-4287-b3c1-9856ca421735",
          "tabLabel": "BOLSA8",
          "value": ""+start_var.BOLSA8[i]+""
        },
        {
          "tabId": "db54c3fc-7f4d-448f-aa07-8178d72876e8",
          "tabLabel": "BOLSA9",
          "value": ""+start_var.BOLSA9[i]+""
        },
        {
          "tabId": "81baf331-a358-4661-948f-9e40189e4039",
          "tabLabel": "BOLSA10",
          "value": ""+start_var.BOLSA10[i]+""
        },
        {
          "tabId": "d38c5c80-86c8-491e-8a2e-e7058d8317ab",
          "tabLabel": "BOLSA11",
          "value": ""+start_var.BOLSA11[i]+""
        },
        {
          "tabId": "6d226f0d-1977-4abc-9490-65cc9d1a5af9",
          "tabLabel": "BOLSA12",
          "value": ""+start_var.BOLSA12[i]+""
        },
        {
          "tabId": "326e4b21-92ea-4844-8e11-0f013ac5ded5",
          "tabLabel": "BOLSA13",
          "value": ""+start_var.BOLSA13[i]+""
        },
        {
          "tabId": "0a30f116-965f-4ce5-bad6-c44a03ec38f4",
          "tabLabel": "VALB1",
          "value": ""+start_var.VALB[i]+""
        },
        {
          "tabId": "f255e24f-2cde-4055-bd22-9679b3d82c47",
          "tabLabel": "VALB2",
          "value": ""+start_var.VALB2[i]+""
        },
        {
          "tabId": "8849dd32-f8e8-4b06-aa1a-35b19d14ef88",
          "tabLabel": "VALB3",
          "value": ""+start_var.VALB3[i]+""
        },
        {
          "tabId": "98e5e549-8203-41e3-909f-0769af4ff177",
          "tabLabel": "VALB4",
          "value": ""+start_var.VALB4[i]+""
        },
        {
          "tabId": "8fdedfe2-2e79-4f8e-8ba2-ae93719513e7",
          "tabLabel": "VALB5",
          "value": ""+start_var.VALB5[i]+""
        },
        {
          "tabId": "12fbdb46-f929-422b-a231-afb3c037c0fa",
          "tabLabel": "VALB6",
          "value": ""+start_var.VALB6[i]+""
        },
        {
          "tabId": "9848340c-9acc-4b7d-b009-d0fe827a62da",
          "tabLabel": "VALB7",
          "value": ""+start_var.VALB7[i]+""
        },
        {
          "tabId": "619e16a4-11d6-4dd9-b01f-144cb5e36509",
          "tabLabel": "VALB8",
          "value": ""+start_var.VALB8[i]+""
        },
        {
          "tabId": "d4405e04-cc74-4b77-9ee9-017f5e2d9e72",
          "tabLabel": "VALB9",
          "value": ""+start_var.VALB9[i]+""
        },
        {
          "tabId": "50be3eb7-b9ca-4879-b05b-b4259b2ea437",
          "tabLabel": "VALB10",
          "value": ""+start_var.VALB10[i]+""
        },
        {
          "tabId": "583948b4-167d-4654-a422-81ed85622256",
          "tabLabel": "VALB11",
          "value": ""+start_var.VALB11[i]+""
        },
        {
          "tabId": "dbbc5349-ce09-4101-b4aa-b66f579c2924",
          "tabLabel": "VALB12",
          "value": ""+start_var.VALB12[i]+""
        },
        {
          "tabId": "7fa5cbeb-6add-4f7b-820f-6bf8c249e356",
          "tabLabel": "VALB13",
          "value": ""+start_var.VALB13[i]+""
        },
        {
          "tabId": "b46e00b3-0800-4782-a6cc-8ede4fc3d6a7",
          "tabLabel": "VALDESC1",
          "value": ""+start_var.VALDESC1[i]+""
        },
        {
          "tabId": "5a2d59ff-dae9-4a76-87cf-4186674ed277",
          "tabLabel": "VALDESC2",
          "value": ""+start_var.VALDESC2[i]+""
        },
        {
          "tabId": "7f88f6f0-df42-4b6a-a7d5-99f753431e7c",
          "tabLabel": "VALDESC3",
          "value": ""+start_var.VALDESC3[i]+""
        },
        {
          "tabId": "67770723-8145-4865-a4d0-33773a199c3a",
          "tabLabel": "VALDESC4",
          "value": ""+start_var.VALDESC4[i]+""
        },
        {
          "tabId": "4c6ec1b9-8bcc-4ac5-91ca-ae552d22a042",
          "tabLabel": "VALDESC5",
          "value": ""+start_var.VALDESC5[i]+""
        },
        {
          "tabId": "739b91fd-2767-4648-a24d-3dcabb06b427",
          "tabLabel": "VALDESC6",
          "value": ""+start_var.VALDESC6[i]+""
        },
        {
          "tabId": "840f5a00-b7e7-4291-a245-b0019b6c5ff4",
          "tabLabel": "VALDESC7",
          "value": ""+start_var.VALDESC7[i]+""
        },
        {
          "tabId": "086f7138-5fb0-4e8b-8b20-1ae130a26eb4",
          "tabLabel": "VALDESC8",
          "value": ""+start_var.VALDESC8[i]+""
        },
        {
          "tabId": "a5b50dbb-4a37-470e-96d6-279ab437bd46",
          "tabLabel": "VALDESC9",
          "value": ""+start_var.VALDESC9[i]+""
        },
        {
          "tabId": "4eb030d4-93dd-4a91-afd1-e7cb8adbc331",
          "tabLabel": "VALDESC10",
          "value": ""+start_var.VALDESC10[i]+""
        },
        {
          "tabId": "dab6dc3e-2972-4f3d-82f5-fe4230d00c92",
          "tabLabel": "VALDESC11",
          "value": ""+start_var.VALDESC11[i]+""
        },
        {
          "tabId": "f00c2858-3258-4361-aff4-d55e589c231b",
          "tabLabel": "VALDESC12",
          "value": ""+start_var.VALDESC12[i]+""
        },
        {
          "tabId": "d6a5fd46-982b-431d-a795-4edc50ecf044",
          "tabLabel": "VALDESC13",
          "value": ""+start_var.VALDESC13[i]+""
        },
        {
          "tabId": "b8c33cfa-6c4b-4d19-8eb8-b6b4a4c88358",
          "tabLabel": "VALLQ1",
          "value": ""+start_var.VALLQ1[i]+""
        },
        {
          "tabId": "6dda4c8f-1515-418a-88f5-6055cc14f87f",
          "tabLabel": "VALLQ2",
          "value": ""+start_var.VALLQ2[i]+""
        },
        {
          "tabId": "24ca22a5-0364-48ca-85c9-38c46a6a9bba",
          "tabLabel": "VALLQ3",
          "value": ""+start_var.VALLQ3[i]+""
        },
        {
          "tabId": "e61f6f87-c938-492c-8bbb-b9ad8632db1f",
          "tabLabel": "VALLQ4",
          "value": ""+start_var.VALLQ4[i]+""
        },
        {
          "tabId": "f7333c54-38e8-4b49-95b9-e89456c2073d",
          "tabLabel": "VALLQ5",
          "value": ""+start_var.VALLQ5[i]+""
        },
        {
          "tabId": "ed66c01b-9211-4261-bd82-729b476a675f",
          "tabLabel": "VALLQ6",
          "value": ""+start_var.VALLQ6[i]+""
        },
        {
          "tabId": "c011db27-e6f7-4c38-92c5-dcb87014e818",
          "tabLabel": "VALLQ7",
          "value": ""+start_var.VALLQ7[i]+""
        },
        {
          "tabId": "4ab21d54-27b5-4cdb-8e2b-106b2dce183d",
          "tabLabel": "VALLQ8",
          "value": ""+start_var.VALLQ8[i]+""
        },
        {
          "tabId": "244ea789-209f-49f7-bdcd-31a06fcae64f",
          "tabLabel": "VALLQ9",
          "value": ""+start_var.VALLQ9[i]+""
        },
        {
          "tabId": "d56a1182-346a-4440-99d5-cbfca85016d9",
          "tabLabel": "VALLQ10",
          "value": ""+start_var.VALLQ10[i]+""
        },
        {
          "tabId": "d9f66473-9d95-40e8-9a1e-8ff85e02766d",
          "tabLabel": "VALLQ11",
          "value": ""+start_var.VALLQ11[i]+""
        },
        {
          "tabId": "93c67305-6bd7-4386-82e0-c06943aa9e97",
          "tabLabel": "VALLQ12",
          "value": ""+start_var.VALLQ12[i]+""
        },
        {
          "tabId": "b4b79d64-f645-492b-82fc-1cb28c08a1f7",
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
