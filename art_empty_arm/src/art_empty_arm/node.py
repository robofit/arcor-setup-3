#!/usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerResponse


class ArtEmptyArm(object):

    def __init__(self):
        self.get_ready_srv = rospy.Service("arm/get_ready", Trigger, self.get_ready_cb)

    def get_ready_cb(self, req):
        resp = TriggerResponse()
        resp.success = True
        return resp


if __name__ == '__main__':
    rospy.init_node('art_empty_arm', log_level=rospy.INFO)

    try:
        node = ArtEmptyArm()
        rospy.spin()

    except rospy.ROSInterruptException:

        node = None