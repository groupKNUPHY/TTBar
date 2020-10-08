import uproot as ROOT
import uproot_methods as upm
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
#import mplhep as hep
import sys


## argument check
try:
  input = raw_input
except:
  pass

if len(sys.argv) < 2:
	print(" running method: macro_file_name.py input_file_name.root")

## Read your Tree
dat = ROOT.open(sys.argv[1])["Delphes"]


## attatch to total events
tot_evt = dat.numentries

## Convert ROOT to jagged arrays
PT_arr, BTag_arr = dat.arrays(['Jet.PT', 'Jet.BTag'], outputtype = tuple)

## Grep your particles
BTagPT = PT_arr[BTag_arr == 1].flatten()
#BTagAlgoPT = PT_arr[BTagAlgo_arr == 1]
#BTagPhysPT = PT_arr[BTagPhys_arr == 1]
nTagPT = PT_arr[BTag_arr == 0].flatten()
#nTagAlgoPT = PT_arr[BTagAlgo_arr == 0]
#nTagPhysPT = PT_arr[BTagPhys_arr == 0]



print(BTagPT)
print(nTagPT)

## Using TLorentzVector, grep your particles


## UNDER DEBUGGING

## Set your Lorentz Vectors


## Draw histogram
#plt.style.use(hep.style.ROOT)
font_path = "/usr/share/fonts/stix/STIXGeneralItalic.otf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font',family=font_name)
plt.rcParams["figure.figsize"] = (10,6)
plt.hist(BTagPT,range=(0,300), bins=300, label='Tag',color='red', histtype='step')
plt.hist(nTagPT, range=(0,300), bins=300, label='nonTag',color='blue', histtype='step')
plt.xlim(0, 300)
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.title("Jet p$_{T}$",fontsize=15)
plt.xlabel("p$_{T}$ [GeV]", fontsize=15)
plt.ylabel("Number of Events | 1 GeV", fontsize=15)
plt.text(250, 200, "MADGRAPH 5",  ha='center',va='center',fontsize=25)
plt.minorticks_on()
plt.legend(fontsize=15)
plt.savefig("b_tag.png")


