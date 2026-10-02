# LInOG figure helpers: vector icons drawn with matplotlib primitives.
from matplotlib.patches import Circle, Rectangle, Polygon
import numpy as np
GATE='#117a65'
# ---------- icons (centre cx,cy; size s) ----------
def ic_gear(cx,cy,s,c):
    for a in range(0,360,45):
        t=np.radians(a); ax.add_patch(Rectangle((cx+np.cos(t)*s*0.62-s*0.13,cy+np.sin(t)*s*0.62-s*0.13),s*0.26,s*0.26,angle=0,fc=c,ec=c,zorder=5))
    ax.add_patch(Circle((cx,cy),s*0.55,fc=c,zorder=5)); ax.add_patch(Circle((cx,cy),s*0.22,fc='white',zorder=6))
def ic_archive(cx,cy,s,c):
    ax.add_patch(Rectangle((cx-s*0.6,cy-s*0.55),s*1.2,s*0.85,fc=c,zorder=5))
    ax.add_patch(Rectangle((cx-s*0.7,cy+s*0.3),s*1.4,s*0.3,fc=c,ec='white',lw=1.2,zorder=6))
    ax.add_patch(Rectangle((cx-s*0.22,cy+s*0.02),s*0.44,s*0.13,fc='white',zorder=7))
def ic_merge(cx,cy,s,c):
    for dy in (0.45,-0.45):
        ax.annotate('',xy=(cx+s*0.05,cy),xytext=(cx-s*0.75,cy+dy*s),arrowprops=dict(arrowstyle='-',color=c,lw=3),zorder=5)
    ax.annotate('',xy=(cx+s*0.8,cy),xytext=(cx,cy),arrowprops=dict(arrowstyle='-|>',color=c,lw=3,mutation_scale=14),zorder=5)
    ax.text(cx-s*0.85,cy+s*0.62,'FBS',fontsize=5.5,color=c,ha='center',weight='bold'); ax.text(cx-s*0.85,cy-s*0.8,'FBD',fontsize=5.5,color=c,ha='center',weight='bold')
def ic_mountain(cx,cy,s,c):
    ax.add_patch(Polygon([[cx-s*0.85,cy-s*0.5],[cx-s*0.2,cy+s*0.55],[cx+s*0.35,cy-s*0.5]],fc=c,zorder=5))
    ax.add_patch(Polygon([[cx-s*0.05,cy-s*0.5],[cx+s*0.4,cy+s*0.25],[cx+s*0.85,cy-s*0.5]],fc=c,alpha=0.65,zorder=5))
    ax.plot([cx-s*0.9,cx+s*0.9],[cy-s*0.5,cy-s*0.5],color=c,lw=2,zorder=5)
def ic_layers(cx,cy,s,c):
    for k,dy in enumerate((-0.4,0,0.4)):
        ax.add_patch(Polygon([[cx-s*0.8,cy+dy*s],[cx,cy+dy*s+s*0.28],[cx+s*0.8,cy+dy*s],[cx,cy+dy*s-s*0.28]],fc=c,ec='white',lw=1.2,alpha=0.55+0.15*k,zorder=5+k))
def ic_fringe(cx,cy,s,c):
    cols=['#c0392b','#e67e22','#f1c40f','#27ae60','#2980b9','#8e44ad']
    for k,col in enumerate(cols):
        ax.add_patch(Circle((cx,cy),s*(0.85-0.13*k),fc=col,ec='white',lw=0.6,zorder=5+k))
def ic_grid(cx,cy,s,c):
    for i in range(2):
        for j in range(2):
            ax.add_patch(Rectangle((cx-s*0.7+i*s*0.75,cy-s*0.7+j*s*0.75),s*0.65,s*0.65,fc=c,alpha=0.85,zorder=5))
    ax.add_patch(Circle((cx+s*0.45,cy-s*0.4),s*0.32,fc='white',ec=GATE,lw=2,zorder=7)); ax.plot([cx+s*0.32,cx+s*0.43,cx+s*0.6],[cy-s*0.4,cy-s*0.52,cy-s*0.25],color=GATE,lw=1.8,zorder=8)
def ic_chart(cx,cy,s,c):
    ax.plot([cx-s*0.75,cx-s*0.75,cx+s*0.8],[cy+s*0.7,cy-s*0.65,cy-s*0.65],color=c,lw=2.2,zorder=5)
    xs=np.linspace(-0.6,0.7,8); ys=0.45-0.85*(xs+0.6)/1.3+0.08*np.sin(xs*12)
    ax.plot(cx+xs*s,cy+ys*s,color='#c0392b',lw=2.2,zorder=6); ax.scatter(cx+xs*s,cy+ys*s,s=6,color='#c0392b',zorder=7)
def ic_map(cx,cy,s,c):
    ax.add_patch(Polygon([[cx-s*0.85,cy-s*0.6],[cx-s*0.85,cy+s*0.5],[cx-s*0.3,cy+s*0.7],[cx+s*0.3,cy+s*0.5],[cx+s*0.85,cy+s*0.7],[cx+s*0.85,cy-s*0.4],[cx+s*0.3,cy-s*0.6],[cx-s*0.3,cy-s*0.4]],fc=c,alpha=0.75,zorder=5))
    ax.add_patch(Circle((cx+s*0.05,cy+s*0.2),s*0.28,fc='#c0392b',zorder=6)); ax.add_patch(Polygon([[cx-s*0.18,cy+s*0.08],[cx+s*0.28,cy+s*0.08],[cx+s*0.05,cy-s*0.35]],fc='#c0392b',zorder=6)); ax.add_patch(Circle((cx+s*0.05,cy+s*0.22),s*0.1,fc='white',zorder=7))
def ic_lens(cx,cy,s,c):
    ax.add_patch(Circle((cx-s*0.15,cy+s*0.15),s*0.48,fc='white',ec=c,lw=3,zorder=5))
    ax.plot([cx+s*0.2,cx+s*0.75],[cy-s*0.2,cy-s*0.75],color=c,lw=4,solid_capstyle='round',zorder=5)
    ax.plot([cx-s*0.45,cx-s*0.25,cx-s*0.05,cx+s*0.12],[cy+s*0.3,cy+s*0.05,cy+s*0.1,cy-s*0.05],color='#c0392b',lw=1.6,zorder=6)

