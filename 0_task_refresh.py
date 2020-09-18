from tendo import singleton

## PREVINE O SCRIPT DE SER ABERTO ENQUANTO ESTIVER EM EXECUÇÃO
me = singleton.SingleInstance()

import refresh_token

refresh_token.refresh()
refresh_token.set_token(refresh_token.token)