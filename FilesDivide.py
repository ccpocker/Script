import argparse
parser=argparse.ArgumentParser(description="Dividefiles")
parser.add_argument("-i","--inputdir",type=str,default=None)
parser.add_argument("-c","--comparedir",type=str,default=None)
parser.add_argument("-o","--outputdir",type=str,default=None)
parser.add_argument("-s","--sourcedir",type=str,default=None)
parser.add_argument("-d","--deletestr",type=int,default=-4)
args=parser.parse_args()

import os 
import sys
from shutil import copyfile
input_files=[]
compare_files=[]
for root,dirs,input_file in os.walk(args.inputdir):
    input_files.append(input_file)
for root,dirs,compare_file in os.walk(args.comparedir):
    compare_files.append(compare_file)

print("The number of inputfiles= ",len(input_files[0]))
print("The number of comparefiles= ",len(compare_files[0]))
x=0 #notfound filese
for i in input_files[0]:
    if args.deletestr==0:
        inputx=i
    else:inputx=i[:args.deletestr]
    if str(inputx) in compare_files[0]:
        compare_files[0].remove(inputx)
    else:
        x=x+1
        print("File %s is not found " %(inputx))
print("There is %d files not found" %(x))
print("After Comparing, the numbers of non-contain files= ",len(compare_files[0]))
root_dir=''
if args.outputdir==None:
    root_dir=os.getcwd()
    os.mkdir(os.path.join(root_dir,'contain'))
    os.mkdir(os.path.join(root_dir,'not_contain'))
else:
    root_dir=args.outputdir
    os.mkdir(os.path.join(args.outputdir,'contain'))
    os.mkdir(os.path.join(args.outputdir,'not_contain'))

for i in input_files[0]:
    source_path=os.path.join(args.sourcedir,i)
    out_path=os.path.join(root_dir,'contain',i)
    copyfile(source_path,out_path)
for i in compare_files[0]:
    source_path=os.path.join(args.sourcedir,i)
    out_path=os.path.join(root_dir,'not_contain',i)
    copyfile(source_path,out_path)
