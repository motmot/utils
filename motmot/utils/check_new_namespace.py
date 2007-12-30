import sys
import re

# Check if old motmot packages are still being used.  Note that this
# won't pick up multiple import in the same line (e.g. "import blah,
# cam_iface"). Also, note that use of __import__ makes this mostly
# impossible.

# Suggested usage::
#   find . -name '*.py' | xargs motmot_check_new_namespace

old_top_level_modules = ['motmot_utils',
                         'cam_iface',
                         'FastImage',
                         'fview_UDP_logger',
                         'fview',
                         'wxvalidatedtext',
                         'wxvideo',
                         'imops',
                         'fview_PLUGIN_TEMPLATE',
                         'fview_c_callback', 'motmot_utils',
                         'FlyMovieFormat',
                         'wxglvideo',
                         'flytrax',
                         'FastImage',
                         'realtime_image_analysis',
                         'trackem',
                         'fview_UDP_logger']

def main():
    filenames = sys.argv[1:]
    for filename in filenames:
        fd = open(filename, mode='r')
        lineno=0
        for line in fd.readlines():
            lineno+=1
            split = line.strip().split()
            if not len(split):
                continue
            if split[0].startswith('#'):
                continue
            if '__import__' in line:
                if line == "__import__('pkg_resources').declare_namespace(__name__)\n":
                    continue
                else:
                    print 'WARNING: could not parse line %s(%d): %s'%(filename,lineno,repr(line))
                    continue
            if len(split)<2: # cannot be import line
                continue
            if split[0] in ['from','import']:
                top = split[1].split('.')[0]
                if top in old_top_level_modules:
                    print '%s(%d): %s'%(filename,lineno,repr(line))
        fd.close()

if __name__=='__main__':
    main()
