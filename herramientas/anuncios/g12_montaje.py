# Anuncio G12 «La organizadora» · estilo de texto A (aprobado 13-nov).
# voz: piezas/semana-02/aprobadas/g12-voz-final.mp3 · música: disco-funk 1 de ElevenLabs desde 6,73 s (17 s) → mus.mp3
import sys; sys.path.insert(0,'/home/user/herrera-contenido/herramientas/anuncios')
from armar_anuncio import build
segs=[
 (0,3.97,[('m24',3.2),('m27',2.3),('m12',0.2)],'¿Quién *entretiene*|a tus invitados?',{'size':100}),
 (3.97,5.71,[('m39',7.5),('m13',2.6)],'Déjalo en|*nuestras manos*',None),
 (5.71,8.58,[('m11',0.4),('m19',1.0)],'*Fotocabina*',{'sub':'fotos impresas al instante'}),
 (8.58,9.9,[('m26',5.0)],'*Plataforma 360*',{'sub':'videos para compartir'}),
 (9.9,11.6,[('m36',8.2),('m35',1.2)],'*Selfie Mirror*',{'sub':'todo el evento'}),
 (11.6,14.62,[('m37',1.0),('m13',5.0)],'*$240.000*',{'sup':'Pack Estrella desde','sub':'+ traslado','size':150}),
 (14.62,15.96,[('m40',2.6)],'Escríbenos por|*WhatsApp*',None)]
import copy
if __name__=='__main__':
    which=sys.argv[1:] or ['base']
    if 'base' in which: build('G12','voz.mp3',15.96,segs,'mus.mp3','G12-organizadora.mp4',estilo='A')
    # Variante gancho 1: abre con la invitada del ramo en la 360 (humo y luces)
    g1=copy.deepcopy(segs); g1[0]=(0,3.97,[('m40',0.6),('m27',2.3),('m12',0.2)],'¿Quién *entretiene*|a tus invitados?',{'size':100})
    if 'g1' in which: build('G12g1','voz.mp3',15.96,g1,'mus.mp3','G12-gancho1.mp4',estilo='A')
    # Variante gancho 2: igual a g1 + entrada con golpe del titular y del precio
    g2=copy.deepcopy(g1); g2[0]=g2[0][:4]+({'size':100,'pop':True},); g2[5]=g2[5][:4]+(dict(g2[5][4],pop=True),)
    if 'g2' in which: build('G12g2','voz.mp3',15.96,g2,'mus.mp3','G12-gancho2.mp4',estilo='A')
