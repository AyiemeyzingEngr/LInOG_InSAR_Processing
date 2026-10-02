import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
plt.rcParams['font.family']='DejaVu Sans'
R='/home/user/LInOG_InSAR_Processing/'
old=Image.open(R+'reports/P448F0290_Igram_Report_Page_1.jpg').convert('RGB')
new=Image.open(R+'linog_data/08_data_exports/LINOG_DELIVERY_v1.2_20260924_review/p448/f0290/LInOG_Upload_P448F0290/reports/P448F0290_Igram_Report_Page_1.jpg').convert('RGB')
crop=lambda im,box:im.crop(box)
T1=(25,270,665,630)          # first tile (phase + combined), page coordinates
T4=(2350,270,2990,630)       # fourth tile in row 1
NAVY='#1b4f72'; NEWE='#ca6f1e'; GREY='#7f8c8d'
fig=plt.figure(figsize=(13,9.6),dpi=170)
gs=fig.add_gridspec(2,3,height_ratios=[1.15,1],hspace=0.32,wspace=0.08)
a1=fig.add_subplot(gs[0,0:1]); a1.remove()
ax=fig.add_subplot(gs[0,:]); ax.axis('off')
ax_o=fig.add_axes([0.03,0.50,0.45,0.38]); ax_n=fig.add_axes([0.52,0.50,0.45,0.38])
for a,im,h,sub,c in [(ax_o,old,'YEAR 1 (reported June 2026)','FBS only · 11 dates · 36 interferograms · 3 report pages',GREY),
                     (ax_n,new,'YEAR 2, QUARTER 2 (this report)','FBS + FBD · 24 dates staged, 21 used · 149 formed / 129 inverted · 13 report pages',NEWE)]:
    a.imshow(im); a.axis('off')
    a.set_title(h,fontsize=12,weight='bold',color='white',pad=26,bbox=dict(boxstyle='round,pad=0.35',fc=c,ec=c))
    a.text(0.5,1.015,sub,transform=a.transAxes,ha='center',fontsize=9.5,weight='bold',color=NAVY)
fig.text(0.5,0.69,'➜',fontsize=30,color=NEWE,ha='center',va='center')
fig.text(0.5,0.955,'Interferogram report pages, ALOS-1 PALSAR Path 448 Frame 0290 (Cabanatuan–Gabaldon area): page 1 of each stack',ha='center',fontsize=12.5,weight='bold',color=NAVY)
zs=[(old,T1,'Same pair, Year 1 (FBS only)\n3 Feb 2007 – 22 Dec 2007 (322 days)',GREY),
    (new,T4,'Same pair, Year 2 Q2 (FBS+FBD stack)\n3 Feb 2007 – 22 Dec 2007 (322 days)',NEWE),
    (new,T1,'New short pair possible only with FBD dates\n3 Feb 2007 – 21 Jun 2007 (138 days)',NEWE)]
for k,(im,box,lab,c) in enumerate(zs):
    a=fig.add_axes([0.03+k*0.32,0.06,0.30,0.33]); a.imshow(crop(im,box)); a.set_xticks([]); a.set_yticks([])
    for s in a.spines.values(): s.set_edgecolor(c); s.set_linewidth(2.5)
    a.set_title(lab,fontsize=9.5,color=NAVY,weight='bold')
fig.text(0.03,0.42,'Zoom (left: wrapped phase; right: phase combined with amplitude)',fontsize=9,color='#555',style='italic')
plt.savefig('igram_compare.png',bbox_inches='tight',facecolor='white'); print('ok')
