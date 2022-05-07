from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hour = time.strftime('%I')      # getting hour element from time. strf means string format
    minute = time.strftime('%M')    # getting minute
    sec = time.strftime('%S')       # getting seconds
    ampm = time.strftime('%p')      #getting am/pm
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')

    label_hour.config(text=hour)
    label_min.config(text=minute)
    label_sec.config(text=sec)
    label_ampm.config(text=ampm)
    label_date.config(text=date)
    label_month.config(text=month)
    label_year.config(text=year)
    label_day.config(text=day)

    label_hour.after(200, date_time)        #after function recalls program for data. Hence data gets updated. 200 milliseconds
    





clock = Tk()     # creating object of class Tk
clock.title('My Digital Clock Using Python')    # setting window title
clock.geometry('1000x500')  # setting window size
clock.config(bg='black')

############ Time - Hours, Minutes, Seconds, AM/PM  ##########################

label_hour = Label(clock, text="00", font=('Times New Roman', 40, "bold"), bg='white', fg='black') # setting properties of box inside window
label_hour.place(x=120, y=50, height=110, width=100)
label_hour_txt = Label(clock, text="HOUR", font=('Times New Roman', 18, "bold"), bg='white', fg='black') # setting properties of box inside window
label_hour_txt.place(x=120, y=190, height=30, width=100)

label_min = Label(clock, text="00", font=('Times New Roman', 40, "bold"), bg='white', fg='black') # setting properties of box inside window
label_min.place(x=340, y=50, height=110, width=100)
label_min_txt = Label(clock, text="MINUTE", font=('Times New Roman', 18, "bold"), bg='white', fg='black') # setting properties of box inside window
label_min_txt.place(x=340, y=190, height=30, width=100)

label_sec = Label(clock, text="00", font=('Times New Roman', 40, "bold"), bg='white', fg='black') # setting properties of box inside window
label_sec.place(x=560, y=50, height=110, width=100)
label_sec_txt = Label(clock, text="SECOND", font=('Times New Roman', 18, "bold"), bg='white', fg='black') # setting properties of box inside window
label_sec_txt.place(x=560, y=190, height=30, width=100)

label_ampm = Label(clock, text="00", font=('Times New Roman', 40, "bold"), bg='white', fg='black') # setting properties of box inside window
label_ampm.place(x=780, y=50, height=110, width=100)
label_ampm_txt = Label(clock, text="AM/PM", font=('Times New Roman', 18, "bold"), bg='white', fg='black') # setting properties of box inside window
label_ampm_txt.place(x=780, y=190, height=30, width=100)



################ Date - Date, Month, Year, Day ######################

label_date = Label(clock, text="00", font=('Times New Roman', 40, "bold"), bg='white', fg='black') # setting properties of box inside window
label_date.place(x=120, y=250, height=110, width=100)
label_date_txt = Label(clock, text="DATE", font=('Times New Roman', 18, "bold"), bg='white', fg='black') # setting properties of box inside window
label_date_txt.place(x=120, y=390, height=30, width=100)

label_month = Label(clock, text="00", font=('Times New Roman', 40, "bold"), bg='white', fg='black') # setting properties of box inside window
label_month.place(x=340, y=250, height=110, width=100)
label_month_txt = Label(clock, text="MONTH", font=('Times New Roman', 18, "bold"), bg='white', fg='black') # setting properties of box inside window
label_month_txt.place(x=340, y=390, height=30, width=100)

label_year = Label(clock, text="00", font=('Times New Roman', 40, "bold"), bg='white', fg='black') # setting properties of box inside window
label_year.place(x=560, y=250, height=110, width=100)
label_year_txt = Label(clock, text="YEAR", font=('Times New Roman', 18, "bold"), bg='white', fg='black') # setting properties of box inside window
label_year_txt.place(x=560, y=390, height=30, width=100)

label_day = Label(clock, text="00", font=('Times New Roman', 40, "bold"), bg='white', fg='black') # setting properties of box inside window
label_day.place(x=780, y=250, height=110, width=100)
label_day_txt = Label(clock, text="DAY", font=('Times New Roman', 18, "bold"), bg='white', fg='black') # setting properties of box inside window
label_day_txt.place(x=780, y=390, height=30, width=100)


date_time()

clock.mainloop() # opens a window and keeps it running until user closes using GUI 