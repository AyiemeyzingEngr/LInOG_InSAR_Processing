import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon
from PIL import Image
exec(open('icons.py').read())
F='/home/user/LInOG_InSAR_Processing/linog_data/04_methods_notes/FBS FBD/v4.0_figures/'
def load(f,crop=None):
    im=Image.open(F+f).convert('RGB')
    if crop:
        w,h=im.size; im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
    return np.asarray(im)
NAVY='#1b4f72'; NEWE='#ca6f1e'; NEWF='#fdf2e9'; STDF='#eef5fb'; OUTF='#f4fbf6'; OUTE='#1e8449'; GATE='#117a65'; GREY='#555'
fig,ax=plt.subplots(figsize=(12,23),dpi=170); ax.set_xlim(0,120); ax.set_ylim(0,230); ax.axis('off'); ax.set_aspect('equal')
def rbox(x,y,w,h,fc,ec,lw=1.5):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.3,rounding_size=1.5',fc=fc,ec=ec,lw=lw,zorder=2))
P=[
 ('0','Set-up and pre-flight','Install ISCE2, MintPy, GDAL and SNAPHU;\ncheck software provenance; size the\nmachine; count the archive',ic_gear,False,'provenance check',
  'TERM','Summary of the pre-flight\nrecord: all 14 checks pass\nbefore any data is touched'),
 ('1','Unpack and unify FBS + FBD','Unzip ALOS-1 L1.1 granules; beam check;\nsort dates into FBS / FBD; band-limit\nthe FBS dates to the common 14 MHz\nat their native 4.68 m range sampling','merge',True,'gates G1–G6',
  ('fig3_2.png',(0,0,1,1)),'Range spectra: FBS before\n(red) and after (dark) band-\nlimiting match FBD (green)'),
 ('2','DEM and network design','Shared DEM; select pairs with temporal\nbaseline ≤ 730 days and perpendicular\nbaseline ≤ 1,500 m',ic_mountain,False,'gate G17',
  ('fig4_2.png',(0,0,1,1)),'Baseline network of the\ninterferogram pairs,\n2007–2011'),
 ('3','Coregistration','Align every SLC to one FBS reference\ndate (4.68 m range grid; FBD dates are\nresampled onto it); misregistration\ninversion pinned to the reference date',ic_layers,False,'gates G7–G9, G16, G21',
  ('fig5_2.png',(0,0,1,1)),'Coregistration residuals\nper date, checked against\nthe tolerance band'),
 ('4','Interferogram generation','Form interferograms; multilook\n28 × 12 (~90 m × 90 m); filter;\nunwrap the phase with SNAPHU',ic_fringe,False,'gates G10, G11, G18, G20',
  ('fig6_2.jpg',(0,0.03,0.49,1)),'Filtered interferogram,\n8 Jan – 23 Feb 2008; each\ncolour cycle is one fringe'),
 ('4.5','Visual quality control','Phase and amplitude report pages for\nevery interferogram; poor pairs are\nflagged and excluded',ic_grid,False,'visual check',
  ('fig7_1.jpg',(0,0,1,1)),'Interferogram report page\nused to inspect every pair'),
 ('5','SBAS time-series analysis','MintPy network inversion; DEM-error\ncorrection; ramp removal; coherence\nand water masks',ic_chart,False,'gates G12, G13, G15, G19, G22, G23',
  ('fig8_2.png',(0,0,1,1)),'MintPy interferogram\nnetwork coloured by\ncoherence; coherence matrix'),
 ('6','Geocoding, delivery, verification','Geocode to a common 1/1200° (~90 m)\ngrid; export 16 products per frame;\n27-check verification',ic_map,False,'gate G14; 27 checks',
  ('fig9_2.jpg',(0,0,1,1)),'Delivered LOS velocity\nmap (cm/yr), one of 16\nproducts per frame'),
 ('7','Interpretation','Read the velocity maps; measure\nsubsidence against nearby stable\nground on both tracks',ic_lens,False,'two-track check',
  ('fig10_2.png',(0,0,0.445,0.93)),'Cabanatuan subsidence\nbowl on Path 448 (left)\nand Path 449 (right)'),
]
ax.text(60,228.5,'LInOG ALOS-1 PALSAR FBS + FBD InSAR Processing Workflow',ha='center',va='top',fontsize=16,weight='bold',color=NAVY)
ax.text(60,224.4,'Pipeline v4.0: each processing phase (left) and a real output it produced (right); sample frame Path 449 Frame 0280 unless noted',ha='center',va='top',fontsize=9.5,color=GREY)
ax.text(27,219.6,'PROCESSING PHASE',ha='center',fontsize=9.5,weight='bold',color=NAVY)
ax.text(89,219.6,'REAL OUTPUT OF THE PHASE',ha='center',fontsize=9.5,weight='bold',color=OUTE)
H=21.5; gap=2.4; y=217.5
PX,PW=1,54; OX,OW=61,58
for num,title,body,icon,new,gate,img,cap in P:
    y0=y-H; ec=NEWE if new else NAVY; fc=NEWF if new else STDF
    rbox(PX,y0,PW,H,fc,ec,2.2 if new else 1.5)
    cx,cy=PX+7,y0+H/2
    ax.add_patch(Circle((cx,cy),5.2,fc='white',ec=ec,lw=1.8,zorder=3))
    col=NEWE if new else NAVY
    (ic_merge if icon=='merge' else icon)(cx,cy,3.5,col)
    ax.text(PX+14,y0+H-2.2,f'Phase {num}',fontsize=9,color=ec,weight='bold',va='top')
    if new: ax.text(PX+PW-1.2,y0+H-1.8,'NEW IN YEAR 2',fontsize=7.4,color='white',weight='bold',va='top',ha='right',bbox=dict(boxstyle='round,pad=0.3',fc=NEWE,ec=NEWE))
    ax.text(PX+14,y0+H-5.4,title,fontsize=11.2,color=NAVY,weight='bold',va='top')
    ax.text(PX+14,y0+H-9.0,body,fontsize=8.4,color='#222',va='top',linespacing=1.32)
    ax.text(PX+14,y0+1.4,gate,fontsize=7.6,color=GATE,style='italic',va='bottom')
    rbox(OX,y0,OW,H,OUTF,OUTE,1.5)
    ax.annotate('',xy=(OX-0.5,y0+H/2),xytext=(PX+PW+0.6,y0+H/2),arrowprops=dict(arrowstyle='-|>',color=OUTE,lw=2,mutation_scale=15),zorder=4)
    # image area: left part of output box
    ix0,iy0,iw,ih=OX+1.0,y0+1.0,31.0,H-2.0
    if img=='TERM':
        ax.add_patch(Rectangle((ix0,iy0),iw,ih,fc='#1e1e1e',ec='#444',zorder=3))
        lines=['# pre-flight record (felix, 17 Sep 2026)','  software provenance ......... OK','  ISCE2 · MintPy · GDAL · SNAPHU  OK','  machine: 48 cores, 125 GB RAM','  archive: 779 ALOS-1 L1.1 zips','  RESULT: PASS 14/14']
        for k,l in enumerate(lines):
            ax.text(ix0+1.0,iy0+ih-2.2-k*3.0,l,fontsize=6.2,family='DejaVu Sans Mono',color=('#7dcea0' if 'PASS' in l else '#eaeaea'),va='top',zorder=4)
    else:
        a=load(*img); h,w=a.shape[:2]
        s=min(iw/w,ih/h); dw,dh=w*s,h*s
        ex=(ix0+(iw-dw)/2,ix0+(iw+dw)/2,iy0+(ih-dh)/2,iy0+(ih+dh)/2)
        ax.add_patch(Rectangle((ix0,iy0),iw,ih,fc='white',ec='#cfd8dc',lw=0.8,zorder=3))
        ax.imshow(a,extent=ex,zorder=4,interpolation='antialiased')
    ax.text(OX+33.5,y0+H-2.0,'OUTPUT',fontsize=7,color='white',weight='bold',va='top',bbox=dict(boxstyle='round,pad=0.25',fc=OUTE,ec=OUTE))
    ax.text(OX+33.5,y0+H-6.0,cap,fontsize=7.9,color='#222',va='top',linespacing=1.4)
    y=y0-gap
    if num!='7': ax.annotate('',xy=(PX+PW/2,y+0.2),xytext=(PX+PW/2,y0-0.3),arrowprops=dict(arrowstyle='-|>',color=NAVY,lw=1.8,mutation_scale=14),zorder=4)
ly=y-3.5
for j,(fc,ec,lab) in enumerate([(NEWF,NEWE,'new for FBS+FBD processing'),(STDF,NAVY,'carried over from FBS-only'),(OUTF,OUTE,'real output of the phase')]):
    lx=2+j*40; rbox(lx,ly,4.5,2.6,fc,ec,1.5); ax.text(lx+6,ly+1.3,lab,fontsize=8.4,va='center',color='#333')
ax.text(2,ly-3.4,'Green italic labels: automated quality gates (G1–G23) and checks; a failed gate stops the phase until the cause is fixed.',fontsize=8,color=GATE,style='italic')
ax.set_ylim(ly-6,230)
plt.savefig('fbsfbd_workflow.png',bbox_inches='tight',facecolor='white',pad_inches=0.15); print('ok')
