# Apigee
Environment Specific Properties For Apigee Proxies Runs on Python 3
  
  ## 1. To Generate Configuration from Proxy

**python ApigeeConfigProxy.py -p ProxyZipFileName.zip**

**Will generate several such properties** 


```
{'PropFile': 'apiproxy\\policies\\GenerateToken.xml', 'PropPath': 'DisplayName[1]', 'PropKey': 'GenerateToken'}
{'PropFile': 'apiproxy\\policies\\GenerateToken.xml', 'PropPath': 'Operation[1]', 'PropKey': 'GenerateAccessToken'}
{'PropFile': 'apiproxy\\policies\\GenerateToken.xml', 'PropPath': 'ExpiresIn[1]', 'PropKey': '3600'}
{'PropFile': 'apiproxy\\policies\\GenerateToken.xml', 'PropPath': 'SupportedGrantTypes[1]GrantType[1]', 'PropKey': 'client_credentials'}
{'PropFile': 'apiproxy\\policies\\OauthSpikeArrest.xml', 'PropPath': 'Rate[1]', 'PropKey': '30ps'}
{'PropFile': 'apiproxy\\proxies\\default.xml', 'PropPath': 'PreFlow[1]', 'PropKey': "{'name': 'PreFlow'}", 'XMLAttribute': True}
{'PropFile': 'apiproxy\\proxies\\default.xml', 'PropPath': 'PreFlow[1]Request[1]Step[1]Name[1]', 'PropKey': 'OauthSpikeArrest'}
{'PropFile': 'apiproxy\\proxies\\default.xml', 'PropPath': 'HTTPProxyConnection[1]BasePath[1]', 'PropKey': '/OAuth'}
```

we can filter out the property we are looking to override using the | grep -r | findstr command  for example

```
python ApigeeConfigProxy.py -p ProxyZipFileName.zip | findstr /I OauthSpikeArrest
python ApigeeConfigProxy.py -p ProxyZipFileName.zip | grep -i  OauthSpikeArrest
```



```
{'PropFile': 'apiproxy\\policies\\OauthSpikeArrest.xml', 'PropPath': 'Rate[1]', 'PropKey': '30ps'}
```



we can redirect several such configurations to a Proxy configuration file and modify the PropKey values which might look like 

```
{'PropFile': 'apiproxy\\policies\\OauthSpikeArrest.xml', 'PropPath': 'Rate[1]', 'PropKey': '90ps'}
{'PropFile': 'apiproxy\\policies\\GenerateToken.xml', 'PropPath': 'ExpiresIn[1]', 'PropKey': '360000 '}
{'PropFile': 'apiproxy\\policies\\OauthSpikeArrest.xml', 'PropPath': 'Identifier[1]', 'PropKey': "{'ref': 'request.header.some-OtherHeader-name'}", 'XMLAttribute': True}
```

**Lets Name this file GenerateOauth_rev2_2020_04_17.PRDCFG**

## 2. Applying Generated Configuration

```python ApigeeConfigProxy.py -p GenerateOauth_rev2_2020_04_17.zip -c GenerateOauth_rev2_2020_04_17.PRDCFG```

```
Applying Configuration In Folder GenerateOauth_rev2_2020_04_17
CFG => apiproxy\policies\OauthSpikeArrest.xml Rate[1] From | 30ps | To | 90ps |
CFG => apiproxy\policies\GenerateToken.xml ExpiresIn[1] From | 3600 | To | 360000 |
CFG => apiproxy\policies\OauthSpikeArrest.xml Identifier[1] From | request.header.some-header-name | To | request.header.some-OtherHeader-name |
```

**Old Proxy will be Timestamped and Renamed to be found in the same folder. Proxy with updated configuration will be found in the same folder with sname name.**


# What Did we achieve...
  ## We have updated the proxy configuration without any GUI support, if im an admin who needs to reconfigure same value to 100's of proxies this utility might come in handy, provided the policy name is standardised across all proxies. Im sure you can think of other uses for it.
 
 
 Known Bugs and points to note.
 ```
 XML Comments will vanish because xml.etree does not support them
 XML declaration Not supported... did a patch for it.. 
 If a Configuraion is not found in the current Proxy Warning is printed and code moves on. (can be reconfigured by commenting the if condition which prints this line)
 Exceptions are not handeled temporary work folder remains undeleted in case of exceptions to allow us to debug the issue.
 ```
 
