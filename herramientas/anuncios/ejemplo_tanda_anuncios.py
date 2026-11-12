import sys; sys.path.insert(0,'.')
from armar_anuncio import build
P='Pack Estrella desde $240.000 por hora'; T='+ traslado'; W='Escríbenos por WhatsApp'
mu='musica1.mp3'
which=sys.argv[1:]
J={}
J['A']=('voA.mp3',20.8,[
 (0,2.99,[('m24',3.2),('m12',0.2)],'Nunca organices un evento sin pensar en esto',None),
 (2.99,5.95,[('m34',0.9),('m36',6.0)],'Nadie habla de la decoración',None),
 (5.95,7.9,[('m39',0.2),('m13',2.6)],'Todos recuerdan lo que vivieron',None),
 (7.9,11.41,[('m27',2.3),('m26',5.0),('m10',2.0)],'3 experiencias para hacerlo inolvidable',None),
 (11.41,12.5,[('m11',0.4)],'Fotocabina',None),(12.5,13.7,[('m25',5.2)],'Plataforma 360',None),(13.7,15.07,[('m35',1.2)],'Selfie Mirror',None),
 (15.07,18.76,[('m16',21.3),('m19',1.0),('m36',15.4)],P,T),
 (18.76,20.8,[('m40',2.6)],W,None)],'v2/A-decoracion.mp4')
J['B']=('voB.mp3',23.0,[
 (0,3.13,[('m24',3.2),('m12',0.2),('m21',1.0)],'Si estás organizando un evento, esto es para ti',None),
 (3.13,6.35,[('m39',0.2),('m13',2.6),('m36',15.4)],'Lo van a recordar por lo que vivan',None),
 (6.35,9.18,[('m27',2.3),('m10',2.0),('m35',1.2)],'3 experiencias distintas',None),
 (9.18,10.25,[('m11',0.4)],'Fotocabina',None),(10.25,11.3,[('m26',5.0)],'Plataforma 360',None),(11.3,12.86,[('m36',8.2)],'Selfie Mirror',None),
 (12.86,17.06,[('m19',1.0),('m25',5.2),('m21',1.6),('m40',0.6)],'Cada una, un recuerdo diferente',None),
 (17.06,20.89,[('m16',21.3),('m12',2.9),('m13',5.0)],P,T),
 (20.89,23.0,[('m40',2.6)],W,None)],'v2/B-organizando.mp4')
J['C']=('voC.mp3',17.9,[
 (0,3.29,[('m24',3.2),('m40',0.6),('m12',0.2)],'Así logras un evento inolvidable',None),
 (3.29,5.2,[('m27',2.3),('m26',5.0)],'Tus invitados no solo bailan…',None),
 (5.2,6.6,[('m11',0.4),('m19',1.0)],'Posan en la Fotocabina',None),
 (6.6,8.0,[('m25',5.2),('m40',2.0)],'Giran en la 360',None),
 (8.0,9.96,[('m35',1.2),('m36',15.4)],'Fotos frente al espejo',None),
 (9.96,13.16,[('m13',2.6),('m39',0.2),('m21',1.0)],'Una fiesta de otro nivel','Pack Estrella'),
 (13.16,15.85,[('m10',2.0),('m16',21.3)],'Desde $240.000 por hora',T),
 (15.85,17.9,[('m40',2.6)],W,None)],'v2/C-inolvidable.mp4')
J['D']=('voD.mp3',20.4,[
 (0,2.81,[('m24',3.2),('m12',0.2)],'Esto es lo que andan diciendo de nosotros…',None),
 (2.81,6.16,[('m40',0.6),('m26',5.0)],('Juan Carlos F.','“La experiencia es única y queda un lindo recuerdo.”'),None),
 (6.16,8.61,[('m39',0.2),('m13',2.6)],('Estefanía G.','“Todo muy lindo, muy ordenado. Los invitados quedaron muy contentos.”'),None),
 (8.61,11.22,[('m21',1.0),('m36',15.4)],('Karen M.','“Muy amables en cuanto al trato con los invitados.”'),None),
 (11.22,12.3,[('m11',0.4)],'Fotocabina',None),(12.3,13.4,[('m27',2.3)],'Plataforma 360',None),(13.4,14.64,[('m35',1.2)],'Selfie Mirror',None),
 (14.64,18.35,[('m16',21.3),('m19',1.0),('m36',8.2)],P,T),
 (18.35,20.4,[('m40',2.6)],W,None)],'v2/D-resenas.mp4')
J['E1']=('vo1cl.mp3',15.9,[
 (0,2.26,[('m24',3.2),('m27',2.3)],'Cero invitados aburridos',None),
 (2.26,4.75,[('m12',0.2),('m11',0.4),('m19',1.0)],'Fotocabina','fotos impresas para llevarse'),
 (4.75,7.9,[('m26',5.0),('m40',0.6),('m25',5.2)],'Plataforma 360','videos para compartir'),
 (7.9,10.26,[('m21',1.0),('m35',1.2),('m36',15.4)],'Selfie Mirror','todo el evento'),
 (10.26,13.92,[('m13',2.6),('m10',2.0),('m39',0.2),('m16',21.3)],P,T),
 (13.92,15.9,[('m40',2.6)],W,None)],'v2/E1-aburrimiento.mp4')
J['E4']=('vo4cl.mp3',14.6,[
 (0,2.75,[('m24',3.2),('m12',0.2)],'Así lo viven tus invitados',None),
 (2.75,4.91,[('m11',0.4),('m19',1.0),('m13',2.6)],'Posan y se llevan su foto','Fotocabina'),
 (4.91,7.56,[('m27',2.3),('m26',5.0),('m40',0.6)],'Bailan y se llevan su video','Plataforma 360'),
 (7.56,9.74,[('m21',1.0),('m35',1.2),('m36',15.4)],'Selfies frente al espejo','Selfie Mirror'),
 (9.74,12.54,[('m10',2.0),('m39',0.2),('m16',21.3)],P,T),
 (12.54,14.6,[('m40',2.6)],W,None)],'v2/E4-invitados.mp4')
for k in (which or J):
    vo,tot,segs,out=J[k]; build(k,vo,tot,segs,mu,out)
