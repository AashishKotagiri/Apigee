import os
import xml.etree.ElementTree as ET
from glob import glob
from zipfile import ZipFile
import argparse
import ntpath
import CreateProperties,ApplyProperties
import shutil


def parseAttributes(xmlTag):
    return str(dict(xmlTag.items()))


def fprint(xmlpath, xmlvalue, filepath, xmlattribute=False):
    Dict = {}
    Dict['PropFile'] = filepath
    Dict['PropPath'] = xmlpath
    Dict['PropKey'] = xmlvalue
    if xmlattribute:
        Dict['XMLAttribute'] = True
    print(Dict)




parser = argparse.ArgumentParser()
AbsProxyPath = None
ConfigurationFile = None
parser.add_argument("-p", "--Path", dest="AbsProxyPath",    help="Absolute Proxy Path")
parser.add_argument("-c", "--Config", dest="ConfigurationFile",    help="Absolute Path To Configuration File")
args = parser.parse_args()

if args.AbsProxyPath is None and args.ConfigurationFile is None:
    print("============================================================"
          "\n Mandatory Parameters missing"
          "\n To Generate Configuration ACP -p Proxy.zip"
          "\n To Save Configuration Redirect the Output to a file"
          "\n To Apply a configuration ACP -p Proxy.zip -c ConfigFile"
          "\n============================================================"
          )
elif args.AbsProxyPath is not None and args.ConfigurationFile is not None:
    AbsProxyPath = args.AbsProxyPath
    #print(os.path.dirname(AbsProxyPath))  ## directory of file
    WorkDirectory = os.path.dirname(AbsProxyPath)
    TempFolderNameSuffix = ntpath.basename(AbsProxyPath).split(".", 1)[0]
    WorkDirectory = os.path.join(WorkDirectory, TempFolderNameSuffix)
    os.makedirs(WorkDirectory)
    with ZipFile(AbsProxyPath, 'r') as zipObj:
        zipObj.extractall(WorkDirectory)
    result = [y for x in os.walk(WorkDirectory) for y in glob(os.path.join(x[0], '*'))]
    ApplyProperties.ApplyProperties(result,args.ConfigurationFile,WorkDirectory , TempFolderNameSuffix , AbsProxyPath)
    shutil.rmtree(WorkDirectory)

elif args.AbsProxyPath is not None:
    AbsProxyPath = args.AbsProxyPath
    print(os.path.dirname(AbsProxyPath)) ## directory of file
    WorkDirectory = os.path.dirname(AbsProxyPath)
    TempFolderNameSuffix = ntpath.basename(AbsProxyPath).split(".", 1)[0]
    WorkDirectory = os.path.join(WorkDirectory , TempFolderNameSuffix)
    os.makedirs(WorkDirectory)
    with ZipFile(AbsProxyPath, 'r') as zipObj:
        zipObj.extractall(WorkDirectory)
    result = [y for x in os.walk(WorkDirectory) for y in glob(os.path.join(x[0], '*'))]
    CreateProperties.ExtractProxyProperties(result)
    shutil.rmtree(WorkDirectory)
