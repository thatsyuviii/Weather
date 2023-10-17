from tkinter import *
import datetime
from tkinter import Frame
import requests
import calendar
import time
import tkinter.font as font
from PIL import ImageTk, Image
from timezonefinder import TimezoneFinder
import pytz
from geopy.geocoders import Nominatim


def ex():
    var1.set(1)


location = ""

root = Tk()
root.minsize(450, 700 )
root.maxsize(450, 500 )
root.title( "Weather Forecasting" )  # created the main frame
label2 = Frame( root )

def sets():
    global location
    location = name_entry.get()
    var.set(1)


location = "null"

while True:  # if user enter wrong city name

    c1g = ImageTk.PhotoImage( Image.open( './pj1.jpg' ) )
    label2.place( height=700, width=600, x=0, y=0 )

    labelg2 = Label( label2, image=c1g )
    labelg2.place( height=1000, width=500, x=-25, y=-120 )
    btn = Button(label2, text = 'Search !', bd = '5',command = sets, bg='#373737', fg='white')

    name_var = StringVar()
    name_entry = Entry( label2, textvariable=name_var, font=('calibre', 10, 'normal') , bg='#373737', fg='white',justify=CENTER)

    var = IntVar()
    var1 = IntVar()

    name_entry.place(height=50, width=200, x=120, y=470)
    btn.place(height=50, width=200, x=120, y=540)
    label1 = Frame( root )

    btn.wait_variable(var)
    location = location.lower()
    for widget in label2.winfo_children():
        widget.destroy()
    if location == "":
        location = "null"

    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=d1047658669f11b91c03b9e9c7a9d8d0"  ##url for open wen API

    api_link = requests.get( complete_api_link )  # sending request to server
    api_data = api_link.json()
    if api_data['cod'] != '404':
        break
    else:
        print( "Invalid city name is entered, please check your city name :", format( location ) )
if False:
    j=0
else:

    # api_keys = "d1047658669f11b91c03b9e9c7a9d8d0"
    geolocator = Nominatim( user_agent="your_app_name" )
    loc = geolocator.geocode(location)
    print( (loc.latitude, loc.longitude) )

    obj = TimezoneFinder()

    # pass the longitude and latitude
    # in timezone_at and
    # it return time zone
    tiz = obj.timezone_at( lng=loc.longitude, lat=loc.latitude )



    # Convert timezone to time
    now_time = datetime.datetime.now( pytz.timezone( tiz ) )
    print(now_time)

    Current_Date = now_time.date()
    label17 = Frame( root )
    label19 = Frame( root )
    if now_time.hour >= 5 and now_time.hour < 12:
        c1 = ImageTk.PhotoImage(Image.open( './back/Golden.jpeg' ) )
        # adding background to main frame
        c1_label = Label( label17, image=c1 )
        c1_label.pack()

        label17.place( x=-5, y=-5 )
        label11: Frame = Frame( label1 )
        label11.place( height=400, width=320, x=70, y=70 )

    elif now_time.hour >= 12 and now_time.hour <= 16:
        c1 = ImageTk.PhotoImage( Image.open( './back/Gorgeous.jpeg' ) )
        # adding background to main frame
        c1_label = Label( label17, image=c1 )
        c1_label.pack()

        label17.place( x=-5, y=-5 )
        label11: Frame = Frame( label1 )
        label11.place( height=400, width=320, x=70, y=70 )

    elif now_time.hour > 16 and now_time.hour <= 18:
        c1 = ImageTk.PhotoImage( Image.open( './back/Quotes.jpeg' ) )
        # adding background to main frame
        c1_label = Label( label17, image=c1 )
        c1_label.pack()
        label17.place(x=-5,y=-5)
        label11: Frame = Frame( label1 )
        label11.place( height=400, width=320, x=70, y=70 )

    elif now_time.hour > 18 and now_time.hour < 20:
        c1 = ImageTk.PhotoImage( Image.open( './back/night.jpeg' ) )
        # adding background to main frame
        c1_label = Label( label17, image=c1 )
        c1_label.pack()

        label17.place( x=-5, y=-5 )
        label11: Frame = Frame( label1 )
        label11.place( height=400, width=320, x=70, y=70 )

    else:
        c1 = ImageTk.PhotoImage( Image.open( './back/night.jpeg' ) )
        # adding background to main frame
        c1_label = Label( label17, image=c1 )
        c1_label.pack()
        label17.place( x=-5, y=-5 )
        label11: Frame = Frame( label1 )

    if now_time.hour >= 5 and now_time.hour <= 18:  # check if its currently day

        c11 = ImageTk.PhotoImage(
            Image.open(
                './day1234.jpg' ) )  # day background for day time in frame 2
        c11_label = Label( label19, image=c11 )
        c11_label.pack()
    else:

        c11 = ImageTk.PhotoImage(
            Image.open(
                './night12345.jpg' ) )  # night background for night time in frame 2
        c11_label = Label( label19, image=c11 )
        c11_label.pack()

    label19.place(height=420, width=320, x=70, y=65 )

    label111 = Frame( root )
    label111.place( height=180, width=320, x=70, y=470 )
    c111 = ImageTk.PhotoImage(
        Image.open(
            './background1png.png' ) )  # frame 3 beholding the description part
    c111_label = Label( label111, image=c111 )
    c111_label.pack()


    # now creating variables to store data
    temp_city = int( (api_data['main']['temp']) - 273.15 )
    real_feel = int( (api_data['main']['feels_like']) - 273.15 )
    min_temp = int( (api_data['main']['temp_min']) - 273.15 )
    max_temp = int( (api_data['main']['temp_max']) - 273.15 )
    description = (api_data['weather'][0]['description'])
    humidity_city = (api_data['main']['humidity'])
    country = (api_data['sys']['country'])
    sunrise_time = time.strftime( "%I:%M:%S", time.gmtime( api_data['sys']['sunrise'] - 19800 ) )
    sunset_time = time.strftime( "%I:%M:%S", time.gmtime( api_data['sys']['sunset'] - 19800 ) )

    # now showing icons according to the current_state
    if description == 'clear sky':
        state_icon = ImageTk.PhotoImage( Image.open( './sunnydayr.png' ) )
        state_iconimg = Label( root, image=state_icon, bg='#87CEFA' )
        state_iconimg.place( height=100, width=100, x=180, y=490 )

    if description == 'smoke' or description == 'haze' or description == 'mist' or description == 'fog':
        state_icon = ImageTk.PhotoImage( Image.open( './foggyr.png' ) )
        state_iconimg = Label( root, image=state_icon, bg='#87CEFA' )
        state_iconimg.place( height=100, width=100, x=180, y=490 )

    if description == 'broken clouds':
        state_icon = ImageTk.PhotoImage( Image.open( './stromyr1.png' ) )
        state_iconimg = Label( root, image=state_icon, bg='#87CEFA' )
        state_iconimg.place( height=100, width=100, x=180, y=490 )

    if description == 'scattered clouds' or description == 'overcast clouds':
        state_icon = ImageTk.PhotoImage( Image.open( './cloudsonlyr.png' ) )
        state_iconimg = Label( root, image=state_icon, bg='#87CEFA' )
        state_iconimg.place( height=100, width=100, x=180, y=490 )

    if (description == 'few clouds'):
        state_icon = ImageTk.PhotoImage( Image.open( './cloudysunr.png' ) )
        state_iconimg = Label( root, image=state_icon, bg='#87CEFA' )
        state_iconimg.place( height=100, width=100, x=180, y=490 )

    if description == 'heavy intensity rain' or description == 'light rain' or description == 'moderate rain':
        state_icon = ImageTk.PhotoImage( Image.open( './rainyr.png' ) )
        state_iconimg = Label( root, image=state_icon, bg='#87CEFA' )
        state_iconimg.place( height=100, width=100, x=180, y=494 )

    # label for current state of weather

    myfont = font.Font( size=20 )
    description_type = Label( root, text=description, bd=1,
                              bg='#87CEFA' )  # bd=2,relief="solid",font="Times 32",width=30,height=2)
    description_type.place( height=20, width=100, x=180, y=598 )

    # label for city temperature
    if now_time.hour >= 5 and now_time.hour <= 18:
        myfont2 = font.Font( size=22 )
        temp_city_label = Label( root, text=str( temp_city ) + '°C', bd=2,
                                 font=myfont, bg='#fde080')  # bd=2,relief="solid",font="Times 32",width=30,height=2)
        temp_city_label.place( height=60, width=70, x=315, y=276 )
    else:
        myfont2 = font.Font( size=22 )
        temp_city_label = Label( root, text=str( temp_city ) + '°C', bd=2,
                                 font=myfont, bg='#4C688D' )  # bd=2,relief="solid",font="Times 32",width=30,height=2)
        temp_city_label.place( height=60, width=70, x=315, y=276 )

    # label for showing current date
    if now_time.hour >= 5 and now_time.hour <= 18:
        date_label = Label(root, text=str(Current_Date.day) + '/' + str(Current_Date.month ) + '/' + str(
            Current_Date.year),
                            bd=1, bg='#fde080')  # bd=2,relief="solid",font="Times 32",width=30,height=2)
        date_label.place(height=25, width=80, x=305, y=80)
    else:
        date_label = Label(root,
                            text=str( Current_Date.day) + '/' + str( Current_Date.month) + '/' + str(
                                Current_Date.year),
                            bd=1, bg='#4C688D')  # bd=2,relief="solid",font="Times 32",width=30,height=2)
        date_label.place(height=25, width=80, x=305, y=80)

    # showing city name

    city_name_label = Label(root, text=location.upper(), bg='#87CEFA',
                             font=myfont)  # bd=2,relief="solid",font="Times 32",width=30,height=2)
    city_name_label.place(height=30, width=320, x=70, y=440)

    # label for humidity

    humidity_label = Label(root, text='Humidity :' + str( humidity_city ) + "%",
                            bd=0.5, bg='#87CEFA')  # bd=2,relief="solid",font="Times 32",width=30,height=2)
    humidity_label.place(height=20, width=103, x=70, y=494)

    # showing average_temperature

    real_feel_label = Label(root, text='Avg-Temp :' + str(real_feel) + "°C",
                             bd=0.5, bg='#87CEFA')  # bd=2,relief="solid",font="Times 32",width=30,height=2)
    real_feel_label.place(height=20, width=103, x=70, y=519)

    # showing minimum_temperature

    max_temp_label = Label(root, text='Min-Temp :' + str(min_temp) + "°C",
                            bd=0.5, bg='#87CEFA')  # bd=2,relief="solid",font="Times 32",width=30,height=2)
    max_temp_label.place(height=20, width=103, x=70, y=544)

    # showing maximum_temperature

    min_temp_label = Label(root, text='Max-Temp :' + str(max_temp) + "°C",
                            bd=0.5, bg='#87CEFA')  # bd=2,relief="solid",font="Times 32",width=30,height=2)
    min_temp_label.place(height=20, width=103, x=70, y=569)

    # showing current time

    time_label = Label(root, text=str( now_time.hour ) + ' hours ' + str( now_time.minute ) + ' minutes',
                        bd=2, bg='#87CEFA')  # font=myfont)#bd=2,relief="solid",font="Times 32",width=30,height=2)
    time_label.place(height=20, width=125, x=70, y=622)

    # checking current hours to show morning,afternoon,evening & night

    if now_time.hour >= 5 and now_time.hour < 12:
        title = Label(root, text='Good Morning', font=('ariel', 22, 'bold'), foreground='black', bg='#fde080')
        title.place(height=40, width=320, x=70, y=30)
        title.after(1000)

    elif now_time.hour >= 12 and now_time.hour <= 16:
        title = Label(root, text='Good Afternoon', font=('ariel', 22, 'bold'), foreground='black', bg='#fde080')
        title.place(height=40, width=320, x=70, y=30)
        title.after(1000)

    elif now_time.hour > 16 and now_time.hour <= 18:
        title = Label(root, text='Good Evening', font=('ariel', 22, 'bold'), foreground='black', bg='#fde080')
        title.place(height=40, width=320, x=70, y=30)
        title.after(1000)

    elif now_time.hour > 18 and now_time.hour < 20:
        title = Label(root, text='Good Evening', font=('ariel', 22, 'bold'), foreground='black', bg='#4C688D')
        title.place(height=40, width=320, x=70, y=30)
        title.after(1000)

    else:
        title = Label(root, text='Good Night', font=('ariel', 22, 'bold'), foreground='black', bg='#4C688D')
        title.place(height=40, width=320, x=70, y=30)
        title.after(1000)


    # function to find current day
    def findday(date):
        today_day = datetime.datetime.strptime( date, "%d %m %Y" ).weekday()
        return calendar.day_name[today_day]


    date = str(Current_Date.day) + " " + str(now_time.month) + " " + str(now_time.year)
    today_day = findday(date)

    # label for showing current day

    if now_time.hour >= 5 and now_time.hour <= 18:
        day_label = Label(root, text=today_day, bd=2, bg='#fde080')  # bd=2,relief="solid",font="Times 32",width=30,height=2)
        day_label.place(height=35, width=70, x=315, y=348)

    else:
        day_label = Label(root, text=today_day, bd=2,
                           bg='#4C688D')  # bd=2,relief="solid",font="Times 32",width=30,height=2)
        day_label.place(height=35, width=70, x=315, y=348)

    # label showing sunrise time

    sunrise_label = Label(root, text='SunRise :', bd=1, bg='#87CEFA')
    sunrise_label.place(height=20, width=103, x=287, y=494)

    sunrisetime_label = Label(root, text=sunrise_time, bd=1, bg='#87CEFA')
    sunrisetime_label.place(height=20, width=103, x=287, y=519)

    # label showing sunset time

    sunset_label = Label(root, text='SunSet :', bd=1, bg='#87CEFA')
    sunset_label.place(height=20, width=103, x=287, y=544)

    sunsettime_label = Label(root, text=sunset_time, bd=1, bg='#87CEFA')
    sunsettime_label.place(height=20, width=103, x=287, y=569)

    # label showing currently day/night

    if now_time.hour >= 5 and now_time.hour < 12:
        situation = 'MORNING'
        icon = ImageTk.PhotoImage( Image.open('./sunnydayr.png'))
        icon_img = Label(root, image=icon, bg='#fde080')
        icon_img.place(height=120, width=120, x=70, y=102)
        day_night_label = Label(root, text=situation, bd=1, bg='#fde080')

    elif now_time.hour >= 12 and now_time.hour <= 16:
        situation = 'DAY'
        icon = ImageTk.PhotoImage(Image.open('./sunnydayr.png'))
        icon_img = Label(root, image=icon, bg='#fde080')
        icon_img.place(height=120, width=120, x=70, y=102)
        day_night_label = Label(root, text=situation, bd=1, bg='#fde080')

    elif now_time.hour > 16 and now_time.hour <= 18:
        situation = 'EVENING'
        icon = ImageTk.PhotoImage(Image.open('./sunnydayr.png'))
        icon_img = Label(root, image=icon, bg='#fde080')
        icon_img.place(height=120, width=120, x=70, y=102)
        day_night_label = Label(root, text=situation, bd=1, bg='#fde080')

    elif now_time.hour > 18 and now_time.hour < 20:
        situation = 'EVENING'
        icon = ImageTk.PhotoImage(Image.open('./moonr.png'))
        icon_img = Label(root, image=icon, bg='#4C688D')
        icon_img.place(height=120, width=120, x=70, y=92)
        day_night_label = Label(root, text=situation, bd=1, bg='#4C688D')

    else:
        situation = 'NIGHT'
        icon = ImageTk.PhotoImage(Image.open('./moonr.png'))
        icon_img = Label(root, image=icon, bg='#4C688D')
        icon_img.place(height=120, width=120, x=70, y=92)
        day_night_label = Label(root, text=situation, bd=1, bg='#4C688D')

    day_night_label.place(height=20, width=120, x=70, y=210)

    btn2 = Button( root, text='Exit !', bd='5', command=ex, bg='#87CEFA', fg='black' )

    btn2.place( height=26, width=100, x=290, y=620)
    label1.place( x=0, y=0 )


    btn2.wait_variable( var1 )