import pandas as pd
from ladybug.epw import EPW
import sys 
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

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
dry_bulb_temp = epw_data.dry_bulb_temperature.values



dt = epw_data.dry_bulb_temperature.datetimes
data={'Date':list(dt),'Dry Build Temperature':list(dry_bulb_temp)}

df = pd.DataFrame(data).set_index('Date')
df['Dry Build Temperature']=df.round(0).astype(int)
#value_bins = df['Bins'].value_counts()
#print(value_bins)

#Count=df.groupby('Bins').Bins.nunique()

#print(Count)

#value_bins.plot.hist(bins=32)


fig, ax = plt.subplots()
plt.figure(figsize=(14,7))
counts, bins, patches = ax.hist(df,bins=30 , facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5,rwidth=0.9)

# Set the ticks to be at the edges of the bins.
ax.set_xticks(bins)

for bar in patches:
    if bar.get_x() < 5:
        bar.set_facecolor("cornflowerblue")
    elif bar.get_x()>18:
        bar.set_facecolor("firebrick")
    else:
        bar.set_facecolor("C1")

rects = ax.patches
labels = ["%dhrs" % i for i in counts]

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
            ha='center', va='bottom')

plt.style.use('seaborn-whitegrid') # nice and clean grid
#plt.hist(x,bins=30, facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5,rwidth=0.9)
#plt.title('Normal Distribution') 

plt.show()

print(df)

