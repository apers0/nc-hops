from ReadHop import ExtractHopProcessing
import os


file = os.path.join(os.path.dirname(__file__), 'test', 'panel_5.hop')

hop = ExtractHopProcessing(file)

# Hop Comments
comments = hop.get_comments()

# Print comment that contains exe version
print(comments['EXEVERSION'])

# Hop VARS
vars = hop.get_vars()
dx = vars['DX']
dy = vars['DY']
dz = vars['DZ']

# Print length, width and thickness
print(f'DX: {dx}, DY: {dy}, DZ: {dz}')

# Get all BOHRUNG-HORZB from the file
drills = hop.all_drillings()
vertical_drills = drills['vertical']
horizontal_drills = drills['horizontal']

for vertical in vertical_drills: 
    print(vertical)

for horzb in horizontal_drills: 
    print(horzb)

