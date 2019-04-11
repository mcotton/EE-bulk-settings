
"""
Goes through cameras on the list of bridges
Set the cloud_retention_days to 60
Requires Python 3
Contact mcotton@een.com with questions
"""


from  EagleEye import *

een = EagleEye()


# Credentials to Eagle Eye account that can see the devices and has permission to change camera settings
USERNAME = ''
PASSWORD = ''



een.login(username=USERNAME, password=PASSWORD)

# array of bridge ESNs
site_bridges = ['']

# find cameras that are seen by these bridges, only looks at first bridge, but a good first pass
site_cameras = [i for i in een.cameras if i.bridges and i.bridges[0][0] in site_bridges]

# find cameras that are attached to these bridges
attd_cameras = [i for i in een.cameras if i.bridges and i.bridges[0][0] in site_bridges and i.bridges[0][1] == 'ATTD']

print( f"Site Bridges: {len(site_bridges)}" )
print( f"Site Cameras: {len(site_cameras)}" )
print( f"Attd Cameras: {len(attd_cameras)}" )

for cam in site_cameras:
    print( f"Changing settings for {cam} on {cam.bridges[0][0]}")
    cam.update_device_details(een, {"id": cam.camera_id, "camera_settings_add": json.dumps({ "settings": { "cloud_retention_days": 60 } } )  } ) 

