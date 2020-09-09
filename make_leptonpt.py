import argparse
from rootpy.io import root_open
import rootpy.ROOT as ROOT
from rootpy.plotting import Hist, HistStack, Legend, Canvas
import rootpy.plotting.root2matplotlib as rplt
import matplotlib.pyplot as plt

# --Setup parser
parser = argparse.ArgumentParser()
parser.add_argument('infile', type=str,
            help="INPUT_ROOTFILE_PATH")
parser.add_argument('--save', type=bool,default=False,
            help="--save True/False")
parser.add_argument('--TCanvas', type=bool,default=False,
            help="--TCanvas True/False")

args = parser.parse_args()




# --Set your Delphes/libDelphes.so path, header path
ROOT.gSystem.Load("/home/twkim/MG5_aMC_v2_7_3/ExRootAnalysis/libExRootAnalysis.so")



try:
  ROOT.gInterpreter.Declare('#include "/home/twkim/MG5_aMC_v2_7_3/ExRootAnalysis/ExRootAnalysis/ExRootClasses.h"')
  ROOT.gInterpreter.Declare('#include "/home/twkim/MG5_aMC_v2_7_3/ExRootAnalysis/ExRootAnalysis/ExRootTreeReader.h"')
except:
  pass



# Read & Write File
inputFile = args.infile

if args.save:
	outputFile = root_open("powheg_muon.root","recreate")

# Create chain of root trees
chain = ROOT.TChain("LHEF")
chain.Add(inputFile)

# Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

# Get pointers to branches used in this analysis
branchParticle = treeReader.UseBranch("Particle")
# branchElectron = treeReader.UseBranch("Electron")

# Define histograms
histPT = ROOT.TH1F("pt", "P_{T} distribution",100, 0, 400.0)




# --EventLoop start
for entry in range(0, numberOfEntries):
	# Load selected branches with data from specified event
	treeReader.ReadEntry(entry)

	# If event contains at least 1 electrons
	if branchParticle.GetEntries() == 0:
		continue
	
	for i in range(0, branchParticle.GetEntries()):

		a = branchParticle.At(i)
		if abs(a.PID) in [11,12,13,14]:
			histPT.Fill(a.PT)


# I/O
if args.save:
	outputFile.write()
	outputFile.close()

# -- EventLoop Ends

# --Show histogram using TCanvas
if (not args.save and args.TCanvas ):

	c1 = ROOT.TCanvas()
	c1.cd()
	histMass.GetXaxis().SetTitle("Jet PT [GeV]")
	histMass.GetYaxis().SetTitle("Events")
	histMass.Draw("Hist")
	dummy=input("Press Enter to continue...")


# --Show histogram using Matplotlib
if (not args.save and not args.TCanvas):
	# Set parametres for plotting
	plt.rcParams["figure.figsize"] = (10,6)
	plt.rc('xtick', labelsize=15)
	plt.rc('ytick', labelsize=15)
	plt.title("Transverse mass", fontsize=25)
	plt.xlabel("$M_{T} [GeV]$",fontsize=15)
	plt.ylabel("Events",fontsize=15)
	
	plt.grid(which='major', linestyle='-.')
	
	# Draw hist
	rplt.hist(histMass,linewidth=3, color="royalblue",label="W^{+} transverse mass")
	plt.xticks([0,20,40,60,80,100,120,140,160,180,200])
	plt.yticks([0,20,40,60,80,100,120,140])
	plt.legend()
	plt.show()


