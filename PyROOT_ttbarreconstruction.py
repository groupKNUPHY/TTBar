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
outputFile = ROOT.TFile.Open("sibar_mad.root","recreate") ### <- Set Your output file name

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
histLorentz = ROOT.TH1F("Lorentz", "t Transverse mass1",150, 0, 300.0)
# histCosine  = ROOT.TH1F("Cosine", "W Transverse mass2",200, 0, 200.0)

## Define electron and neutrino
e = ROOT.TLorentzVector()
v = ROOT.TLorentzVector()

## Define W and b,  w = e + v
w = ROOT.TLorentzVector()
b = ROOT.TLorentzVector()

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

		if a.PID == -5:
			b.SetPxPyPzE(a.Px, a.Py, a.Pz, a.E)



	w = e + v
	histLorentz.Fill(np.sqrt(np.square(e.Et()+v.Et()+b.Et())-np.square(e.Px()+v.Px()+b.Px())-np.square(e.Py()+v.Py()+b.Py())))
	# histCosine.Fill(np.sqrt(2*(e.Et())*(v.Et())*(1.0-np.cos(abs((e.Phi())-(v.Phi())))))) <- if your events have any heavy quark, use this formula.


outputFile.Write()
outputFile.Close()

# -- EventLoop Ends
