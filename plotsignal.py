import subprocess
import re
import platform
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.animation as animation

#initialize the plot
x_data, y_data = [], []
fig = plt.figure()
axis = plt.axes(ylim =(0, 150)) 
line, = axis.plot([], [],)

def plot_signal():
    axis.set_title('Wifi Signal over Time')
    plt.xlabel('Time [s]')
    plt.ylabel('Signal Level [%]')
    anim = animation.FuncAnimation(fig, animate, interval = 150)
    plt.show()	


def animate(frames):
    x_data.append(datetime.now())
    signalValue = read_signal()
    y_data.append(signalValue)
    line.set_data(x_data,y_data)
    fig.gca().relim()
    fig.gca().autoscale_view()
    return line,



def read_signal()->int:
	if platform.system() == 'Linux':
		p = subprocess.Popen("iwconfig", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	elif platform.system() == 'Windows':
		p = subprocess.Popen("netsh wlan show interfaces", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	else:
		raise Exception('reached else of if statement')
	out = p.stdout.read().decode()

	if platform.system() == 'Linux':
		m = re.findall('(wlan[0-9]+).*?Signal level=(-[0-9]+) dBm', out, re.DOTALL)
	elif platform.system() == 'Windows':
		m = re.findall('Name.*?:.*?([A-z0-9 ]*).*?Signal.*?:.*?([0-9]*)%', out, re.DOTALL)
	else:
		raise Exception('reached else of if statement')

	p.communicate()

	return int(m[0][1])

	