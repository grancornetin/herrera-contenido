"""Monta un anuncio vertical 1080x1920: clips reales (ids m10, m24...) con cortes sincronizados a una voz,
texto en la mitad inferior (y termina en 1380), tarjetas de reseña, voz + música (a 0,20 de volumen).
Requiere ffmpeg y Pillow. Los clips se leen de medios/servicios/ y las fuentes de medios/marca/fuentes/.
Estilo A (13-nov, aprobado): build(..., estilo='A'); el subtítulo es un dict {'sup':..,'sub':..,'size':..}.
Uso: ver ejemplo_tanda_anuncios.py y g12_montaje.py (build(nombre, voz.mp3, duracion_total, segmentos, musica.mp3, salida.mp4)).
Cada segmento = (t_inicio, t_fin, [(id_clip, segundo_de_inicio), ...], texto_principal, subtitulo).
Para sincronizar: medir las pausas de la voz con
  ffmpeg -i voz.mp3 -af silencedetect=n=-35dB:d=0.18 -f null -
y cortar los segmentos en esas pausas. Faltan por hacer: tarjetas de reseña con 5 estrellas y en motion graphics.
"""
import subprocess, json, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
M='/home/user/herrera-contenido/medios/servicios/'
F='/home/user/herrera-contenido/medios/marca/fuentes/'
C={'m10':M+'fotocabina/m10-extracto-sesion-fotocabina.mp4','m11':M+'fotocabina/m11-fotocabina-extracto-de-sesion-novios.mp4',
'm12':M+'fotocabina/m12-fotocabina-sesion-en-camara-rapida.mp4','m13':M+'fotocabina/m13-fotocabina-sesion-grupal-v1.mp4',
'm16':M+'fotocabina/m16-fotocabina-vista-interna.mp4','m19':M+'fotocabina/m19-grupo-fotocabina.mp4','m39':M+'fotocabina/m39-sesion-grupal-fotocabina-extraxto.mp4',
'm21':M+'selfie-mirror/m21-novios-frente-al-selfie-mirror.mp4','m35':M+'selfie-mirror/m35-selfie-mirror-registro-propio.mp4','m36':M+'selfie-mirror/m36-selfie-mirror-uso.mp4',
'm24':M+'plataforma-360/m24-plataforma-360-pov-desde-afuera.mp4','m25':M+'plataforma-360/m25-plataforma-360-pov-externo-con-staff.mp4',
'm26':M+'plataforma-360/m26-plataforma-360-pov-final-2.mp4','m27':M+'plataforma-360/m27-plataforma-360-pov-final.mp4','m40':M+'plataforma-360/m40-plataforma-360-invitada-con-ramo.mp4','m34':M+'selfie-mirror/m34-selfie-mirror-montaje-2.mp4','m33':M+'selfie-mirror/m33-selfie-mirror-montaje-1.mp4','m37':M+'fotocabina/m37-sesion-fotoacbina-novios.mp4'}
def card(path, main, sub=None):
    im=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im)
    f=ImageFont.truetype(F+'montserrat-600.ttf',76); fs=ImageFont.truetype(F+'montserrat-600.ttf',46)
    words=main.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=f)>840 and cur: lines.append(cur); cur=w
        else: cur=t
    lines.append(cur)
    h=len(lines)*92+(58 if sub else 0)
    y=1380-h; items=[]
    for l in lines: items.append((l,f,y)); y+=92
    if sub: items.append((sub,fs,y+6))
    sh=Image.new('RGBA',im.size,(0,0,0,0)); ds=ImageDraw.Draw(sh)
    for l,ff,yy in items:
        x=(1080-d.textlength(l,font=ff))/2; ds.text((x+3,yy+4),l,font=ff,fill=(0,0,0,200))
    sh=sh.filter(ImageFilter.GaussianBlur(7)); im=Image.alpha_composite(sh,im); d=ImageDraw.Draw(im)
    for l,ff,yy in items:
        x=(1080-d.textlength(l,font=ff))/2; d.text((x,yy),l,font=ff,fill=(255,255,255,255))
    im.save(path)
CH=(207,175,116)  # champagne de marca
def card_a(path, main, sub=None, sup=None, size=112):
    """Estilo A (aprobado 13-nov): titular Sora 800 grande, palabra clave en champagne.
    main: '|' corta línea, *palabra* va en champagne. sup: línea chica arriba. sub: línea chica abajo."""
    im=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im)
    big=ImageFont.truetype(F+'sora-800.ttf',size); small=ImageFont.truetype(F+'sora-600.ttf',56)
    rows=[]
    if sup: rows.append(([(sup,small,(255,255,255))],70))
    for ln in main.split('|'):
        parts=[];
        for i,ch in enumerate(ln.split('*')):
            if ch: parts.append((ch,big,CH if i%2 else (255,255,255)))
        rows.append((parts,size+18))
    if sub: rows.append(([(sub,small,(255,255,255))],70))
    y=1380-sum(h for _,h in rows); items=[]
    for parts,h in rows:
        w=sum(d.textlength(t,font=f) for t,f,c in parts); x=(1080-w)/2
        for t,f,c in parts: items.append((x,y,t,f,c)); x+=d.textlength(t,font=f)
        y+=h
    sh=Image.new('RGBA',im.size,(0,0,0,0)); ds=ImageDraw.Draw(sh)
    for x,y,t,f,c in items: ds.text((x+4,y+6),t,font=f,fill=(0,0,0,230))
    sh=sh.filter(ImageFilter.GaussianBlur(9)); im=Image.alpha_composite(sh,im); d=ImageDraw.Draw(im)
    for x,y,t,f,c in items: d.text((x,y),t,font=f,fill=c,stroke_width=2,stroke_fill=(0,0,0,90))
    im.save(path)
def build(name, vo, total, segs, music, out, estilo=None):
    # segs: (t0,t1,[(clip,start)],main,sub)
    tmp=out+'_tmp'; os.makedirs(tmp,exist_ok=True)
    inp=[];fl=[];k=0;vl=[]
    for (t0,t1,clips,main,sub) in segs:
        dd=(t1-t0)/len(clips)
        for (c,s) in clips:
            inp+=['-ss',str(s),'-t',f'{dd:.3f}','-i',C[c]]
            fl.append(f'[{k}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,trim=duration={dd:.3f},setpts=PTS-STARTPTS[v{k}]'); vl.append(f'[v{k}]'); k+=1
    fl.append(''.join(vl)+f'concat=n={k}:v=1:a=0[base]')
    last='base'
    for i,(t0,t1,clips,main,sub) in enumerate(segs):
        p=f'{tmp}/c{i}.png'
        if isinstance(main,tuple): review_card(p,*main)
        elif estilo=='A': card_a(p,main,**(sub or {}))
        else: card(p,main,sub)
        inp+=['-i',p]
        fl.append(f'[{last}][{k}:v]overlay=0:0:enable=\'between(t,{t0},{t1-0.001})\'[o{i}]'); last=f'o{i}'; k+=1
    inp+=['-i',vo,'-i',music]; a1=k; a2=k+1
    fl.append(f'[{a1}:a]loudnorm=I=-16:TP=-1.5,apad[voz]')
    fl.append(f'[{a2}:a]volume=0.20,afade=t=out:st={total-0.8}:d=0.8[mus]')
    fl.append(f'[voz][mus]amix=inputs=2:duration=longest:normalize=0,atrim=duration={total}[aud]')
    subprocess.run(['ffmpeg','-loglevel','error','-y',*inp,'-filter_complex',';'.join(fl),'-map',f'[{last}]','-map','[aud]','-t',str(total),
      '-c:v','libx264','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',out],check=True)
    print(name,'ok')

def review_card(path, name, quote):
    W=900
    im=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im)
    fn=ImageFont.truetype(F+'montserrat-600.ttf',44); fq=ImageFont.truetype(F+'montserrat-400.ttf',46); fst=ImageFont.truetype(F+'montserrat-600.ttf',40)
    words=quote.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=fq)>W-110 and cur: lines.append(cur); cur=w
        else: cur=t
    lines.append(cur)
    h=60+56+50+len(lines)*60+50
    x0=(1080-W)//2; y0=1390-h
    sh=Image.new('RGBA',im.size,(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle((x0,y0+10,x0+W,y0+h+10),radius=40,fill=(0,0,0,120))
    sh=sh.filter(ImageFilter.GaussianBlur(14)); im=Image.alpha_composite(im,sh); d=ImageDraw.Draw(im)
    d.rounded_rectangle((x0,y0,x0+W,y0+h),radius=40,fill=(255,255,255,245))
    cx,cy=x0+85,y0+88; d.ellipse((cx-38,cy-38,cx+38,cy+38),fill=(232,140,165,255))
    d.text((cx,cy),name[0],font=fn,fill='white',anchor='mm')
    d.text((x0+145,y0+52),name,font=fn,fill=(20,20,20,255))
    d.text((x0+145,y0+104),'Reseña de cliente',font=fst,fill=(120,120,120,255))
    y=y0+170
    for l in lines: d.text((x0+55,y),l,font=fq,fill=(30,30,30,255)); y+=60
    im.save(path)
