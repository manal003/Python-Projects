from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')

    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_day.config(text=day)
    lab_year.config(text=year)
    lab_mo.config(text=month)


    lab_hr.after(200,date_time)




clock = Tk()
clock.title('     **** Digital Clock ****  ')
clock.geometry('1000x500')
clock.config(bg='pink')

lab_hr=Label(clock, text = "00" , font= ('Time New Roman', 60, "bold" ), bg = 'purple', fg='pink' )
lab_hr.place(x=40, y=50, height= 110 ,width=100 )
lab_hr_txt=Label(clock, text = "Hour" , font= ('Time New Roman', 20, "bold" ), bg = 'purple', fg='pink' )
lab_hr_txt.place(x=40, y=190, height= 30 ,width=100 )

lab_min=Label(clock, text = "00" , font= ('Time New Roman', 60, "bold" ), bg = 'purple', fg='pink' )
lab_min.place(x=290, y=50, height= 110 ,width=100 )
lab_min_txt=Label(clock, text = "Min" , font= ('Time New Roman', 20, "bold" ), bg = 'purple', fg='pink' )
lab_min_txt.place(x=290, y=190, height= 30 ,width=100 )

lab_sec=Label(clock, text = "00" , font= ('Time New Roman', 60, "bold" ), bg = 'purple', fg='pink' )
lab_sec.place(x=560, y=50, height= 110 ,width=100 )
lab_sec_txt=Label(clock, text = "Sec" , font= ('Time New Roman', 20, "bold" ), bg = 'purple', fg='pink' )
lab_sec_txt.place(x=560, y=190, height= 30 ,width=100 )

lab_am=Label(clock, text = "00" , font= ('Time New Roman', 45, "bold" ), bg = 'purple', fg='pink' )
lab_am.place(x=780, y=50, height= 110 ,width=100 )
lab_am_txt=Label(clock, text = "AM/PM" , font= ('Time New Roman', 15, "bold" ), bg = 'purple', fg='pink' )
lab_am_txt.place(x=780, y=190, height= 30 ,width=100 )

###### DATE ->

lab_date=Label(clock, text = "00" , font= ('Time New Roman', 60, "bold" ), bg = 'purple', fg='pink' )
lab_date.place(x=40, y=270, height= 110 ,width=100 )
lab_date_txt=Label(clock, text = "Date" , font= ('Time New Roman', 20, "bold" ), bg = 'purple', fg='pink' )
lab_date_txt.place(x=40, y=410, height= 30 ,width=100 )

lab_mo=Label(clock, text = "00" , font= ('Time New Roman', 60, "bold" ), bg = 'purple', fg='pink' )
lab_mo.place(x=290, y=270, height= 110 ,width=100 )
lab_mo_txt=Label(clock, text = "Month" , font= ('Time New Roman', 20, "bold" ), bg = 'purple', fg='pink' )
lab_mo_txt.place(x=290, y=410, height= 30 ,width=100 )

lab_year=Label(clock, text = "00" , font= ('Time New Roman', 60, "bold" ), bg = 'purple', fg='pink' )
lab_year.place(x=560, y=270, height= 110 ,width=100 )
lab_year_txt=Label(clock, text = "Year" , font= ('Time New Roman', 20, "bold" ), bg = 'purple', fg='pink' )
lab_year_txt.place(x=560, y=410, height= 30 ,width=100 )

lab_day=Label(clock, text = "00" , font= ('Time New Roman', 35, "bold" ), bg = 'purple', fg='pink' )
lab_day.place(x=780, y=270, height= 110 ,width=100 )
lab_day_txt=Label(clock, text = "Day" , font= ('Time New Roman', 20, "bold" ), bg = 'purple', fg='pink' )
lab_day_txt.place(x=780, y=410, height= 30 ,width=100 )


date_time()
clock.mainloop()