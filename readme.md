## TTbar analysis repository  


1. Change lhe to root file  
 
```bash
./LHEFConverter [input.lhe] [output.root]
```  
  
  

2. Gen-Level analysis  

```bash
python [code.py] [input.root]
``` 

 2.1. Lepton Transverse momentum
  - [PyROOT_example1.py](https://github.com/groupKNUPHY/TTBar/blob/master/PyROOT_example1.py)

 2.2. W Transverse mass
  - using PyROOT [PyROOT_TVmass.py](https://github.com/groupKNUPHY/TTBar/blob/master/PyROOT_TVmass.py)
  - using uproot [uproot_wmass.py](https://github.com/groupKNUPHY/TTBar/blob/master/uproot_wmass.py)
 2.3. t Transverse mass
  - [PyROOT_ttbarreconstruction.py](https://github.com/groupKNUPHY/TTBar/blob/master/PyROOT_ttbarreconstruction.py)
  

3. Detector level analysis

```bash
python [code.py] [input.root]
```

 3.1 b jet
  - [PyROOT_bjet.py](https://github.com/groupKNUPHY/TTBar/blob/master/PyROOT_bjet.py)

4. Draw histogram 

```bash
python [code.py]
``` 

 - [makehist_simple.py](https://github.com/groupKNUPHY/TTBar/blob/master/makehist_simple.py)
