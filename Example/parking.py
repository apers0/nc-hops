from WriteHop.WriteHop import WriteHop


"""
A script demonstrating how to call on the standard parking
The standard parking is part of the 3dg scripts in hop
"""
hop = WriteHop(600, 400, 18)
hop.machine.standard_park_mode()
hop.write_to_file(file_name='park_standard.hop', wzgv='7507D_196')
