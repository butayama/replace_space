from testfixtures import TempDirectory
import subprocess
import shlex
from search_space import foo2bar


def test_foo2bar():

    with TempDirectory() as d:
        d.write('test.txt', b'some foo thing')
        foo2bar(d.path, 'test.txt')
        d.read('test.txt')


def test_command_line_arguments():
    subprocess.call(shlex.split('./home/uwe/D_sdb2/GitHub/replace_space/src/command_line/replace_space.py -analyse /home/uwe/D_sdb2/Blender'))
