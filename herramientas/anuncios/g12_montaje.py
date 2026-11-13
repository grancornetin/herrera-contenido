import sys; sys.path.insert(0,'/home/user/herrera-contenido/herramientas/anuncios')
from armar_anuncio import build
segs=[
 (0,1.36,[('m24',3.2)],'Organizaste todo…',None),
 (1.36,3.97,[('m27',2.3),('m12',0.2)],'¿Quién entretiene a tus invitados?',None),
 (3.97,5.71,[('m39',7.5),('m13',2.6)],'De eso nos encargamos nosotros',None),
 (5.71,8.58,[('m11',0.4),('m19',1.0)],'Fotocabina','fotos impresas al instante'),
 (8.58,9.9,[('m26',5.0)],'Plataforma 360',None),
 (9.9,11.6,[('m21',1.0),('m36',15.4)],'Selfie Mirror',None),
 (11.6,14.62,[('m16',21.3),('m37',1.0)],'Pack Estrella desde $240.000','+ traslado'),
 (14.62,15.96,[('m40',2.6)],'Escríbenos por WhatsApp',None)]
# voz: piezas/semana-02/aprobadas/g12-voz-final.mp3 · música: disco-funk 1 desde 6,73 s (17 s)
build('G12','voz.mp3',15.96,segs,'mus.mp3','G12-organizadora.mp4')
