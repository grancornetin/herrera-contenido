# Anuncios G7, G10 y G11 · estilo A con golpe en titular y precio (como el G12 variante B), 13-nov.
# Voces (ElevenLabs, flow Ewr863D1kOokTeEczqoF): G10 3JGDwvOurYjZX8dE1Jp2 · G11 P6omBlLyaqm6oBwGa68G · G7 1BufwcpCjTABWchHr5Iy
# G7 a 16 s (PROPUESTA, sin aprobar): se quita «La tercera es la más sencilla, y la más top» (2,86–6,0 s),
# pausas a 0,14 s y ×1,10 (atempo) → vo-g7-16s.mp3. Música: mus.mp3 (disco-funk 1 desde 6,73 s).
import sys; sys.path.insert(0,'/home/user/herrera-contenido/herramientas/anuncios')
from armar_anuncio import build
P={'sup':'Pack Estrella desde','sub':'+ traslado','size':150,'pop':True}
W='Escríbenos por|*WhatsApp*'
G={}
G['g10']=('vo-g10.mp3',15.80,[
 (0,1.64,[('m40',0.6)],'¿Evento en el *Maule*?',{'size':90,'pop':True}),
 (1.64,2.86,[('m12',0.2)],'*Pack Estrella*',None),
 (2.86,4.30,[('m11',0.4),('m19',1.0)],'*Fotocabina*',{'sub':'fotos impresas al instante'}),
 (4.30,6.10,[('m26',5.0),('m27',2.3)],'*Plataforma 360*',{'sub':'videos para compartir'}),
 (6.10,7.53,[('m36',8.2),('m35',1.2)],'*Selfie Mirror*',{'sub':'todo el evento'}),
 (7.53,10.89,[('m39',7.5),('m13',2.6),('m21',1.0)],'3 experiencias,|un recuerdo|*inolvidable*',{'size':96}),
 (10.89,14.54,[('m37',1.0),('m13',5.0)],'*$240.000*',P),
 (14.54,15.80,[('m40',2.6)],W,None)],'G10-maule.mp4')
G['g11']=('vo-g11.mp3',11.65,[
 (0,1.96,[('m24',3.2),('m12',0.2)],'¿*Fotocabina* o 360?',{'size':92,'pop':True}),
 (1.96,3.28,[('m39',7.5)],'No tienes que|*elegir*',None),
 (3.28,4.92,[('m11',0.4),('m26',5.0)],'*Las dos*, en el|Pack Estrella',{'size':100}),
 (4.92,7.74,[('m36',8.2),('m35',1.2)],'+ *Selfie Mirror*',{'sub':'todo el evento'}),
 (7.74,10.35,[('m37',1.0),('m13',5.0)],'*$240.000*',P),
 (10.35,11.65,[('m40',2.6)],W,None)],'G11-indecision.mp4')
G['g7']=('vo-g7-16s.mp3',15.94,[
 (0,2.60,[('m40',0.6),('m27',2.3)],'*3 infaltables*|para tu evento',{'size':104,'pop':True}),
 (2.60,5.33,[('m11',0.4),('m19',1.0)],'1 · *Fotocabina*',{'sub':'risas impresas'}),
 (5.33,8.53,[('m26',5.0),('m24',3.2)],'2 · *Plataforma 360*',{'sub':'siéntete protagonista'}),
 (8.53,11.62,[('m36',8.2),('m35',1.2)],'3 · *Selfie Mirror*',{'sub':'la más top'}),
 (11.62,14.82,[('m37',1.0),('m13',5.0)],'*$240.000*',P),
 (14.82,15.94,[('m40',2.6)],W,None)],'G7-infaltables.mp4')
for k in (sys.argv[1:] or G):
    vo,tot,segs,out=G[k]; build(k,vo,tot,segs,'mus.mp3',out,estilo='A')
