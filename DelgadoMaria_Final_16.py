import numpy as np
import matplotlib.pylab as plt




x=np.linspace(0,100,100)

def f(x,y,t,v):
    return(x)

def metropolis(x,y,t,v):

    xini=np.random.uniform(x,y,1)
    yini=np.random.uniform(x,y,1)
    tini=np.random.uniform(0,t,1)
    vini=np.random.uniform(0,v,1)
    xcamina=np.zeros((0))
    ycamina=np.zeros((0))
    tcamina=np.zeros((0))
    vcamina=np.zeros((0))
    xcamina= np.append(xcamina,xini)
    ycamina = np.append(ycamina,yini)
    tcamina= np.append(tcamina,tini)
    vcamina=np.append(vcamina,vini)
    n=1000
    sigma=0.1
    for i in range(n):
        xn=np.random.normal(xcamina[i],sigma)
        yn=np.random.normal(ycamina[i],sigma)
        tn=np.random.normal(tcamina[i],sigma)
        vn=np.random.normal(vcamina[i],sigma)
        alfa=f(xn,yn,tn,vn)/f(xcamina[i],ycamina[i],tcamina[i],vcamina[i] )
        if(alfa>=1.0):
            xcamina= np.append(xcamina,xn)
            ycamina=  np.append(ycamina,yn)
            tcamina=  np.append(tcamina,tn)
            vcamina=  np.append(vcamina,vn)
        if(alfa<1.0):
            beta=np.random.random()
            if(beta<alfa):
                xcamina= np.append(xcamina,xn)
                ycamina=  np.append(ycamina,yn)
                tcamina=  np.append(tcamina,tn)
                vcamina=  np.append(vcamina,vn)
            else:
                xcamina= np.append(xcamina,xcamina[i])
                ycamina=  np.append(ycamina,ycamina[i])
                tcamina=  np.append(tcamina,tcamina[i])
                vcamina=  np.append(vcamina,vcamina[i])
    
    return("coordenada x", xcamina, "coordenada y", ycamina, "tiempo de lanzamiento", tcamina, "velocidad del sonido", vcamina  )

print(metropolis(4,100,62, 299792458))
