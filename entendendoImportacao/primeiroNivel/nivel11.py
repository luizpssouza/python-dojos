from .nivel111 import metodoNivel111

#Se tentar realizar este import não conseguirá pois averá uma referencia circular
#pois o modulo .nivel1 ainda está sendo criado, ocorrendo o erro:
# ImportError: cannot import name 'metodoNivel1'
# from .nivel1 import metodoNivel1 

print('---- primeiroNivel.Nivel11')

#metodoNivel1()

def metodoNivel11():
    print('---- primeiroNivel.Nivel1.metodoNivel11()')
