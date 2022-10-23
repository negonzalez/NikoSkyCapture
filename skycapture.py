#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  skycapture.py
#  
#  Copyright 2022 Nicolas Gonzalez <negonzalezm@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import argparse
import locale
import logging
import sys

import gphoto2 as gp


def main(args):
    
    parser = argparse.ArgumentParser()                                  #Parse command option
    parser.add_argument('-v', '--verbosity_level', 
                         choices = [0, 1, 2, 3, 4],
                         type = int, 
                         help = 'Increase output verbosity. Default INFO.',
                         default = 1)
    parser.add_argument('-n', '--number_light', 
                         type = int, 
                         help = 'Number of light frames. Default 10 exposures.',
                         default = 10)
    parser.add_argument('-t', '--time_exposures', 
                        type = int, 
                        help = 'Time of exposure in seconds. Default 60 seconds.',
                        default = 60)
    parser.add_argument('-l', '--time_lapse', 
                        type = int, 
                        help = 'Time between exposure in seconds. Default 5 seconds.',
                        default = 5)
    parser.add_argument('-s', '--number_sequence', 
                        type = int, 
                        help = 'Number of light exposure sequences. Default 1 sequence',
                        default = 1)
    parser.add_argument('-k', '--number_dark', 
                        type = int, 
                        help = 'Number of dark frames. Default 10 exposures.',
                        default = 10)
    parser.add_argument('-b', '--number_bias', 
                        type = int, 
                        help = 'Number of bias frames. Default 10 exposures.',
                        default = 10)
    parser.add_argument('-d', '--skip_dark', 
                        help = 'Skip dark frame capture',
                        action = 'store_true')
    parser.add_argument('-a', '--skip_bias', 
                         help = 'Skip bias capture',
                         action = 'store_true')
    parser.add_argument('-f', '--flat', 
                        help = '''The capture is for flat field.
                                  With this option dark frame and bias frames 
                                  captures are disable''',
                        action = 'store_true')
    parser.add_argument('-i', '--iso',
                        type = int,
                        help = 'ISO sensibility. Default 5000 ISO.',
                        default = 5000)
    args = vars(parser.parse_args())                                    #Get options like a dict
    
    print(args)
    
    log_level = [logging.DEBUG,                                         #Log level list
                 logging.INFO, 
                 logging.WARNING, 
                 logging.ERROR, 
                 logging.CRITICAL]
    
    logger = logging.getLogger('sky_capture')                           #Setup logger
    logger.setLevel(log_level[args['verbosity_level']])
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    sh = logging.StreamHandler()                                        #Output in stdout
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    
    logger.info('Sky Capture V0.0')

    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
