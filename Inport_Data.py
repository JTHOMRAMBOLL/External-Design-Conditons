import pandas as pd
from ladybug.epw import EPW
import sys 
import PySimpleGUI as sg


def Loadfile():
    if len(sys.argv) == 1:
            event, values = sg.Window('Load EPW File',
                            [[sg.Text('Document to open')],
                            [sg.In(), sg.FileBrowse()],
                            [sg.Open(), sg.Cancel()]]).read(close=True)
            fname = values[0]
    else:
            fname = sys.argv[1]

    
    if not fname:
            sg.popup("Cancel", "No filename supplied")
            raise SystemExit("Cancelling: no filename supplied")
    return(fname)

EP_File=Loadfile()

epw_data = EPW(EP_File)
dry_bulb_temp = epw_data.dry_bulb_temperature

print(dry_bulb_temp)