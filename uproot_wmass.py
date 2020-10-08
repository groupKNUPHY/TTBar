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
dat = ROOT.open(sys.argv[1])["LHEF"]


## attatch to total events
tot_evt = dat.numentries

## Convert ROOT to jagged arrays
PID_arr, Px_arr, Py_arr, Pz_arr, E_arr = dat.arrays(['Particle.PID','Particle.Px','Particle.Py','Particle.Pz','Particle.E'],outputtype=tuple)

## Using TLorentzVector, grep your particles
lm_px, lm_py, lm_pz, lm_E = Px_arr[PID_arr == 11], Py_arr[PID_arr == 11], Pz_arr[PID_arr == 11], E_arr[PID_arr == 11]
vl_px, vl_py, vl_pz, vl_E = Px_arr[PID_arr == -12], Py_arr[PID_arr == -12], Pz_arr[PID_arr == -12], E_arr[PID_arr == -12]
lp_px, lp_py, lp_pz, lp_E = Px_arr[PID_arr == -11], Py_arr[PID_arr == -11], Pz_arr[PID_arr == -11], E_arr[PID_arr == -11]
vlb_px, vlb_py, vlb_pz, vlb_E = Px_arr[PID_arr == 12], Py_arr[PID_arr == 12], Pz_arr[PID_arr == 12], E_arr[PID_arr == 12]


#b_px, b_py, b_pz, b_E = Px_arr[PID_arr == -5], Py_arr[PID_arr == -5], Pz_arr[PID_arr == -5], E_arr[PID_arr == -5]

## Set your Lorentz Vectors
lm_Vector = upm.TLorentzVectorArray.from_cartesian(lm_px, lm_py, lm_pz, lm_E)
vl_Vector = upm.TLorentzVectorArray.from_cartesian(vl_px, vl_py, vl_pz, vl_E)
lp_Vector = upm.TLorentzVectorArray.from_cartesian(lp_px, lp_py, lp_pz, lp_E)
vlb_Vector = upm.TLorentzVectorArray.from_cartesian(vlb_px, vlb_py, vlb_pz, vlb_E)

wm_Vector = lm_Vector.flatten() + vl_Vector.flatten()
wp_Vector = lp_Vector.flatten() + vlb_Vector.flatten()


## Draw histogram
#plt.style.use(hep.style.ROOT)
font_path = "/usr/share/fonts/stix/STIXGeneralItalic.otf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font',family=font_name)
plt.rcParams["figure.figsize"] = (10,6)
plt.hist(wm_Vector.mt, range=(0,400),bins=400, label='W- boson',color="red", histtype='step')
plt.hist(wp_Vector.mt, range=(0,400),bins=400,label='W+ boson',color="blue", histtype='step')
plt.xlim(0, 400)
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.title("W m$_{T}$",fontsize=15)
plt.xlabel("m$_{T}$ [GeV]", fontsize=15)
plt.ylabel("Number of Events | 1 GeV", fontsize=15)
#plt.text(300, 200, "TEST",  ha='center',va='center',fontsize=25)
plt.minorticks_on()
plt.legend(fontsize=15)
plt.savefig("w_tvmass2.png")



