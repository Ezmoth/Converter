from tkinter import *
from tkinter import ttk
import converters


root = Tk()
root.geometry('450x350')
root.title('Converters')
root.iconbitmap('img\cat.ico')


tabs = ttk.Notebook(root)
tabs.pack()

temp = Frame(tabs, width=400, height=250)
dist = Frame(tabs, width=400, height=250)
weig = Frame(tabs, width=400, height=250)
tim = Frame(tabs, width=400, height=250)

temp.pack(fill='both', expand=1)
dist.pack(fill='both', expand=1)
weig.pack(fill='both', expand=1)
tim.pack(fill='both', expand=1)


# Temperature tab section
temp_units = ['Celcius', 'Farenheit', 'Kelvin', 'Rankine']
choose_temp = StringVar()
choose_temp.set(temp_units[0])

temp_label = Label(temp, text='Choose unit:')
temp_choose = OptionMenu(temp, choose_temp, *temp_units)

def temp_choosen():
    temp_frame = LabelFrame(temp, text='Temperature')
    temp_input = Entry(temp_frame, width=50, borderwidth=5)
    temp_cel = Label(temp_frame, text='Celcius = ')
    temp_far = Label(temp_frame, text='Farenheit = ')
    temp_kel = Label(temp_frame, text='Kelvin = ')
    temp_ran = Label(temp_frame, text='Rankine = ')
    temp_cel_show = Label(temp_frame, text='')
    temp_far_show = Label(temp_frame, text='')
    temp_kel_show = Label(temp_frame, text='')
    temp_ran_show = Label(temp_frame, text='')
    
    def click_temp():
        nonlocal temp_cel_show
        nonlocal temp_far_show
        nonlocal temp_kel_show
        nonlocal temp_ran_show
        
        temp_cel_show.grid_forget()
        temp_far_show.grid_forget()
        temp_kel_show.grid_forget()
        temp_ran_show.grid_forget()
        
        temp_cel_show = Label(temp_frame, text=converters.temperature(choose_temp.get(), float(temp_input.get()))[0])
        temp_far_show = Label(temp_frame, text=converters.temperature(choose_temp.get(), float(temp_input.get()))[1])
        temp_kel_show = Label(temp_frame, text=converters.temperature(choose_temp.get(), float(temp_input.get()))[2])
        temp_ran_show = Label(temp_frame, text=converters.temperature(choose_temp.get(), float(temp_input.get()))[3])
        
        temp_cel_show.grid(row=2, column=1, sticky=W)
        temp_far_show.grid(row=3, column=1, sticky=W)
        temp_kel_show.grid(row=4, column=1, sticky=W)
        temp_ran_show.grid(row=5, column=1, sticky=W)
        
        temp_input.delete(0, END)
                    
    temp_calc = Button(temp_frame, text='Convert', command=click_temp)
  
    temp_frame.grid(row=1, column=0, columnspan=3, padx=5)
    temp_input.grid(row=0, column=0, columnspan=2, padx=5)
    temp_calc.grid(row=0, column=2, padx=10)
    temp_cel.grid(row=2, column=0, sticky=W)
    temp_far.grid(row=3, column=0, sticky=W)
    temp_kel.grid(row=4, column=0, sticky=W)
    temp_ran.grid(row=5, column=0, sticky=W)
    
temp_confirm = Button(temp, text='Choose', command=temp_choosen)


# Distance tab section
dist_units = ['Meters', 'Kilometers', 'Centimeters', 'Milimeters', 'Micrometers', 'Nanometers', 'Miles', 'Yards', 'Foots', 'Inches']
choose_dist = StringVar()
choose_dist.set(dist_units[0])

dist_label = Label(dist, text='Choose unit:')
dist_choose = OptionMenu(dist, choose_dist, *dist_units)

def dist_choosen():
    dist_frame = LabelFrame(dist, text='Distance')
    dist_input = Entry(dist_frame, width=50, borderwidth=5)
    dist_meter = Label(dist_frame, text='Meter = ')
    dist_kilometer = Label(dist_frame, text='Kilometer =')
    dist_centimeter = Label(dist_frame, text='Centimeter =')
    dist_milimeter = Label(dist_frame, text='Milimeter =')
    dist_micrometer = Label(dist_frame, text='Micrometer =')
    dist_nanometer = Label(dist_frame, text='Nanometer =')
    dist_mile = Label(dist_frame, text='Mile =')
    dist_yard = Label(dist_frame, text='Yard =')
    dist_foot = Label(dist_frame, text='Foot =')
    dist_inch = Label(dist_frame, text='Inch =')
    
    dist_meter_show = Label(dist_frame, text='')
    dist_kilometer_show = Label(dist_frame, text='')
    dist_centimeter_show = Label(dist_frame, text='')
    dist_milimeter_show = Label(dist_frame, text='')
    dist_micrometer_show = Label(dist_frame, text='')
    dist_nanometer_show = Label(dist_frame, text='')
    dist_mile_show = Label(dist_frame, text='')
    dist_yard_show = Label(dist_frame, text='')
    dist_foot_show = Label(dist_frame, text='')
    dist_inch_show = Label(dist_frame, text='')    
    
    def click_dist():
        nonlocal dist_meter_show
        nonlocal dist_kilometer_show
        nonlocal dist_centimeter_show
        nonlocal dist_milimeter_show
        nonlocal dist_micrometer_show
        nonlocal dist_nanometer_show
        nonlocal dist_mile_show
        nonlocal dist_yard_show
        nonlocal dist_foot_show
        nonlocal dist_inch_show
        
        dist_meter_show.grid_forget()
        dist_kilometer_show.grid_forget()
        dist_centimeter_show.grid_forget()
        dist_milimeter_show.grid_forget()
        dist_micrometer_show.grid_forget()
        dist_nanometer_show.grid_forget()
        dist_mile_show.grid_forget()
        dist_yard_show.grid_forget()
        dist_foot_show.grid_forget()
        dist_inch_show.grid_forget()
        
        dist_meter_show = Label(dist_frame, text=converters.distance(choose_dist.get(), float(dist_input.get()))[0])
        dist_kilometer_show = Label(dist_frame, text=converters.distance(choose_dist.get(), float(dist_input.get()))[1])
        dist_centimeter_show = Label(dist_frame, text=converters.distance(choose_dist.get(), float(dist_input.get()))[2])
        dist_milimeter_show = Label(dist_frame, text=converters.distance(choose_dist.get(), float(dist_input.get()))[3])
        dist_micrometer_show = Label(dist_frame, text=converters.distance(choose_dist.get(), float(dist_input.get()))[4])
        dist_nanometer_show = Label(dist_frame, text=converters.distance(choose_dist.get(), float(dist_input.get()))[5])
        dist_mile_show = Label(dist_frame, text=converters.distance(choose_dist.get(), float(dist_input.get()))[6])
        dist_yard_show = Label(dist_frame, text=converters.distance(choose_dist.get(), float(dist_input.get()))[7])
        dist_foot_show = Label(dist_frame, text=converters.distance(choose_dist.get(), float(dist_input.get()))[8])
        dist_inch_show = Label(dist_frame, text=converters.distance(choose_dist.get(), float(dist_input.get()))[9])
        
        dist_meter_show.grid(row=2, column=1, sticky=W)
        dist_kilometer_show.grid(row=3, column=1, sticky=W)
        dist_centimeter_show.grid(row=4, column=1, sticky=W)
        dist_milimeter_show.grid(row=5, column=1, sticky=W)
        dist_micrometer_show.grid(row=6, column=1, sticky=W)
        dist_nanometer_show.grid(row=7, column=1, sticky=W)
        dist_mile_show.grid(row=8, column=1, sticky=W)
        dist_yard_show.grid(row=9, column=1, sticky=W)
        dist_foot_show.grid(row=10, column=1, sticky=W)
        dist_inch_show.grid(row=11, column=1, sticky=W)
        
        dist_input.delete(0, END)
        
    dist_calc = Button(dist_frame, text='Convert', command=click_dist)
    
    dist_frame.grid(row=1, column=0, columnspan=3, padx=5)
    dist_input.grid(row=0, column=0, columnspan=2, padx=5)
    dist_calc.grid(row=0, column=2, padx=10)
    dist_meter.grid(row=2, column=0, sticky=W)
    dist_kilometer.grid(row=3, column=0, sticky=W)
    dist_centimeter.grid(row=4, column=0, sticky=W)
    dist_milimeter.grid(row=5, column=0, sticky=W)
    dist_micrometer.grid(row=6, column=0, sticky=W)
    dist_nanometer.grid(row=7, column=0, sticky=W)
    dist_mile.grid(row=8, column=0, sticky=W)
    dist_yard.grid(row=9, column=0, sticky=W)
    dist_foot.grid(row=10, column=0, sticky=W)
    dist_inch.grid(row=11, column=0, sticky=W)
    
    
dist_confirm = Button(dist, text='Choose', command=dist_choosen)


# Weight tab section
weig_units = ['Kilograms', 'Grams', 'Miligrams', 'Metric ton', 'Long ton', 'Short ton', 'Pounds', 'Ounces', 'Carrats']
choose_weig = StringVar()
choose_weig.set(weig_units[0])

weig_label = Label(weig, text='Choose unit:')
weig_choose = OptionMenu(weig, choose_weig, *weig_units)

def weig_choosen():
    weig_frame = LabelFrame(weig, text='Weight')
    weig_input = Entry(weig_frame, width=50, borderwidth=5)
    weig_kilograms = Label(weig_frame, text='Kilograms = ')
    weig_grams = Label(weig_frame, text='Grams =')
    weig_miligrams = Label(weig_frame, text='Miligrams =')
    weig_metric_ton = Label(weig_frame, text='Metric ton =')
    weig_long_ton = Label(weig_frame, text='Long ton =')
    weig_short_ton = Label(weig_frame, text='Short ton =')
    weig_pounds = Label(weig_frame, text='Pounds =')
    weig_ounces = Label(weig_frame, text='Ounces =')
    weig_carrats = Label(weig_frame, text='Carrats =')
    
    weig_kilograms_show = Label(weig_frame, text='')
    weig_grams_show = Label(weig_frame, text='')
    weig_miligrams_show = Label(weig_frame, text='')
    weig_metric_ton_show = Label(weig_frame, text='')
    weig_long_ton_show = Label(weig_frame, text='')
    weig_short_ton_show = Label(weig_frame, text='')
    weig_pounds_show = Label(weig_frame, text='')
    weig_ounces_show = Label(weig_frame, text='')
    weig_carrats_show = Label(weig_frame, text='')   
    
    def click_weig():
        nonlocal weig_kilograms_show
        nonlocal weig_grams_show
        nonlocal weig_miligrams_show
        nonlocal weig_metric_ton_show
        nonlocal weig_long_ton_show
        nonlocal weig_short_ton_show
        nonlocal weig_pounds_show
        nonlocal weig_ounces_show
        nonlocal weig_carrats_show
        
        weig_kilograms_show.grid_forget()
        weig_grams_show.grid_forget()
        weig_miligrams_show.grid_forget()
        weig_metric_ton_show.grid_forget()
        weig_long_ton_show.grid_forget()
        weig_short_ton_show.grid_forget()
        weig_pounds_show.grid_forget()
        weig_ounces_show.grid_forget()
        weig_carrats_show.grid_forget()
        
        weig_kilograms_show = Label(weig_frame, text=converters.weight(choose_weig.get(), float(weig_input.get()))[0])
        weig_grams_show = Label(weig_frame, text=converters.weight(choose_weig.get(), float(weig_input.get()))[1])
        weig_miligrams_show = Label(weig_frame, text=converters.weight(choose_weig.get(), float(weig_input.get()))[2])
        weig_metric_ton_show = Label(weig_frame, text=converters.weight(choose_weig.get(), float(weig_input.get()))[3])
        weig_long_ton_show = Label(weig_frame, text=converters.weight(choose_weig.get(), float(weig_input.get()))[4])
        weig_short_ton_show = Label(weig_frame, text=converters.weight(choose_weig.get(), float(weig_input.get()))[5])
        weig_pounds_show = Label(weig_frame, text=converters.weight(choose_weig.get(), float(weig_input.get()))[6])
        weig_ounces_show = Label(weig_frame, text=converters.weight(choose_weig.get(), float(weig_input.get()))[7])
        weig_carrats_show = Label(weig_frame, text=converters.weight(choose_weig.get(), float(weig_input.get()))[8])
        
        weig_kilograms_show.grid(row=2, column=1, sticky=W)
        weig_grams_show.grid(row=3, column=1, sticky=W)
        weig_miligrams_show.grid(row=4, column=1, sticky=W)
        weig_metric_ton_show.grid(row=5, column=1, sticky=W)
        weig_long_ton_show.grid(row=6, column=1, sticky=W)
        weig_short_ton_show.grid(row=7, column=1, sticky=W)
        weig_pounds_show.grid(row=8, column=1, sticky=W)
        weig_ounces_show.grid(row=9, column=1, sticky=W)
        weig_carrats_show.grid(row=10, column=1, sticky=W)
        
        weig_input.delete(0, END)
        
    weig_calc = Button(weig_frame, text='Convert', command=click_weig)
    
    weig_frame.grid(row=1, column=0, columnspan=3, padx=5)
    weig_input.grid(row=0, column=0, columnspan=2, padx=5)
    weig_calc.grid(row=0, column=2, padx=10)
    weig_kilograms.grid(row=2, column=0, sticky=W)
    weig_grams.grid(row=3, column=0, sticky=W)
    weig_miligrams.grid(row=4, column=0, sticky=W)
    weig_metric_ton.grid(row=5, column=0, sticky=W)
    weig_long_ton.grid(row=6, column=0, sticky=W)
    weig_short_ton.grid(row=7, column=0, sticky=W)
    weig_pounds.grid(row=8, column=0, sticky=W)
    weig_ounces.grid(row=9, column=0, sticky=W)
    weig_carrats.grid(row=10, column=0, sticky=W)
    
       
weig_confirm = Button(weig, text='Choose', command=weig_choosen)


# Time tab section
tim_units = ['Seconds', 'Minutes', 'Hours', 'Days', 'Weeks', 'Months', 'Years']
choose_tim = StringVar()
choose_tim.set(tim_units[0])

tim_label = Label(tim, text='Choose unit:')
tim_choose = OptionMenu(tim, choose_tim, *tim_units)

def tim_choosen():
    tim_frame = LabelFrame(tim, text='Time')
    tim_input = Entry(tim_frame, width=50, borderwidth=5)
    tim_seconds = Label(tim_frame, text='Seconds = ')
    tim_minutes = Label(tim_frame, text='Minutes =')
    tim_hours = Label(tim_frame, text='Hours =')
    tim_days = Label(tim_frame, text='Days =')
    tim_weeks = Label(tim_frame, text='Weeks =')
    tim_months = Label(tim_frame, text='Months =')
    tim_years = Label(tim_frame, text='Years =')
    
    tim_seconds_show = Label(tim_frame, text='')
    tim_minutes_show = Label(tim_frame, text='')
    tim_hours_show = Label(tim_frame, text='')
    tim_days_show = Label(tim_frame, text='')
    tim_weeks_show = Label(tim_frame, text='')
    tim_months_show = Label(tim_frame, text='')
    tim_years_show = Label(tim_frame, text='')
 
    
    def click_tim():
        nonlocal tim_seconds_show
        nonlocal tim_minutes_show
        nonlocal tim_hours_show
        nonlocal tim_days_show
        nonlocal tim_weeks_show
        nonlocal tim_months_show
        nonlocal tim_years_show

        
        tim_seconds_show.grid_forget()
        tim_minutes_show.grid_forget()
        tim_hours_show.grid_forget()
        tim_days_show.grid_forget()
        tim_weeks_show.grid_forget()
        tim_months_show.grid_forget()
        tim_years_show.grid_forget()

        
        tim_seconds_show = Label(tim_frame, text=converters.time(choose_tim.get(), float(tim_input.get()))[0])
        tim_minutes_show = Label(tim_frame, text=converters.time(choose_tim.get(), float(tim_input.get()))[1])
        tim_hours_show = Label(tim_frame, text=converters.time(choose_tim.get(), float(tim_input.get()))[2])
        tim_days_show = Label(tim_frame, text=converters.time(choose_tim.get(), float(tim_input.get()))[3])
        tim_weeks_show = Label(tim_frame, text=converters.time(choose_tim.get(), float(tim_input.get()))[4])
        tim_months_show = Label(tim_frame, text=converters.time(choose_tim.get(), float(tim_input.get()))[5])
        tim_years_show = Label(tim_frame, text=converters.time(choose_tim.get(), float(tim_input.get()))[6])

        
        tim_seconds_show.grid(row=2, column=1, sticky=W)
        tim_minutes_show.grid(row=3, column=1, sticky=W)
        tim_hours_show.grid(row=4, column=1, sticky=W)
        tim_days_show.grid(row=5, column=1, sticky=W)
        tim_weeks_show.grid(row=6, column=1, sticky=W)
        tim_months_show.grid(row=7, column=1, sticky=W)
        tim_years_show.grid(row=8, column=1, sticky=W)

        
        tim_input.delete(0, END)
        
    tim_calc = Button(tim_frame, text='Convert', command=click_tim)
    
    tim_frame.grid(row=1, column=0, columnspan=3, padx=5)
    tim_input.grid(row=0, column=0, columnspan=2, padx=5)
    tim_calc.grid(row=0, column=2, padx=10)
    tim_seconds.grid(row=2, column=0, sticky=W)
    tim_minutes.grid(row=3, column=0, sticky=W)
    tim_hours.grid(row=4, column=0, sticky=W)
    tim_days.grid(row=5, column=0, sticky=W)
    tim_weeks.grid(row=6, column=0, sticky=W)
    tim_months.grid(row=7, column=0, sticky=W)
    tim_years.grid(row=8, column=0, sticky=W)
    
    
tim_confirm = Button(tim, text='Choose', command=tim_choosen)


# Displaing in Temperature tab
temp_label.grid(row=0, column=0, padx=5)
temp_choose.grid(row=0, column=1, padx=5)
temp_confirm.grid(row=0, column=2)

# Displaing in Distance tab
dist_label.grid(row=0, column=0, padx=5)
dist_choose.grid(row=0, column=1, padx=5)
dist_confirm.grid(row=0, column=2)

# Displaying in Weight tab
weig_label.grid(row=0, column=0, padx=5)
weig_choose.grid(row=0, column=1, padx=5)
weig_confirm.grid(row=0, column=2)

# Displaying in Time tab
tim_label.grid(row=0, column=0, padx=5)
tim_choose.grid(row=0, column=1, padx=5)
tim_confirm.grid(row=0, column=2)

tabs.add(temp, text='Temperature')
tabs.add(dist, text='Distance')
tabs.add(weig, text='Weight')
tabs.add(tim, text='Time')
exit_button = Button(root, text='Exit', command=root.quit)


exit_button.pack(anchor=SE, padx=5, pady=5)


root.mainloop()