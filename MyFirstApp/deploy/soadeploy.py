print '*** Script invocation : Starting ***'

readSOAProperties = FileInputStream("soadeploy.properties")
configProps = Properties()
configProps.load(readSOAProperties)
    
soa_server = configProps.get("soa.soa_server")
jar_location = configProps.get("soa.jar_location")
xml_location = configProps.get("soa.xml_location")
username = configProps.get("soa.username")
password = configProps.get("soa.password")

# list of composites, JARs in left column, XMLs in right column
composites = [
['sca_ABC_rev25.jar',    'ABC_cfgplan.xml'],
['sca_XYZ_rev26.jar',    'XYZ_cfgplan.xml'],
['sca_MNO_rev27.jar',    'MNO_cfgplan.xml']
]

    
for composite in composites:
    print '----------------------------------------------------------------------------------------------------'
    print 'Starting  to deploy: ' + composite[0]
    
    try:
        if composite[1] is None:
            # No config file
            configpath = None
        else:
            # Config file exists
            configpath = xml_location + composite[1]

        sca_deployComposite(soa_server,jar_location + composite[0],true,username,password,true,configpath)

    except:
        print 'Failed to deploy: ' + composite[0]
        pass
    
    print '----------------------------------------------------------------------------------------------------'
        
print 'All composites deployed successfully'
exit()

print '*** Script Invocation : STOPPED ***'


