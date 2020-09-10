## rootpy I/O
from rootpy.io import root_open

## rootpy for histograming
from rootpy.plotting import Hist, HistStack, Legend, Canvas

## rootpy for matplotlib 
import rootpy.plotting.root2matplotlib as rplt
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager

## opening your own root file. please change "input*.root" to your own file name
myfile1 = root_open("input1.root")
myfile2 = root_open("input2.root")
myfile3 = root_open("input3.root")
#myfile4 = root_open("input4.root")
#myfile5 = root_open("input5.root")
#myfile6 = root_open("input6.root")

## cloning your histogram input*.root file.
## please change pt term to your own name of histogram

myhist1 = myfile1.pt.Clone()
myhist2 = myfile2.pt.Clone()
myhist3 = myfile3.pt.Clone()
#myhist4 = myfile3.mpt.Clone()
#myhist5 = myfile4.ept.Clone()
#myhist6 = myfile4.mpt.Clone()
#myhist7 = myfile5.met.Clone()
#myhist8 = myfile6.met.Clone()


## set your histogram for you want to see physik
G=(myhist1)
H=(myhist2)
I=(myhist3)
#J=(myhist5 + myhist6 + myhist8)



## Set parameters for plotting
font_path = "/usr/share/fonts/stix/STIXGeneralItalic.otf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font',family=font_name)
plt.rcParams["figure.figsize"] = (10,6)
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.title("b quark p$_{T}$",fontsize=15)
#plt.grid(which='major', linestyle='-.')
plt.xlabel("p$_{T}$ [GeV]", fontsize=15)
plt.ylabel("Number of Events", fontsize=15)
#plt.text(280, 500, "COMBINED",  ha='center',va='center',fontsize=25)
#plt.text(300, 75, "+ DELPHES3",  ha='center',va='center',fontsize=25)
#plt.plot(myhist1, label='W+')
#plt.plot(myhist2, label='W-')
#plt.legend(['W+', 'W-'], fontsize=15)
plt.minorticks_on()


## Draw hist
rplt.hist(G, linewidth=3,label='POWHEG v1 NLO',color="royalblue")
rplt.hist(H, linewidth=3,label='POWHEG v1 NNLO',color="red")
rplt.hist(I, linewidth=3,label='MADGRAPH5 NLO',color="black")
#rplt.hist(J, linewidth=3,label='nn23lo1 Delphes',color="green")


plt.legend(fontsize=15)
#plt.show()

plt.savefig("output.png")
