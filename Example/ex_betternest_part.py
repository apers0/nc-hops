from WriteHop import WriteHop


hop = WriteHop(
    dx=600,
    dy=400,
    dz=18,
    rot=0
)

"""
Look at the docstring on init_nest_part() inside WriteHop/Nesting.py
There's many fields to operate with - including custom VARS
To enter a custom variable call on hop
for example here - hop.vars['a_custom_var'] = 'A custom VAR'
"""
hop.nesting.init_nest_part(
    art_no=1,
    info='Part_name',
    material='Some material',
    order_text1='Some order text',
    free_text1='Some free text',
    edge_mat_back='Back edge',
    edge_mat_front='Front edge',
    edge_mat_left='Left edge',
    edge_mat_right='Right edge',
)


# Do something with the nestpart
hop.drilling.call_501()  # Call drilling tool

# Perform a vertical drill
hop.drilling.vertical(
    x=10, y='dy/2',
    diameter=8,
    depth=-13,
    cycle=10
)

hop.milling.add_tool(50)  # Call milling tool

# Perform a milling pocket
hop.milling.rectangle_pocket(
    x_center='dx/2',
    y_center='dy/2',
    pocket_length=300,
    pocket_height=100,
    depth=-3
)

# Get standard router ID
hop.milling.get_standard_router_id()

# Klein format macro for formatting
# This will be done with the standard router which has been called with the line above
# When the piece is a "small piece"
# The part will be milled two times - with the first cutting depth being DZ-1.5
# And the final depth of the formatting being DZ+0.2
# Try to keep this macro at the end of the file to avoid any tool conflicts
hop.nesting.klein_format(
    first_depth=1.5,
    milling_steps=2,
    final_depth=0.2
)

# Save the .hop file
hop.write_to_file(
    file_name='a_nestpart.hop',
    wzgv='YOUR_MACHINE_NAME',
    comment='A comment'
)
