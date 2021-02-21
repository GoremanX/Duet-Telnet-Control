#!python3
"""
Telnet listener written in python to run commands on a linux system based on M118 gcodes issued on Duet3D motion control boards
# Copyright (C) 2021 Frank Gore all rights reserved.
# Released under The GPL V3 License https://www.gnu.org/licenses/gpl-3.0.en.html
#
#
# Developed on Raspberry pi
"""
global dtcVersion
dtcVersion = '0.0.1'
import argparse
import os
import sys
import threading
import subprocess
import shlex
import psutil
import socket
import time
import platform
import telnetlib
import pexpect

