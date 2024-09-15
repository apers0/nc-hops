from WriteHop import WriteHop

board = WriteHop(  # initialize board
    dx=600,  # DX
    dy=400,  # DY
    dz=19,   # DZ
    rot=0    # Part rotation
)

"""
Calling drilling tools is different than calling Milling tools or Sawing tools
The same goes for milling or sawing tools 
WZB- Drilling tool
WZF- Milling tool
WZS- Sawing tool
Calling the 501 drill head looks like this:
WZB (501,_VE,_V,_VA,_SD,_ANF,'51')
for that we can use: board.drilling.call_501(), OR board.drilling.add_tool(501)
board.add_tool() method exists to call a drilling aggregate with a specific tool no.
for example-if there's a cabineo drilling aggregate whose number is 1002, we'd type board.drilling.add_tool(1002)
"""

board.drilling.call_501()


board.drilling.vertical(x=34,
                        y=200,
                        diameter=15,
                        depth=-13.4,
                        cycle=30)  # 10=dowels, 20=through holes, 30=camlocks, hinges etc.

board.drilling.horizontal(x=0,
                          y=200,
                          z=-9.5,
                          diameter=8,
                          depth=34,
                          rotation_angle=0  # 0-left, 90-bottom, 180-right, 270-up
                          )

board.write_to_file(file_name='basic_drilling_example.hop',  # File name + extension
                    wzgv='7405_1443',  # Machine name
                    comment='Drilling Example')  # Comment
