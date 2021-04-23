#!/usr/bin/env python

# Copyright (c) 2019, Robot Control and Pattern Recognition Group,
# Institute of Control and Computation Engineering
# Warsaw University of Technology
#
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Warsaw University of Technology nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYright HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Author: Dawid Seredynski
#

import os
import sys
from distutils.dir_util import copy_tree
import rospkg

def printUsage():
    print('Usage:')
    print('prepare_velma_msgs_for_matlab.py <dst_path>')

def main():
    if len(sys.argv) != 2:
        printUsage()
        return 1

    dst_path = sys.argv[1]
    if not os.path.isdir(dst_path):
        print('The path "{}" is not an existing directory'.format( dst_path ))
        return 2

    package_name_list = [
        'velma_core_cs_task_cs_msgs',
        'velma_core_cs_ve_body_msgs',
        'velma_core_ve_re_lwr_msgs',
        'simulation_control_msgs',
        'barrett_hand_msgs',
        'barrett_hand_status_msgs',
        'cartesian_trajectory_msgs',
        'lwr_msgs',
        ]

    rospack = rospkg.RosPack()

    #print dir(rospack)
    #print rospack.get_manifest('velma_ec_gen_msgs')
    #print dir(rospack.get_manifest('velma_ec_gen_msgs'))
    for package_name in package_name_list:
        path = rospack.get_path( package_name )
        copy_tree(path, '{}/{}'.format(dst_path, package_name))

    print('Done. Run MATLAB and execute:')
    print('rosgenmsg( \'{}\' )'.format(dst_path) )
    return 0

if __name__ == "__main__":
    exit( main() )
