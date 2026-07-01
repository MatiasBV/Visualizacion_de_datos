import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

NAVY="#14213D"; BLUE="#2563A8"; AMBER="#E9A23B"; RED="#E63946"
GREY="#6B7280"; LGREY="#E5E7EB"; WHITE="#FFFFFF"
mpl.rcParams.update({"font.family":"DejaVu Sans","text.color":NAVY,"axes.labelcolor":NAVY})

plats=["Instagram","TikTok","YouTube","Facebook"]
axes_lbl=["Usuarios\n(MAU, mill.)","Alcance\npublic. (mill.)","Uso mensual\n16+ (%)","Tiempo diario\n(min)"]
data={"Instagram":[3000,1990,55.1,34],"TikTok":[1990,2210,36.0,69],
      "YouTube":[2580,2650,55.4,59],"Facebook":[3070,2390,56.9,37]}
pcolors={"Instagram":RED,"TikTok":NAVY,"YouTube":AMBER,"Facebook":BLUE}
df=pd.DataFrame(data,index=axes_lbl).T
norm=df/df.max(axis=0)*100

N=len(axes_lbl); ang=np.linspace(0,2*np.pi,N,endpoint=False).tolist(); ang+=ang[:1]
fig=plt.figure(figsize=(13,7.5))
axr=fig.add_subplot(1,2,1,polar=True); axr.set_theta_offset(np.pi/2); axr.set_theta_direction(-1)
axr.set_xticks(ang[:-1]); axr.set_xticklabels(axes_lbl,fontsize=10.5)
axr.set_yticks([25,50,75,100]); axr.set_yticklabels(["25","50","75","100"],fontsize=8,color=GREY)
axr.set_ylim(0,108); axr.grid(color=LGREY,lw=1); axr.spines["polar"].set_color(LGREY)
for p in plats:
    vals=norm.loc[p].tolist(); vals+=vals[:1]
    axr.plot(ang,vals,color=pcolors[p],lw=2.2,label=p); axr.fill(ang,vals,color=pcolors[p],alpha=0.10)
axr.set_title("Perfil comparativo de plataformas\n(ejes normalizados, 100 = maximo)",fontsize=14,fontweight="bold",pad=22,color=NAVY)
axr.legend(loc="upper right",bbox_to_anchor=(1.28,1.12),frameon=False,fontsize=10)
axt=fig.add_subplot(1,2,2); axt.axis("off")
tbl=axt.table(cellText=[[f"{df.loc[p,c]:.0f}" if c!=axes_lbl[2] else f"{df.loc[p,c]:.1f}" for c in axes_lbl] for p in plats],
    rowLabels=plats,colLabels=["MAU\n(mill.)","Alcance\n(mill.)","Uso 16+\n(%)","Tiempo\n(min/dia)"],
    cellLoc="center",rowLoc="center",loc="center",bbox=[0.05,0.30,0.92,0.45])
tbl.auto_set_font_size(False); tbl.set_fontsize(10); tbl.scale(1,1.6)
for (r,c),cell in tbl.get_celld().items():
    cell.set_edgecolor(LGREY)
    if r==0: cell.set_facecolor(NAVY); cell.set_text_props(color=WHITE,fontweight="bold")
    elif c==-1: cell.set_text_props(color=pcolors[plats[r-1]],fontweight="bold")
axt.text(0.5,0.85,"Valores reales",ha="center",fontsize=13,fontweight="bold",color=NAVY)
axt.text(0.5,0.20,"Fuentes:  MAU y alcance publicitario — Statista / We Are Social / DataReportal\n"
    "y herramientas publicitarias de cada plataforma (oct. 2025).\n"
    "Uso mensual 16+ — GWI vía DataReportal (oct. 2025).\n"
    "Tiempo diario por app — DataReportal / analitica de apps (2025-2026).",ha="center",va="top",fontsize=8.5,color=GREY)
plt.tight_layout()
plt.savefig("viz_radar.png",dpi=180,bbox_inches="tight",facecolor=WHITE)
print("OK radar")
