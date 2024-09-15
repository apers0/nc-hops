from WriteHop import WriteHop


board = WriteHop(
    dx=600,
    dy=400,
    dz=19,
    rot=0
)

board.milling.add_tool(12)  # Add milling tool
board.milling.rectangle_pocket(  # Rectangle pocket macro
    x_center='dx/2',
    y_center='dy/2',
    pocket_length=300,
    pocket_height=200,
    radius=0,
    depth=13
)
board.write_to_file(file_name='milling_macro_example.hop',
                    wzgv='7405_1443',
                    comment='Milling Macro Example')
