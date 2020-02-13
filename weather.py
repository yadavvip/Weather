from tkinter import *
import requests


# HEIGHT=650
# WIDTH=550
# def f1(entry):
#     print("The entry is:",entry)

def format_response(weather):
    try:
        coord=weather['coord']
        descrip=weather['weather'][0]['description']
        temperature=weather['main']['temp']
        pressure=weather['main']['pressure']
        final_str='coordinates:- %s\n description:- %s\n temperature:- %s\n pressure:- %s\n'%(coord,descrip,temperature,pressure)
    except:
        final_str='enter valid info'
    return final_str
def get_weather(city):
    weather_key ='801840575bee5bbec3755e3e63c297af'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'metric'}
    response=requests.get(url,params=params)
    weather=response.json()
    label['text']=format_response(weather)
# 801840575bee5bbec3755e3e63c297af
#api.openweathermap.org/data/2.5/forecast?id={city ID
root=Tk()
root.title('WEATHER FORECAST')
background_image=PhotoImage(file='bank.png')
back_label=Label(root,image=background_image)
back_label.place(x=0,y=0,relwidth=1,relheight=1)
root.geometry('650x550')
frame=Frame(root,bg='#80c1ff',bd='5')
frame.place(relx=.5,rely=.07,relheight=.1,relwidth=.75,anchor='n')
entry=Entry(frame,font=40)
entry.place(relwidth=.65,relheight=1)
button=Button(frame,text='Get_Weather',font='40',command=lambda: get_weather(entry.get()))
button.place(relx=.7,relheight=1,relwidth=.25)
lower_frame=Frame(root,bg='#80c1ff',bd='10')
lower_frame.place(relx=.5,rely=.25,relwidth=.75,relheight=.6,anchor='n')
label=Label(lower_frame)
label.place(relwidth=1,relheight=1)
root.mainloop()