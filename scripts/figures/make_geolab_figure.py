import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
from matplotlib.patches import FancyBboxPatch
from PIL import Image
exec(open('/tmp/claude-0/fig/icons.py').read())
plt.rcParams['font.family']='DejaVu Sans'
NAVY='#1b4f72'; NEWE='#ca6f1e'; OUTE='#1e8449'; OUTF='#f4fbf6'; STDF='#eef5fb'; GREY='#555'
fig,ax=plt.subplots(figsize=(13,8.6),dpi=180); ax.set_xlim(0,130); ax.set_ylim(0,86); ax.axis('off'); ax.set_aspect('equal')
def rbox(x,y,w,h,fc,ec,lw=1.5): ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.3,rounding_size=1.2',fc=fc,ec=ec,lw=lw))
ax.text(65,85,'LInOG tutorial route on EarthScope GeoLab (manual v4.0, Chapter 11)',ha='center',va='top',fontsize=15,weight='bold',color=NAVY)
ax.text(65,81.2,'A browser-based JupyterLab server: trainees run the LInOG notebook on a four-date demonstration stack without access to the project server',ha='center',va='top',fontsize=9.5,color=GREY)
steps=[('1','EarthScope account','Google log-in to\nthe GeoLab hub',ic_gear),
       ('2','Start a server','29 GB profile:\n3.66 CPU cores,\n29,776 MiB memory',ic_layers),
       ('3','One-time install','ISCE2, MintPy,\nGDAL, SNAPHU into\nhome (~7 min)',ic_archive),
       ('4','Demonstration stack','Path 449 Frame 0290:\n4 dates, 6 pairs\n(2008)',ic_mountain),
       ('5','Run the notebook','Cells 0–18 call\nthe LInOG scripts,\nPhases 0–6',ic_chart),
       ('6','Check and deliver','18-item run check;\n16 products',ic_map)]
W=19.2; x0=2.0; y=56
for i,(n,t,b,icn) in enumerate(steps):
    x=x0+i*(W+2.2)
    rbox(x,y,W,20,STDF,NAVY)
    ax.add_patch(plt.Circle((x+W/2,y+14.3),3.8,fc='white',ec=NAVY,lw=1.6)); icn(x+W/2,y+14.3,2.6,NAVY)
    ax.text(x+1.0,y+19.2,'Step '+n,fontsize=8,weight='bold',color=NAVY,va='top')
    ax.text(x+W/2,y+9.2,t,ha='center',va='top',fontsize=8.6,weight='bold',color=NAVY)
    ax.text(x+W/2,y+5.6,b,ha='center',va='top',fontsize=7.0,color='#222',linespacing=1.3)
    if i<5: ax.annotate('',xy=(x+W+2.0,y+10),xytext=(x+W+0.25,y+10),arrowprops=dict(arrowstyle='-|>',color=NAVY,lw=1.6,mutation_scale=12))
ax.text(65,52.3,'REAL OUTPUTS PRODUCED ON GEOLAB (September 2026; four-date demonstration stack, for training only)',ha='center',fontsize=10,weight='bold',color=OUTE)
outs=[('s35_1.jpg','Phase 4.5: interferogram report sheet\n(GeoLab, 20 Sept 2026)'),
      ('s35_2.png','Phase 5: velocity in radar coordinates\n(GeoLab, 22 Sept 2026)'),
      ('s35_3.jpg','Phase 6: delivered velocity map, cm/yr\n(GeoLab, 20 Sept 2026)')]
OW=40.5
for k,(f,cap) in enumerate(outs):
    x=2.0+k*(OW+2.25); rbox(x,1.5,OW,47,OUTF,OUTE)
    im=np.asarray(Image.open(f).convert('RGB')); h,w=im.shape[:2]; bw,bh=OW-3,36; s=min(bw/w,bh/h); dw,dh=w*s,h*s
    ax.imshow(im,extent=(x+1.5+(bw-dw)/2,x+1.5+(bw+dw)/2,10.5+(bh-dh)/2,10.5+(bh+dh)/2),zorder=3)
    ax.text(x+OW/2,8.6,cap,ha='center',va='top',fontsize=8.4,color='#222',linespacing=1.3)
plt.savefig('geolab_route.png',bbox_inches='tight',facecolor='white'); print('ok')
