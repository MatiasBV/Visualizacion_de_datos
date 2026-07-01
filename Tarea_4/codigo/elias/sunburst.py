import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import matplotlib as mpl

NAVY="#14213D"; BLUE="#2563A8"; TEAL="#2A9D8F"; AMBER="#E9A23B"; RED="#E63946"
GREY="#6B7280"; WHITE="#FFFFFF"
mpl.rcParams.update({"font.family":"DejaVu Sans","text.color":NAVY,"axes.labelcolor":NAVY})

cats = {
    "Conexion social":  [("Amigos y familia",49.0),("Compartir opiniones",22.5),("Nuevos contactos",22.8)],
    "Entretenimiento":  [("Llenar tiempo libre",39.3),("Seguir deportes",23.5),("Ver streams en vivo",23.4)],
    "Informacion":      [("Leer noticias",30.1),("Investigacion laboral",21.5),("Seguir influencers",20.4)],
    "Compras y marcas": [("Buscar productos",27.3),("Inspiracion de compra",27.1),("Contenido de marcas",22.7)],
}
cat_colors = {"Conexion social":BLUE,"Entretenimiento":RED,"Informacion":TEAL,"Compras y marcas":AMBER}

def shade(hexc,f):
    hexc=hexc.lstrip("#"); r,g,b=(int(hexc[i:i+2],16) for i in (0,2,4))
    r,g,b=(int(c+(255-c)*f) for c in (r,g,b))
    return f"#{r:02x}{g:02x}{b:02x}"

cat_totals={c:sum(v for _,v in s) for c,s in cats.items()}
grand=sum(cat_totals.values())

fig,ax=plt.subplots(figsize=(9,9),subplot_kw=dict(aspect="equal"))
start=90.0; r_in,r_mid,r_out=0.55,0.78,1.10
for c,subs in cats.items():
    ang=cat_totals[c]/grand*360; a0,a1=start-ang,start
    ax.add_patch(Wedge((0,0),r_mid,a0,a1,width=r_mid-r_in,facecolor=cat_colors[c],edgecolor=WHITE,lw=2))
    mid=np.radians((a0+a1)/2)
    ax.text(((r_in+r_mid)/2)*np.cos(mid),((r_in+r_mid)/2)*np.sin(mid),c.replace(" ","\n"),
            ha="center",va="center",color=WHITE,fontsize=11,fontweight="bold")
    s2=a1
    for j,(sub,val) in enumerate(subs):
        sa=val/cat_totals[c]*ang; b0,b1=s2-sa,s2
        ax.add_patch(Wedge((0,0),r_out,b0,b1,width=r_out-r_mid,
                     facecolor=shade(cat_colors[c],0.45+0.12*j),edgecolor=WHITE,lw=1.5))
        m=np.radians((b0+b1)/2); rot=np.degrees(m); rot=rot-180 if 90<rot<270 else rot
        ax.text((r_out+0.12)*np.cos(m),(r_out+0.12)*np.sin(m),f"{sub}\n{val:.0f}%",
                ha="center",va="center",rotation=rot,rotation_mode="anchor",fontsize=8.5,color=NAVY)
        s2=b0
    start=a0
ax.text(0,0,"¿Por qué\nusamos\nredes?",ha="center",va="center",fontsize=14,fontweight="bold",color=NAVY)
ax.set_xlim(-1.55,1.55); ax.set_ylim(-1.45,1.45); ax.axis("off")
ax.set_title("Razones de uso de las redes sociales",fontsize=17,fontweight="bold",pad=14,color=NAVY)
ax.text(0,-1.40,"Fuente: DataReportal / GWI — Digital 2025 (Global Social Media Overview).\n"
        "% de usuarios que declaran cada motivo (multiseleccion).",ha="center",va="top",fontsize=8.5,color=GREY)
plt.tight_layout()
plt.savefig("viz_sunburst.png",dpi=180,bbox_inches="tight",facecolor=WHITE)
print("OK sunburst")
