import db_docu
import start_var
import template
import envelope
i = 0

## INICIA OS ARRAYS COM AS INFOS DO BANCO PARA O TEMPLATE
start_var.start_variables_template()

length = len(db_docu.rows)

while i < length:
    ## INSERE AS INFOS DO BD NO TEMPLATE
    template.update_template(i)

    ## REALIZA O UPDATE NO TEMPLATE
    template.put()

    ## CRIA AS VARIÁVEIS PARA COLOCAR NO ENVELOPE
    envelope.create_var_envelope(i)

    ## INSERE AS INFOS DO BD NO ENVELOPE
    envelope.create_envelope(i,envelope.customKwargs,envelope.kwargs)

    ## REALIZA O ENVIO DO ENVELOPE
    envelope.post(envelope.url,envelope.dataEnv,envelope.hdr)

    ## GRAVA O ENVELOPE NO BANCO
    envelope.gravar(i)

    i+=1