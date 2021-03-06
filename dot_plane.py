
import bion_resolution as bion
import data
import math
filename="dot"

#dataset
focus=40
lamda=0.365
# space=lamda/2
size=0.1
thresh=0.1
xstart=-30
ystart=-30
zstart=0
xend=30
yend=30
z0=0
zend=45
i=0
j=0
NA=0.6
z=0
intparamater=0.002
field = 64
x=0
y=0
def phasefct(z):
    #lamda=0.365
    ph=360*z/lamda
    while ph >360:
        ph = ph -360
    return ph

def spacenum(start,end,sp):
    s=(end-start)/sp
    s_num=math.floor(s)
    return s_num
def NAfct(z):
    c1 = math.sin(field/2/(z)) 
    return c1
def intfunction(z):
    c2 = 0.95 - z*intparamater
    return c2

y0 = 0
x0 = 0
spaceparamater = data.paramaternumber
linenum = 2
z0 = 20
focus = 40
seedname = 'SEED'
f = open(seedname,'w')
j=0
i = 0
x = -20
y = -20
while x < 20 : 
    y = -20
    while y < 20:
        size = spaceparamater*lamda/2
        space = spaceparamater*lamda/2
        pitch = space + size  
        x = x0 + j * space
        #for j in range(spacenum(-0.5,0.5,thresh)):
        y = y0 + i * space
        z = z0
        trans = int(z)
        phase = phasefct(z+focus)
        NA = NAfct(z+focus)
        f.write("rect {0} {1} {2} {3} {4} {5} {6} {7}\n".format(x-size/2, y-size/2, size, size, trans, phase, z, NA))
        i = i +1
    i = 0
    j= j+1
f.close()


plot_csvname="seed_plot.csv"
bion.seedtxt_to_plotcsv(seedname,plot_csvname)
seedhtmlname = "seed_test"
plot=bion.Change(seedhtmlname,plot_csvname)
plot.plot_txt()
