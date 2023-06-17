from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': "Opentrons_4CR",
    'author': 'Kevin <kevinchang.wang@mail.utoronto.ca',
    'description': 'Opentrons liquid dispensing protocol for 4CR',
    'apiLevel': '2.12'
}

# This protocol will use the Opentrons OT-2 robot to combine the 3 components for the 3 component reaction
# Version: Multi-channel pipette

# Set the component volume here
component_volume = 40

# Change the location of the plates here
source_plate_location = '10'
destination_plate_1_location = '11'
destination_plate_2_location = '1'

# This protocol requires 3 pipette racks, 1 for each component. Indicate the locations here
tip_rack_1_location = '7'
tip_rack_2_location = '8'
tip_rack_3_location = '9'
