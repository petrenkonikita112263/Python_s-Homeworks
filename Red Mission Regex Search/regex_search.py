import os
import sys

walk_dir = sys.argv[0]

print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
walk_dir = os.path.abspath(walk_dir)
