from WriteHop import WriteHop


board = WriteHop(  # initialize board
    dx=600,  # DX
    dy=400,  # DY
    dz=19,   # DZ
    rot=0    # Part rotation
)
board.milling.add_tool(12)  # Add milling tool number 12
board.milling.start_point(x='dx/2', y='dy/2', z='-2')  # Starting point
board.milling.g_one(x='dx', y='dy', z=0)  # G01 linear
board.milling.end_point()  # Milling end point

board.write_to_file(file_name='milling_example.hop',  # File name + extension
                    wzgv='7405_1443',  # Machine name
                    comment='Milling Example')  # Comment
