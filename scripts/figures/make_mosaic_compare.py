# LInOG figure script: Year 1 FBS-only vs Year 2 Q2 FBS+FBD LOS velocity mosaic (same deramped product, +/-5 cm/yr).
# Inputs: *_Velocity_demErr_ramp.tif of the v1.2 delivery (12 frames) in the working dir and Year 1 P448 files in ./y1/.
import rasterio,glob,numpy as np,matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.family']='DejaVu Sans'
step=1/1200; S,N,W,E=14.45,17.2,119.95,122.1
def mosaic(files):
    H=int(round((N-S)/step)); Wd=int(round((E-W)/step)); M=np.full((H,Wd),np.nan); fp={}
    for f in files:
        with rasterio.open(f) as r:
            a=r.read(1).astype(float); t=r.transform
            if r.nodata is not None: a[a==r.nodata]=np.nan
            r0=int(round((N-t.f)/step)); c0=int(round((t.c-W)/step)); sub=M[r0:r0+a.shape[0],c0:c0+a.shape[1]]; m=np.isfinite(a); sub[m]=a[m]*100
            k=f.split('/')[-1][:9]; fp[k]=(t.c,t.c+a.shape[1]*step,t.f-a.shape[0]*step,t.f)
    return M,fp
order=['P447F0300','P447F0310','P449F0280','P449F0290','P449F0300','P449F0310','P449F0320','P448F0280','P448F0290','P448F0300','P448F0310','P448F0320']
M1,f1=mosaic(sorted(glob.glob('y1/*.tif')))
M2,f2=mosaic([f'{k}_Velocity_demErr_ramp.tif' for k in order])
cols={'P447':'#6c3483','P448':'#1b4f72','P449':'#117a65'}
sites=[('Cabanatuan',120.9667,15.4867),('Dagupan',120.334,16.043),('La Trinidad',120.588,16.455)]
fig,axs=plt.subplots(1,2,figsize=(13.5,9.2),dpi=200,gridspec_kw=dict(wspace=0.12))
heads=[('YEAR 1 (reported June 2026)','FBS only · Path 448 · 5 frames','10 dates/frame · 34–36 interferograms/frame\n~10,000 km² reported · no water mask'),
       ('YEAR 2, QUARTER 2 (this report)','FBS + FBD · Paths 447–449 · 12 frames','19–24 dates/frame · 1,634 interferograms in total\n27,893 km² with valid data · water-masked (v1.2)')]
for ax,(M,fp),(h1,h2,h3),hc in zip(axs,[(M1,f1),(M2,f2)],heads,['#7f8c8d','#ca6f1e']):
    ax.set_facecolor('#e9e9e9')
    im=ax.imshow(M,extent=(W,E,S,N),cmap='RdYlBu_r',vmin=-5,vmax=5,interpolation='nearest')
    for k,(w,e,s,n) in fp.items(): ax.plot([w,e,e,w,w],[s,s,n,n,s],color=cols[k[:4]],lw=0.7,alpha=0.8)
    for name,x,y in sites:
        ax.plot(x,y,marker='o',ms=4.5,mfc='white',mec='black',mew=1,zorder=5)
        ax.text(x+0.04,y+0.03,name,fontsize=7.5,weight='bold',zorder=6,bbox=dict(boxstyle='round,pad=0.12',fc='white',ec='none',alpha=0.8))
    ax.set_xlim(W,E); ax.set_ylim(S,N); ax.set_aspect(1/np.cos(np.radians(15.8)))
    ax.grid(color='white',lw=0.5,alpha=0.7); ax.tick_params(labelsize=8)
    ax.set_xlabel('Longitude (°E)',fontsize=9)
    ax.text(0.5,1.115,h1,transform=ax.transAxes,ha='center',fontsize=12,weight='bold',color='white',bbox=dict(boxstyle='round,pad=0.35',fc=hc,ec=hc))
    ax.text(0.5,1.06,h2,transform=ax.transAxes,ha='center',fontsize=10.5,weight='bold',color='#1b4f72')
    ax.text(0.03,0.03,h3,transform=ax.transAxes,fontsize=8.3,va='bottom',bbox=dict(boxstyle='round,pad=0.35',fc='white',ec='#bbb',alpha=0.92))
    x0,y0=121.55,14.55; dl=50/(111.32*np.cos(np.radians(14.6))); ax.plot([x0,x0+dl],[y0,y0],color='k',lw=3); ax.text(x0+dl/2,y0+0.04,'50 km',ha='center',fontsize=7.5)
axs[0].set_ylabel('Latitude (°N)',fontsize=9); axs[1].set_yticklabels([])
for p,(x,y) in {'P447':(121.95,16.69),'P448':(121.33,17.165),'P449':(120.3,17.165)}.items(): axs[1].text(x,y,'Path '+p[1:],color=cols[p],fontsize=8.5,weight='bold',ha='center',va='bottom')
axs[0].text(121.33,17.165,'Path 448',color=cols['P448'],fontsize=8.5,weight='bold',ha='center',va='bottom')

cb=fig.colorbar(im,ax=axs,shrink=0.55,pad=0.015,extend='both'); cb.set_label('LOS velocity (cm/yr), deramped\nnegative = away from satellite (subsidence)',fontsize=9)
fig.canvas.draw()
p0=axs[0].get_position(); p1=axs[1].get_position()
fig.text((p0.x1+p1.x0)/2,(p0.y0+p0.y1)/2,'➜',fontsize=30,color='#ca6f1e',ha='center',va='center')
fig.text((p0.x0+p1.x1)/2,p0.y1+0.215*(p0.y1-p0.y0),'Progression of LInOG ALOS-1 PALSAR ground-velocity coverage, 2007–2011 (ascending tracks, same colour scale)',fontsize=12.5,weight='bold',color='#1b4f72',ha='center')
plt.savefig('mosaic_compare.png',bbox_inches='tight',facecolor='white'); print('ok')
