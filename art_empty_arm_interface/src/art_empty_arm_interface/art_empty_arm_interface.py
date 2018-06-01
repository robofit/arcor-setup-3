from art_brain import ArtBrainRobotInterface, ArtGripper


class ArtEmptyArmInterface(ArtBrainRobotInterface):

    EMPTY_ARM = "empty"

    def __init__(self, robot_helper):
        super(ArtEmptyArmInterface, self).__init__(robot_helper)


    def select_arm_for_pick(self, obj_id, objects_frame_id, tf_listener):
        return self.EMPTY_ARM

    def select_arm_for_pick_from_feeder(self, pick_pose, tf_listener):
        return self.EMPTY_ARM

    def select_arm_for_drill(self, obj_to_drill, tf_listener):
        return self.EMPTY_ARM

    def prepare_for_calibration(self):
        pass

    def emergency_stop(self):
        pass

    def restore_robot(self):
        pass

