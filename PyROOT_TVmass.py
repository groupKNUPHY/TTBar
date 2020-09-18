import sys
import ROOT
import numpy as np

try:
  input = raw_input
except:
  pass

if len(sys.argv) < 2:
	print(" running method: macro_file_name.py input_file_name.root")
	sys.exit(1)


## Set your Delphes/libDelphes.so path, header path
ROOT.gSystem.Load("/home/twkim/MG5_aMC_v2_7_3/ExRootAnalysis/libExRootAnalysis.so") ### <- If you wanna change to delphes, rewrite this line to your PATH

try:
  ROOT.gInterpreter.Declare('#include "/home/twkim/MG5_aMC_v2_7_3/ExRootAnalysis/ExRootAnalysis/ExRootClasses.h"') ### <- If you wanna change to delphes, rewrite this line to your PATH
  ROOT.gInterpreter.Declare('#include "/home/twkim/MG5_aMC_v2_7_3/ExRootAnalysis/ExRootAnalysis/ExRootTreeReader.h"')
except:
  pass


## Read & Write File
inputFile = sys.argv[1]
outputFile = ROOT.TFile.Open("Gwayeon.root","recreate") ### <- Set Your output file name

## Create chain of root trees
chain = ROOT.TChain("LHEF")
chain.Add(inputFile)

## Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

## Get pointers to branches used in this analysis
branchParticle = treeReader.UseBranch("Particle")

## if you want to use another branch, follow this line after"
# branchXXX = treeReader.UseBranch("your_own_branch")

## Define histograms
histLorentz = ROOT.TH1F("TV Lorentz", "W Transverse mass1",200, 0, 200.0)
histCosine  = ROOT.TH1F("TV Cosine", "W Transverse mass2",200, 0, 200.0)

## Define electron and neutrino
e = ROOT.TLorentzVector()
v = ROOT.TLorentzVector()


## EventLoop start
for entry in range(0, numberOfEntries):
	# Load selected branches with data from specified event
	treeReader.ReadEntry(entry)
	
	# If event contains at least 1 particle
	if branchParticle.GetEntries() == 0:
		continue
	
	for i in range(0, branchParticle.GetEntries()):
		a = branchParticle.At(i)
		if a.PID == 11:
			e.SetPxPyPzE(a.Px, a.Py, a.Pz, a.E)

		if a.PID == -12:
			v.SetPxPyPzE(a.Px, a.Py, a.Pz, a.E)

			histLorentz.Fill(np.sqrt(2*(e.Et())*(v.Et())*(1.0-np.cos(abs((e.Phi())-(v.Phi()))))))

			histCosine.Fill(np.sqrt(2*((e.Et())*(v.Et())-((e.Px())*(v.Px())+(e.Py())*(v.Py())))))




outputFile.Write()
outputFile.Close()

# -- EventLoop Ends
