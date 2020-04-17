import os
import ast
import shutil
import xml.etree.ElementTree as ET
from glob import glob
from zipfile import ZipFile

def ApplyProperties(result , propertyfileref , WorkDirectory , TempFolderNameSuffix , AbsProxyPath):
    print("Applying Configuration In Folder " + WorkDirectory)
    for Configuration in open(propertyfileref):
        ConfigLine = ast.literal_eval(Configuration)
        for xmlfile in result:
            if ConfigLine.get('PropFile') in xmlfile :
                FileXMLDecleration = open(xmlfile).readline().rstrip()
                # XML Declaration not supported by etree module

                if ConfigLine.get('XMLAttribute') :
                    AttributesDict = ast.literal_eval(ConfigLine.get('PropKey'))
                    for Attribute in AttributesDict.keys():
                        xmlTree = ET.parse(xmlfile)
                        currentattrconfig = xmlTree.find(ConfigLine.get('PropPath')).attrib[Attribute]
                        print("CFG => " + ConfigLine.get('PropFile') + " " + ConfigLine.get(
                            'PropPath') + " From | " + currentattrconfig + " | To | " + AttributesDict.get(Attribute) + " |")
                        xmlTree.find(ConfigLine.get('PropPath')).attrib[Attribute] = AttributesDict.get(Attribute)
                        xmlTree.write(xmlfile)
                    with open(xmlfile, 'r+') as f:
                        content = f.read()
                        f.seek(0, 0)
                        f.write(FileXMLDecleration.rstrip('\r\n') + '\n' + content)
                        f.close()

                else:
                    xmlTree = ET.parse(xmlfile)
                    CurrentConfig = None
                    if xmlTree.find(ConfigLine.get('PropPath')) is not None:
                        CurrentConfig = xmlTree.find(ConfigLine.get('PropPath')).text
                    UpdatedConfig = ConfigLine.get('PropKey')
                    if CurrentConfig is None:
                        print("SKIP => " + ConfigLine.get('PropFile') +" " + ConfigLine.get('PropPath') +" " + UpdatedConfig + " Unavailable Configuration in Current Proxy. ")
                    else:
                        print("CFG => " + ConfigLine.get('PropFile') +" " + ConfigLine.get('PropPath') + " From | " + CurrentConfig +" | To | "+ UpdatedConfig + " |")
                        xmlTree.find(ConfigLine.get('PropPath')).text = UpdatedConfig
                        xmlTree.write(xmlfile)
                        with open(xmlfile, 'r+') as f:
                            content = f.read()
                            f.seek(0, 0)
                            f.write(FileXMLDecleration.rstrip('\r\n') + '\n' + content)
                            f.close()


    zip_name = os.path.join( os.path.dirname(WorkDirectory),TempFolderNameSuffix+"Generated.zip")
    directory_name = WorkDirectory
    #print(zip_name)
    #print(directory_name)
    # Create 'path\to\zip_file.zip'
    from datetime import datetime

    os.rename(AbsProxyPath, AbsProxyPath +"BKP"+ datetime.utcnow().strftime('%Y%m%d%H%M%S%f'))
    shutil.make_archive(WorkDirectory, 'zip', directory_name)


