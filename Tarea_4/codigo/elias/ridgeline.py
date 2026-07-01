import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.interpolate import PchipInterpolator

NAVY="#14213D"; BLUE="#2563A8"; TEAL="#2A9D8F"; AMBER="#E9A23B"; RED="#E63946"
GREY="#6B7280"; LGREY="#E5E7EB"; WHITE="#FFFFFF"
mpl.rcParams.update({"font.family":"DejaVu Sans","text.color":NAVY,"axes.labelcolor":NAVY})

df=pd.read_csv("../../datos/Habitos_de_uso_de_redes_sociales.csv")
df.columns=["ts","horas","redes","contenido","dispositivo"]
df["horas"]=df["horas"].str.strip()

band_order=["Entre 0 y 1 Horas","Entre 1 y 3 Horas","Entre 3 y 5 Horas","Más de 5 Horas"]
band_mid={"Entre 0 y 1 Horas":0.5,"Entre 1 y 3 Horas":2.0,"Entre 3 y 5 Horas":4.0,"Más de 5 Horas":6.0}
band_lbl=["0–1","1–3","3–5","+5"]
df["mid"]=df["horas"].map(band_mid)

plats=["Instagram","YouTube","TikTok","Otra","X (Anteriormente Twitter)"]
pname={"Instagram":"Instagram","YouTube":"YouTube","TikTok":"TikTok","Otra":"Otra","X (Anteriormente Twitter)":"X (Twitter)"}
pcol={"Instagram":RED,"YouTube":AMBER,"TikTok":NAVY,"Otra":TEAL,"X (Anteriormente Twitter)":BLUE}
def uses(row,p): return p in [x.strip() for x in str(row).split(";")]

dist={}
for p in plats:
    sub=df[df["redes"].apply(lambda r:uses(r,p))]
    counts=[(sub["horas"]==b).sum() for b in band_order]; n=len(sub)
    dist[p]=dict(counts=counts,n=n,prop=np.array(counts)/n if n else np.zeros(4),
                 mean=(sub["mid"].mean() if n else np.nan))

order=sorted(plats,key=lambda p:dist[p]["mean"])
xs_pts=np.array([0.5,2.0,4.0,6.0]); xg=np.linspace(0.0,6.6,300)
fig,ax=plt.subplots(figsize=(10,7))
overlap=1.6; scale=3.2
for i,p in enumerate(order):
    base=i*overlap; y_pts=dist[p]["prop"]
    xp=np.concatenate(([0.0],xs_pts,[6.6])); yp=np.concatenate(([0.0],y_pts,[0.0]))
    yg=np.clip(PchipInterpolator(xp,yp)(xg),0,None)*scale+base
    ax.fill_between(xg,base,yg,color=pcol[p],alpha=0.80,zorder=len(order)-i,linewidth=0)
    ax.plot(xg,yg,color=WHITE,lw=1.4,zorder=len(order)-i)
    ax.scatter(xs_pts,y_pts*scale+base,color=WHITE,edgecolor=pcol[p],s=22,zorder=len(order)+1)
    ax.text(-0.15,base+0.12,pname[p],ha="right",va="bottom",fontsize=12,fontweight="bold",color=pcol[p])
    ax.text(-0.15,base-0.12,f"n={dist[p]['n']}",ha="right",va="top",fontsize=8.5,color=GREY)
ax.set_xticks([0.5,2.0,4.0,6.0]); ax.set_xticklabels(band_lbl,fontsize=12)
ax.set_xlabel("Horas diarias de uso declaradas",fontsize=12,labelpad=8)
ax.set_xlim(-1.6,6.9); ax.margins(y=0.08); ax.set_yticks([])
for s in ["left","right","top"]: ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GREY)
fig.text(0.02,0.975,"¿Cuántas horas usan al día según la plataforma?",fontsize=17,fontweight="bold",color=NAVY,ha="left",va="top")
fig.text(0.02,0.935,"Distribución de horas diarias entre quienes usan cada plataforma",fontsize=11,color=GREY,ha="left",va="top")
fig.text(0.98,0.015,"Fuente: encuesta propia del grupo (Google Forms, Tarea 2), n=25.  "
         "Cada cresta usa solo a quienes declararon usar esa plataforma (multiselección).",ha="right",va="bottom",fontsize=8.5,color=GREY)
plt.subplots_adjust(top=0.88,bottom=0.13,left=0.02,right=0.98)
plt.savefig("viz_ridgeline.png",dpi=180,bbox_inches="tight",facecolor=WHITE)
print("OK ridgeline")
