import cx_Freeze
from cx_Freeze import *

setup(
    name='MatrixAutomaton',
    options={'build_exe':{'packages':['numpy','configparser','datetime'],'include_files':['Config.in']}},
    version='2.0',
    description='New Automaton 2.0',
    author='CTCG',
    executables = [
        Executable('TemporalMain.py')]
      )
