# Pone música a un reel ya montado, estirando cada toma a N golpes de la canción.
# Uso: python3 sincronizar_musica.py VIDEO SALIDA MUSICA "cortes,en,segundos" "golpes,por,toma"
# P = duración de un golpe (0.48 s a 125 BPM); off = dónde empieza el primer golpe en la canción.
import subprocess,sys
src,out,music,cuts,beats=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]
cuts=[float(x) for x in cuts.split(',')]   # includes 0 and end
beats=[int(x) for x in beats.split(',')]
P=0.48; off=0.012
parts=[];cum=0;prev=0
for k in range(len(beats)):
    a,b=cuts[k],cuts[k+1]
    cum+=beats[k]*P
    endf=round(cum*30); dur=(endf-prev)/30; prev=endf
    f=dur/(b-a)
    parts.append(f"[0:v]trim=start={a}:end={b},setpts=(PTS-STARTPTS)*{f:.5f},fps=30,trim=end_frame={int(round(dur*30))},setpts=PTS-STARTPTS[v{k}]")
total=prev/30
fc=";".join(parts)+";"+"".join(f"[v{k}]" for k in range(len(beats)))+f"concat=n={len(beats)}:v=1:a=0,format=yuv420p[v];[1:a]atrim=start={off}:duration={total},asetpts=PTS-STARTPTS,afade=t=out:st={total-0.7}:d=0.7,aresample=48000[a]"
cmd=["ffmpeg","-nostdin","-y","-i",src,"-i",music,"-filter_complex",fc,"-map","[v]","-map","[a]","-c:v","libx264","-crf","18","-preset","slow","-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart",out]
subprocess.run(cmd,check=True,capture_output=True)
print(out,total)
