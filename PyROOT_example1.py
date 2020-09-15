import sys
import ROOT

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
outputFile = ROOT.TFile.Open("output_file_name.root","recreate") ### <- Set Your output file name

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
histPT = ROOT.TH1F("pt", "P_{T} distribution",100, 0, 400.0)


## EventLoop start
for entry in range(0, numberOfEntries):
	# Load selected branches with data from specified event
	treeReader.ReadEntry(entry)

	# If event contains at least 1 particle
	if branchParticle.GetEntries() == 0:
		continue
	
	for i in range(0, branchParticle.GetEntries()):

		a = branchParticle.At(i)
		if abs(a.PID) in [11,12,13,14,15,16]:
			histPT.Fill(a.PT)




outputFile.Write()
outputFile.Close()

# -- EventLoop Ends
