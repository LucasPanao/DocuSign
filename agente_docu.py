import db_docu
import start_var
import template
import envelope

## INICIA OS ARRAYS COM AS INFOS DO BANCO PARA O TEMPLATE
start_var.start_variables_template()

## INSERE AS INFOS DO BD NO TEMPLATE
template.update_template()

## REALIZA O UPDATE NO TEMPLATE
template.put()

## INICIA OS ARRAYS COM AS INFOS DO BANCO PARA O ENVELOPE
start_var.start_variables_envelope()

## INSERE AS INFOS DO BD NO ENVELOPE
envelope.create_envelope(envelope.customKwargs,envelope.kwargs)

## REALIZA O ENVIO DO ENVELOPE
envelope.post(envelope.url,envelope.dataEnv,envelope.hdr)

## GRAVA O ENVELOPE NO BANCO
envelope.gravar()