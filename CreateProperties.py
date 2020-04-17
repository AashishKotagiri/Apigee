import xml.etree.ElementTree as ET


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


def ExtractProxyProperties(result):
    for xmlfile in result:
        if '.xml' in xmlfile:

            ApigeeArtifactName = xmlfile.split('apiproxy')[1]
            ApigeeArtifactName = 'apiproxy' + ApigeeArtifactName
            #print(ApigeeArtifactName)


            xmlTree = ET.parse(xmlfile)
            XMLRoot = xmlTree.getroot()
            L1index = 1
            L1XMLXpath = ""
            L1OldTag = ""
            L1OldIndex = 1
            for L1 in XMLRoot:
                if L1.tag == L1OldTag:
                    L1index = L1index + 1
                else:
                    L1index = 1
                L1XMLXpath = L1XMLXpath.replace(L1OldTag+"["+str(L1OldIndex)+"]","",1)
                L1XMLXpath = L1XMLXpath + L1.tag + "["+str(L1index)+"]"
                if hasattr(L1 , 'text') and L1.text is not None and len(L1.text.strip()) > 0:
                    fprint(L1XMLXpath,L1.text,ApigeeArtifactName)
                if len(L1.keys()) > 0:
                    fprint(L1XMLXpath , parseAttributes(L1) , ApigeeArtifactName , True)
                L1OldTag = L1.tag
                L1OldIndex = L1index
                L2index = 1
                L2XMLXpath=""
                L2OldTag=""
                L2OldIndex=""
                for L2 in L1:
                    if L2.tag == L2OldTag:
                        L2index = L2index + 1
                    else:
                        L2index = 1
                    L2XMLXpath = L2XMLXpath.replace(L2OldTag + "[" + str(L2OldIndex) + "]", "", 1)
                    L2XMLXpath = L2XMLXpath + L2.tag + "[" + str(L2index) + "]"
                    if hasattr(L2, 'text') and L2.text is not None and len(L2.text.strip()) > 0:
                        fprint(L1XMLXpath+L2XMLXpath, L2.text, ApigeeArtifactName)
                    if len(L2.keys()) > 0:
                        fprint(L1XMLXpath +L2XMLXpath,  parseAttributes(L2), ApigeeArtifactName, True)
                    L2OldTag = L2.tag;
                    L2OldIndex = L2index
                    L3index = 1
                    L3XMLXpath = ""
                    L3OldTag = ""
                    L3OldIndex = ""
                    L3index = 1
                    for L3 in L2:
                        if L3.tag == L3OldTag:
                            L3index = L3index + 1
                        else:
                            L3index = 1
                        L3XMLXpath = L3XMLXpath.replace(L3OldTag + "[" + str(L3OldIndex) + "]", "", 1)
                        L3XMLXpath = L3XMLXpath + L3.tag + "[" + str(L3index) + "]"
                        if hasattr(L3, 'text') and L3.text is not None and len(L3.text.strip()) > 0:
                            fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath,  L3.text, ApigeeArtifactName)
                        if len(L3.keys()) > 0:
                            fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath, parseAttributes(L3), ApigeeArtifactName , True)
                        L3OldTag = L3.tag;
                        L3OldIndex = L3index
                        L4index = 1
                        L4XMLXpath = ""
                        L4OldTag = ""
                        L4OldIndex = ""
                        L4index = 1
                        for L4 in L3:
                            if L4.tag == L4OldTag:
                                L4index = L4index + 1
                            else:
                                L4index = 1
                            L4XMLXpath = L4XMLXpath.replace(L4OldTag + "[" + str(L4OldIndex) + "]", "", 1)
                            L4XMLXpath = L4XMLXpath + L4.tag + "[" + str(L4index) + "]"
                            if hasattr(L4, 'text') and L4.text is not None and len(L4.text.strip()) > 0 :
                                fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath , L4.text , ApigeeArtifactName)
                            if len(L4.keys()) > 0:
                                fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath  , parseAttributes(L4) , ApigeeArtifactName , True)
                            L4OldTag = L4.tag;
                            L4OldIndex = L4index
                            L5index = 1
                            L5XMLXpath = ""
                            L5OldTag = ""
                            L5OldIndex = ""
                            L5index = 1
                            for L5 in L4:
                                if L5.tag == L5OldTag:
                                    L5index = L5index + 1
                                else:
                                    L5index = 1
                                L5XMLXpath = L5XMLXpath.replace(L5OldTag + "[" + str(L5OldIndex) + "]", "", 1)
                                L5XMLXpath = L5XMLXpath + L5.tag + "[" + str(L5index) + "]"
                                if hasattr(L5, 'text') and L5.text is not None and len(L5.text.strip()) > 0 :
                                    fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath , L5.text, ApigeeArtifactName)
                                if len(L5.keys()) > 0:
                                    fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath , parseAttributes(L5), ApigeeArtifactName, True)
                                L5OldTag = L5.tag;
                                L5OldIndex = L5index
                                L6index = 1
                                L6XMLXpath = ""
                                L6OldTag = ""
                                L6OldIndex = ""
                                L6index = 1
                                for L6 in L5:
                                    if L6.tag == L6OldTag:
                                        L6index = L6index + 1
                                    else:
                                        L6index = 1
                                    L6XMLXpath = L6XMLXpath.replace(L6OldTag + "[" + str(L6OldIndex) + "]", "", 1)
                                    L6XMLXpath = L6XMLXpath + L6.tag + "[" + str(L6index) + "]"
                                    if hasattr(L6, 'text') and L6.text is not None and len(L6.text.strip()) > 0:
                                        fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath + L6XMLXpath , L6.text , ApigeeArtifactName)
                                    if len(L6.keys()) > 0:
                                        fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath + L6XMLXpath, parseAttributes(L6), ApigeeArtifactName, True)
                                    L6OldTag = L6.tag;
                                    L6OldIndex = L6index
                                    L7index = 1
                                    L7XMLXpath = ""
                                    L7OldTag = ""
                                    L7OldIndex = ""
                                    L7index = 1
                                    for L7 in L6:
                                        if L7.tag == L7OldTag:
                                            L7index = L7index + 1
                                        else:
                                            L7index = 1
                                        L7XMLXpath = L7XMLXpath.replace(L7OldTag + "[" + str(L7OldIndex) + "]", "", 1)
                                        L7XMLXpath = L7XMLXpath + L7.tag + "[" + str(L7index) + "]"
                                        if hasattr(L7, 'text') and L7.text is not None and len(L7.text.strip()) > 0:
                                            fprint(
                                                L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath + L6XMLXpath + L7XMLXpath ,  L7.text , ApigeeArtifactName)
                                        if len(L7.keys()) > 0:
                                            fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath + L6XMLXpath + L7XMLXpath , parseAttributes(L7) , ApigeeArtifactName , True)
                                        L7OldTag = L7.tag;
                                        L7OldIndex = L7index
                                        L8index = 1
                                        L8XMLXpath = ""
                                        L8OldTag = ""
                                        L8OldIndex = ""
                                        L8index = 1
                                        for L8 in L7:
                                            if L8.tag == L8OldTag:
                                                L8index = L8index + 1
                                            else:
                                                L8index = 1
                                            L8XMLXpath = L8XMLXpath.replace(L8OldTag + "[" + str(L8OldIndex) + "]", "", 1)
                                            L8XMLXpath = L8XMLXpath + L8.tag + "[" + str(L8index) + "]"
                                            if hasattr(L8, 'text') and L8.text is not None and len(L8.text.strip()) > 0:
                                                fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath + L6XMLXpath + L7XMLXpath + L8XMLXpath , L8.text , ApigeeArtifactName)
                                            if len(L8.keys()) > 0:
                                                fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath + L6XMLXpath + L7XMLXpath + L8XMLXpath , parseAttributes(L8) , ApigeeArtifactName , True)
                                            L8OldTag = L8.tag;
                                            L8OldIndex = L8index
                                            L9index = 1
                                            L9XMLXpath = ""
                                            L9OldTag = ""
                                            L9OldIndex = ""
                                            L9index = 1
                                            for L9 in L8:
                                                if L9.tag == L9OldTag:
                                                    L9index = L9index + 1
                                                else:
                                                    L9index = 1
                                                L9XMLXpath = L9XMLXpath.replace(L9OldTag + "[" + str(L9OldIndex) + "]", "", 1)
                                                L9XMLXpath = L9XMLXpath + L9.tag + "[" + str(L9index) + "]"
                                                if hasattr(L9, 'text') and L9.text is not None and len(L9.text.strip()) > 0:
                                                    fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath + L6XMLXpath + L7XMLXpath + L8XMLXpath + L9XMLXpath , L9.text , ApigeeArtifactName)
                                                if len(L9.keys()) > 0:
                                                    fprint(L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath + L6XMLXpath + L7XMLXpath + L8XMLXpath + L9XMLXpath , parseAttributes(L9) , ApigeeArtifactName , True)
                                                L9OldTag = L9.tag;
                                                L9OldIndex = L9index
                                                L10index = 1
                                                L10XMLXpath = ""
                                                L10OldTag = ""
                                                L10OldIndex = ""
                                                L10index = 1
                                                for L10 in L9:
                                                    if L10.tag == L10OldTag:
                                                        L10index = L10index + 1
                                                    else:
                                                        L10index = 1
                                                    L10XMLXpath = L10XMLXpath.replace(L10OldTag + "[" + str(L10OldIndex) + "]","", 1)
                                                    L10XMLXpath = L10XMLXpath + L10.tag + "[" + str(L10index) + "]"
                                                    if hasattr(L10, 'text') and L10.text is not None and len( L10.text.strip()) > 0:
                                                        fprint(
                                                            L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath + L6XMLXpath + L7XMLXpath + L8XMLXpath + L9XMLXpath + L10XMLXpath , L10.text , ApigeeArtifactName )
                                                    if len(L10.keys()) > 0:
                                                            fprint(
                                                                L1XMLXpath + L2XMLXpath + L3XMLXpath + L4XMLXpath + L5XMLXpath + L6XMLXpath + L7XMLXpath + L8XMLXpath + L9XMLXpath + L10XMLXpath , parseAttributes(
                                                                    L10) , ApigeeArtifactName , True)
                                                    L10OldTag = L10.tag;
                                                    L10OldIndex = L10index
                                                    L11index = 1
                                                    L11XMLXpath = ""
                                                    L11OldTag = ""
                                                    L11OldIndex = ""
                                                    L11index = 1