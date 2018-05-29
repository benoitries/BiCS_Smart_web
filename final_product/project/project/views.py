from django.shortcuts import render
#from .forms import plugs
from django.contrib.auth.models import User, Group
from pyW215.pyW215 import SmartPlug, ON, OFF
import pandas as pd
import datetime as dt
from .forms import plugs
import urllib.request as url
import datetime as dt
import random as rd

#This function will be used to determine which picture to load in the homepage
def img(target_url):
    data = url.urlopen(target_url)

    date = str(dt.datetime.now())
    l_date = date.split()
    l_last_item = []

    for line in data:
        if l_date[0] in str(line):
            if l_last_item == []:
                l_last_item.append(str(line))
            else:
                del l_last_item[0]
                l_last_item.append(str(line))

    line = l_last_item[0]
    string = str(line[82:126])
    return string


#This function works only with csv files that are structured with the following headers: Date, Heure, SensorName, Value
def datamin(data):
    dictofindex = {}
    dictofvalues = {}
    #This loops are used to find the latest value of a Sensor
    for i in range (0,len(data)):
        if data['SensorName'][i] not in dictofindex:
            dictofindex.update({data['SensorName'][i]:i})
        else:
            del dictofindex[data['SensorName'][i]]
            dictofindex.update({data['SensorName'][i]:i})

    #Now that we have the index' of the latest values, we want to know the actual values
    #The following loop takes care of this
    for x in dictofindex:
        dictofvalues.update({data['SensorName'][dictofindex[x]]:data['Value'][dictofindex[x]]})        
    return dictofvalues

#This function returns the real values of the dic
def if_real(dic):
    ignore_this = 0
    dic_of_reals = {}
    for x,y in dic.items():
        try:
            isinstance(float(y), float)
            dic_of_reals.update({x:y})
        except ValueError:
            ignore_this = 0
    return dic_of_reals

#This function makes it so that the reals are dividable by 5
def real_to_mod5(l):
    fdic = {}
    for x,y in l.items():
        newy = float(y)
        for i in range(5,61,5):
            if newy != 0:
                mod = newy-i
            if mod < 3:
                newy = i
                fdic.update({x:str(newy)})
                break
    return fdic

#This function makes it so that the reals are dividable by 20
def real_to_mod20(l):
    fdic = {}
    for x,y in l.items():
        newy = float(y)
        for i in range(0,100,20):
            if newy != 0:
                mod = newy-i
            if mod != 0:
                if mod < 11:
                    newy = i
                    fdic.update({x:newy})
                    break
            else:
                fdic.update({x:newy})
                break
    return fdic

def index(request):
    Staff = Group.objects.all()[0]
    Tech = Group.objects.all()[1]
    data = pd.read_csv("C:\\Users\\viclo\\Desktop\\BSP2\\The_project\\final_product\\project\\values.csv", sep=';')
    dic = datamin(data)

    #plugs
    dic_of_plug1 = {'BLAB-PLUG1':dic['BLAB-PLUG1']}
    dic_of_plug2 = {'BLAB-PLUG2':dic['BLAB-PLUG2']}
    on_or_off1 = dic['BLAB-PLUG1']
    on_or_off2 = dic['BLAB-PLUG2']

    #humidity
    dic_of_humid1 = {'BLAB-HUMID-AIR-1':dic['BLAB-HUMID-AIR-1']}
    dic_of_humid2 = {'BLAB-HUMID-SOIL-1':dic['BLAB-HUMID-SOIL-1']}
    dic_of_approx_hum1 = real_to_mod20(dic_of_humid1)
    dic_of_approx_hum2 = real_to_mod20(dic_of_humid2)

    #temeperature                
    dic_of_temp1 = {'BLAB-TEMP-AIR-1':dic['BLAB-TEMP-AIR-1']}
    dic_of_temp2 = {'BLAB-TEMP-AIR-2':dic['BLAB-TEMP-AIR-2']}
    dic_of_temp3 = {'BLAB-TEMP-SOIL-2':dic['BLAB-TEMP-SOIL-2']}                 
    dic_of_approx_temp1 = real_to_mod5(dic_of_temp1)
    dic_of_approx_temp2 = real_to_mod5(dic_of_temp2)
    dic_of_approx_temp3 = real_to_mod5(dic_of_temp3)

    #plug_control
    IP = 'Invalid Ip'
    Password = 'Invalid Password'
    state = ''
    temperature = 0
    consumption = 0
    total_cuns = 0
    form = ""
    
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = plugs(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            action = form.cleaned_data['choice_field']

            if (action == 'info_1'):
                IP = '10.212.232.12'
                Password = '195570'
                sp = SmartPlug(str(IP), str(Password))
                state = sp.state
                temperature = sp.temperature
                consumption = sp.current_consumption
                total_cuns = sp.total_consumption
            elif (action == 'on_off_1'):
                IP = '10.212.232.12'
                Password = '195570'
                sp = SmartPlug(str(IP), str(Password))
                if sp.state == 'OFF':
                    sp.state = ON
                else:
                    sp.state = OFF
                state = sp.state
            elif (action == 'info_2'):
                IP = '10.212.232.11'
                Password = '570530'
                sp = SmartPlug(str(IP), str(Password))
                state = sp.state
                temperature = sp.temperature
                consumption = sp.current_consumption
                total_cuns = sp.total_consumption
            elif (action == 'on_off_2'):
                IP = '10.212.232.11'
                Password = '570530'
                sp = SmartPlug(str(IP), str(Password))
                if sp.state == 'OFF':
                    sp.state = ON
                else:
                    sp.state = OFF
                state = sp.state
                
    links = []
    for i in range(1,3):
        links += [img('https://messir.uni.lu/bicslab/blab-cam'+str(i)+'-snapshots/gallery-images/')]
    
    return render(request, 'index.html', {'dic_of_temp1':dic_of_temp1,
                                          'img1':links[0],
                                          'img2':links[1],
                                          'dic_of_approx_temp1':dic_of_approx_temp1,
                                          'dic_of_temp2':dic_of_temp2,
                                          'dic_of_approx_temp2':dic_of_approx_temp2,
                                          'dic_of_temp3':dic_of_temp3,
                                          'dic_of_approx_temp3':dic_of_approx_temp3,                                             'dic_of_humid1':dic_of_humid1,
                                          'dic_of_approx_hum1':dic_of_approx_hum1,
                                          'dic_of_humid2':dic_of_humid2,
                                          'dic_of_approx_hum2':dic_of_approx_hum2,
                                          'dic_of_plug1':dic_of_plug1,
                                          'dic_of_plug2':dic_of_plug2,
                                          'on_or_off1':on_or_off1,
                                          'on_or_off2':on_or_off2,
                                          'Staff':Staff,
                                          'Tech':Tech,
                                          'form':form,
                                          'state':state,
                                          'temeperature':temperature,
                                          'consumption':consumption,
                                          'total_cuns':total_cuns
                                               })

#These returns the reverse of a list
def reverse_list(l):
    lrev = []
    for i in range(len(l)-1,-1,-1):
        lrev.append(l[i])
    return lrev

#These two functions are needed to plot the charts later on
def chart_values(data,Sensor,list_of_values,list_of_date):
    for i in range(len(data)-1,-1,-1):
        if data['SensorName'][i]==Sensor:
            list_of_values.append(float(data['Value'][i]))
            list_of_date.append(data['Date'][i])
            if len(list_of_values)==31:
                break
    

def chart_script(data,destination,Sensor,list_of_values,list_of_date,number,color,rgba):
    chart_values(data,Sensor,list_of_values,list_of_date)
    list_of_values = reverse_list(list_of_values)
    list_of_date = reverse_list(list_of_date)
    f = open(destination,'w')
    f.write('var used_label = '+str(list_of_date)+'\n')
    f.write('var used_data = '+str(list_of_values)+'\n')
    f.write(' \n')
    f.write('var ctx = document.getElementById("myChart'+str(number)+'"); \n')
    f.write('var myChart = new Chart(ctx, { \n')
    f.write("  type: 'line', \n")
    f.write('  data: { \n')
    f.write('    labels: used_label, \n')
    f.write('    datasets: [ \n')
    f.write('      {  \n')
    f.write('        borderColor: "'+color+'", \n')
    f.write('        pointBorderColor: "'+color+'",\n')
    f.write('        pointBackgroundColor: "'+color+'",\n')
    f.write('        fill: true,\n')
    f.write('        backgroundColor: "'+rgba+'",\n')
    f.write("        label: 'Value',\n")
    f.write('        data: used_data \n')
    f.write('      } \n')
    f.write('    ] \n')
    f.write('  }, \n')
    f.write('  options: { \n')
    f.write('      scales: {\n')
    f.write('          yAxes: [{\n')
    f.write('              ticks: {\n')
    f.write('                  beginAtZero: true\n')
    f.write('              }\n')
    f.write('          }]\n')
    f.write('      }\n')
    f.write('  }\n')
    f.write('}); \n')
    f.close()

def charts(request):
    data = pd.read_csv("C:\\Users\\viclo\\Desktop\\BSP2\\The_project\\final_product\\project\\values.csv", sep=';')

    l_of_names = []
    for i in range (0,len(data)):
        if ('PLUG' not in str(data['SensorName'][i])) and (str(data['SensorName'][i])!='nan') and (data['SensorName'][i] not in l_of_names):
            l_of_names += [data['SensorName'][i]]

    l_of_sensors = {}
    for x in l_of_names:
        l_of_sensors.update({x:l_of_names.index(x)})

    l_of_colours = [('#D9EDF7','rgba(217, 237, 247, 0.65)'),('#F2DEDE','rgba(242, 222, 222, 0.65)'),('#FCF8E3','rgba(252, 248, 227, 0.65)'),('#DFF0D8','rgba(223, 240, 216, 0.65)')]

    for x,y in l_of_sensors.items():
        i = rd.randint(0,3)
        colour = l_of_colours[i]
        if y==0:
            chart_script(data,"C:\\Users\\viclo\\Desktop\\BSP2\\The_project\\final_product\\project\\webapp\\static\\data\\data.js",x,[],[],y,colour[0],colour[1])
        else:
            chart_script(data,"C:\\Users\\viclo\\Desktop\\BSP2\\The_project\\final_product\\project\\webapp\\static\\data\\data"+str(y+1)+".js",x,[],[],y,colour[0],colour[1])
    
    return render(request, 'charts.html', {'sensors':l_of_sensors})
    
    #we will use that later
    """IP = 'Invalid Ip'
    Password = 'Invalid Password'
    state = ''
    temperature = 0
    consumption = 0
    total_cuns = 0
    
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = plugs(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            if (form.cleaned_data['plug_ip'] == '10.212.232.12') and (form.cleaned_data['plug_pw'] == '195570'):
                IP = form.cleaned_data['plug_ip']
                Password = form.cleaned_data['plug_pw']
                sp = SmartPlug(str(IP), str(Password))
                action = form.cleaned_data['plug_action']

                if (action == 'Info') or (action == 'info'):
                    state = sp.state
                    temperature = sp.temperature
                    consumption = sp.current_consumption
                    total_cuns = sp.total_consumption
                elif action == 'ON':
                    sp.state = ON
                    state = sp.state
                elif action == 'OFF':
                    sp.state = OFF
                    state = sp.state

    return render(request, 'index.html' ,{'form':form,
                                          'IP':IP,
                                          'Pw':Password,
                                          'state':state,
                                          'temeperature':temperature,
                                          'consumption':consumption,
                                          'total_cuns':total_cuns})"""
