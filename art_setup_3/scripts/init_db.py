#!/usr/bin/env python

import sys
import rospy
from art_msgs.msg import Program, ProgramBlock, ProgramItem
from copy import deepcopy
from art_utils import ArtApiHelper
from art_utils.art_msgs_functions import obj_type, wait_item, feeder_item, grid_item, drill_item, place_item,\
    item, polygon_item


def main():

    rospy.init_node('simple_trolley_init_script', anonymous=True)

    art = ArtApiHelper()
    art.wait_for_api()

    # delete all created programs
    ph = art.get_program_headers()
    if ph:
        for h in ph:

            art.program_clear_ro(h.id)
            art.delete_program(h.id)

    prog = Program()
    prog.header.id = 1
    prog.header.name = "Pick & Place"

    pb = ProgramBlock()
    pb.id = 1
    pb.name = "Pick & Place"
    pb.on_success = 1
    pb.on_failure = 0
    prog.blocks.append(pb)

    pb.items.append(polygon_item(1))
    pb.items.append(place_item(2, ref_id=[1], on_success=3, on_failure=0))
    pb.items.append(item(3, "GetReady", on_success=4, on_failure=0))
    pb.items.append(polygon_item(4))
    pb.items.append(place_item(5, ref_id=[4], on_success=6, on_failure=0))
    pb.items.append(item(6, "GetReady", on_success=1, on_failure=0))
    
    art.store_program(prog)
    art.program_set_ro(prog.header.id)

if __name__ == '__main__':
    main()

