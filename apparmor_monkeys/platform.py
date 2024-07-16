from __future__ import absolute_import

import os
import platform
import sys


_uname = platform.uname


def uname():
    # platform.uname() is the same as os.uname(), but with extra data about the
    # processor. Unfortunately this needs to shell out and does something like
    # [sh, -c, "%s 2>%s"].
    # We avoid this - it saves us having to give our apparmor profile access to
    # run a full sh!!!
    # processor = "x86_64" if sys.maxsize > 2 ** 32 else 'i686'
    # return os.uname() + (processor, )
    #
    # Note: Python 3.9 changed the platform API to return the first 5 items (not processor).
    #       So, removing it from this interface for use on systems with python >= 3.9
    # Previous return:
    #    processor = os_uname.machine
    #    return platform.uname_result(system=os_uname.sysname,
    #                             node=os_uname.nodename,
    #                             release=os_uname.release,
    #                             version=os_uname.version,
    #                             machine=os_uname.machine,
    #                             processor=processor)
    
    os_uname = os.uname()
    return platform.uname_result(system=os_uname.sysname,
                                 node=os_uname.nodename,
                                 release=os_uname.release,
                                 version=os_uname.version,
                                 machine=os_uname.machine)
uname.__doc__ = _uname.__doc__


def patch_module():
    platform.uname = uname
