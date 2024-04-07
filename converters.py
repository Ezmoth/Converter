def temperature(unit, user_value):

    kelvin = 0.0
    celsius = 0.0
    fahrenheit = 0.0
    rankine = 0.0

    if unit == 'Celcius':
        kelvin = user_value + 273.15
        fahrenheit = (1.8 * user_value) + 32
        rankine = kelvin * 1.8
        return user_value, fahrenheit, kelvin, rankine

    elif unit == 'Farenheit':
        celsius = ((user_value - 32) * 5) / 9
        kelvin = celsius + 273.15
        rankine = kelvin * 1.8
        return celsius, user_value, kelvin, rankine
    
    elif unit == 'Kelvin':
        celsius = user_value - 273.15
        fahrenheit = (1.8 * celsius) + 32
        rankine = user_value * 1.8
        return celsius, fahrenheit, user_value, rankine
        
    elif unit == 'Rankine':
        kelvin = user_value / 1.8
        celsius = kelvin - 273.15
        fahrenheit = (1.8 * celsius) + 32
        return celsius, fahrenheit, kelvin, user_value


def weight(unit, user_value):
    kilograms = 0.0
    grams = 0.0
    miligrams = 0.0
    metric_ton = 0.0
    long_ton = 0.0
    short_ton = 0.0
    pounds =  0.0
    ounces = 0.0
    carrats = 0.0

    if unit == 'Kilograms':
        kilograms = user_value
        grams = kilograms * 1000
        miligrams = kilograms * 1000000
        metric_ton = kilograms / 1000
        pounds = kilograms * 2.2046244202
        long_ton = pounds / 2240
        short_ton = pounds / 2000
        ounces = pounds * 16
        carrats = kilograms * 5000
        
        return kilograms, grams, miligrams, metric_ton, pounds, long_ton, short_ton, ounces, carrats

    elif unit =='Grams':
        grams = user_value
        kilograms = grams / 1000
        miligrams = kilograms * 1000000
        metric_ton = kilograms / 1000
        pounds = kilograms * 2.2046244202
        long_ton = pounds / 2240
        short_ton = pounds / 2000
        ounces = pounds * 16
        carrats = kilograms * 5000
        
        return kilograms, grams, miligrams, metric_ton, pounds, long_ton, short_ton, ounces, carrats
    
    elif unit == 'Miligrams':
        miligrams = user_value
        kilograms = miligrams / 1000000
        grams = kilograms * 1000
        metric_ton = kilograms / 1000
        pounds = kilograms * 2.2046244202
        long_ton = pounds / 2240
        short_ton = pounds / 2000
        ounces = pounds * 16
        carrats = kilograms * 5000
        
        return kilograms, grams, miligrams, metric_ton, pounds, long_ton, short_ton, ounces, carrats

    elif unit == 'Metric ton':
        metric_ton = user_value
        kilograms = metric_ton * 1000
        grams = kilograms * 1000 
        miligrams = kilograms * 1000000
        pounds = kilograms * 2.2046244202
        long_ton = pounds / 2240
        short_ton = pounds / 2000
        ounces = pounds * 16
        carrats = kilograms * 5000
        
        return kilograms, grams, miligrams, metric_ton, pounds, long_ton, short_ton, ounces, carrats
            
    elif unit == 'Long ton':
        long_ton = user_value
        pounds = long_ton * 2240
        short_ton = pounds / 2000
        ounces = pounds * 16
        kilograms = pounds * 0.453592
        grams = kilograms * 1000 
        miligrams = kilograms * 1000000
        metric_ton = kilograms / 1000
        carrats = kilograms * 5000
        
        return kilograms, grams, miligrams, metric_ton, pounds, long_ton, short_ton, ounces, carrats
            
    elif unit == 'Short ton':
        short_ton = user_value
        pounds = short_ton * 2000
        long_ton = pounds / 2240
        ounces = pounds * 16
        kilograms = pounds * 0.453592
        grams = kilograms * 1000 
        miligrams = kilograms * 1000000
        metric_ton = kilograms / 1000
        carrats = kilograms * 5000
        
        return kilograms, grams, miligrams, metric_ton, pounds, long_ton, short_ton, ounces, carrats

    elif unit == 'Pounds':
        pounds = user_value
        long_ton = pounds / 2240
        short_ton = pounds / 2000
        ounces = pounds * 16
        kilograms = pounds * 0.453592
        grams = kilograms * 1000 
        miligrams = kilograms * 1000000
        metric_ton = kilograms / 1000
        carrats = kilograms * 5000
        
        return kilograms, grams, miligrams, metric_ton, pounds, long_ton, short_ton, ounces, carrats

    elif unit == 'Ounces':
        ounces = user_value
        pounds = ounces / 16
        long_ton = pounds / 2240
        short_ton = pounds / 2000
        kilograms = pounds * 0.453592
        grams = kilograms * 1000 
        miligrams = kilograms * 1000000
        metric_ton = kilograms / 1000
        carrats = kilograms * 5000
        
        return kilograms, grams, miligrams, metric_ton, pounds, long_ton, short_ton, ounces, carrats
            
    elif unit == 'Carrats':
        carrats = user_value
        grams = carrats / 5
        kilograms = grams / 1000
        miligrams = kilograms * 1000000
        metric_ton = kilograms / 1000
        pounds = kilograms * 2.2046244202
        long_ton = pounds / 2240
        short_ton = pounds / 2000
        ounces = pounds * 16
        
        return kilograms, grams, miligrams, metric_ton, pounds, long_ton, short_ton, ounces, carrats


def distance(unit, user_value):
    meters = 0.0
    kilometers = 0.0
    centimeters = 0.0
    milimeters = 0.0
    micrometers = 0.0
    nanometers = 0.0
    miles =  0.0
    yards = 0.0
    feets = 0.0
    inches = 0.0


    if unit == 'Meters':
        meters = user_value
        kilometers = meters / 1000
        centimeters = meters * 100
        milimeters = meters * 1000
        micrometers = meters * 1000000
        nanometers = meters * 1000000000   
        inches = centimeters / 2.54
        feets = inches / 12
        yards = inches / 36
        miles =  yards / 1760

        return meters, kilometers, centimeters, milimeters, micrometers, nanometers, miles, yards, feets, inches

    elif unit == 'Kilometers':
        kilometers = user_value
        meters = kilometers * 1000
        centimeters = meters * 100
        milimeters = meters * 1000
        micrometers = meters * 1000000
        nanometers = meters * 1000000000   
        inches = centimeters / 2.54
        feets = inches / 12
        yards = inches / 36
        miles =  yards / 1760

        return meters, kilometers, centimeters, milimeters, micrometers, nanometers, miles, yards, feets, inches

    elif unit == 'Centimeters':
        centimeters = user_value
        meters = centimeters / 100
        kilometers = meters / 1000            
        milimeters = meters * 1000
        micrometers = meters * 1000000
        nanometers = meters * 1000000000   
        inches = centimeters / 2.54
        feets = inches / 12
        yards = inches / 36
        miles =  yards / 1760
            
        return meters, kilometers, centimeters, milimeters, micrometers, nanometers, miles, yards, feets, inches

    elif unit == 'Milimeters':
        milimeters = user_value
        meters = milimeters / 1000
        kilometers = meters / 1000
        centimeters = meters * 100
        micrometers = meters * 1000000
        nanometers = meters * 1000000000   
        inches = centimeters / 2.54
        feets = inches / 12
        yards = inches / 36
        miles =  yards / 1760
            
        return meters, kilometers, centimeters, milimeters, micrometers, nanometers, miles, yards, feets, inches

    elif unit == 'Micrometers':
        micrometers = user_value
        meters = micrometers / 1000000
        kilometers = meters / 1000
        centimeters = meters * 100
        milimeters = meters * 1000
        nanometers = meters * 1000000000   
        inches = centimeters / 2.54
        feets = inches / 12
        yards = inches / 36
        miles =  yards / 1760

        return meters, kilometers, centimeters, milimeters, micrometers, nanometers, miles, yards, feets, inches

    elif unit == 'Nanometers':
        nanometers = user_value
        meters = nanometers / 1000000
        kilometers = meters / 1000
        centimeters = meters * 100
        milimeters = meters * 1000
        micrometers = meters * 1000000   
        inches = centimeters / 2.54
        feets = inches / 12
        yards = inches / 36
        miles =  yards / 1760

        return meters, kilometers, centimeters, milimeters, micrometers, nanometers, miles, yards, feets, inches

    elif unit == 'Miles':
        miles = user_value
        meters = miles * 1609.35
        kilometers = meters / 1000
        centimeters = meters * 100
        milimeters = meters * 1000
        micrometers = meters * 1000000
        nanometers = meters * 1000000000   
        inches = centimeters / 2.54
        feets = inches / 12
        yards = inches / 36

        return meters, kilometers, centimeters, milimeters, micrometers, nanometers, miles, yards, feets, inches

    elif unit == 'Yards':
        yards = user_value
        meters = yards * 0.9144
        kilometers = meters / 1000
        centimeters = meters * 100
        milimeters = meters * 1000
        micrometers = meters * 1000000
        nanometers = meters * 1000000000   
        inches = centimeters / 2.54
        feets = inches / 12
        miles =  yards / 1760

        return meters, kilometers, centimeters, milimeters, micrometers, nanometers, miles, yards, feets, inches

    elif unit == 'Foots':
        feets = user_value
        meters = feets * 0.3048
        kilometers = meters / 1000
        centimeters = meters * 100
        milimeters = meters * 1000
        micrometers = meters * 1000000
        nanometers = meters * 1000000000   
        inches = centimeters / 2.54
        yards = inches / 36
        miles =  yards / 1760

        return meters, kilometers, centimeters, milimeters, micrometers, nanometers, miles, yards, feets, inches

    elif unit == 'Inches':
        inches = user_value
        meters = inches * 0.0254
        kilometers = meters / 1000
        centimeters = meters * 100
        milimeters = meters * 1000
        micrometers = meters * 1000000
        nanometers = meters * 1000000000   
        feets = inches / 12
        yards = inches / 36
        miles =  yards / 1760

        return meters, kilometers, centimeters, milimeters, micrometers, nanometers, miles, yards, feets, inches


def time(unit, user_value):
    seconds = 0.0
    minutes = 0.0
    hours = 0.0
    days = 0.0
    weeks = 0.0
    months = 0.0
    years = 0.0

    if unit == 'Seconds':
        seconds = user_value
        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24
        weeks = days / 7
        months = minutes / 43830
        years = days / 365
        
        return seconds, minutes, hours, days, weeks, months, years

    elif unit == 'Minutes':
        minutes = user_value
        seconds = minutes * 60
        hours = minutes / 60
        days = hours / 24
        weeks = days / 7
        months = minutes / 43830
        years = days / 365
        
        return seconds, minutes, hours, days, weeks, months, years

    elif unit == 'Hours':
        hours = user_value
        minutes = hours * 60
        seconds = minutes * 60
        days = hours / 24
        weeks = days / 7
        months = minutes / 43830
        years = days / 365
    
        return seconds, minutes, hours, days, weeks, months, years

    elif unit == 'Days':
        days = user_value
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        weeks = days / 7
        months = minutes / 43830
        years = days / 365

        return seconds, minutes, hours, days, weeks, months, years

    elif unit == 'Weeks':
        weeks = user_value
        days = weeks * 7
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        months = minutes / 43830
        years = days / 365

        return seconds, minutes, hours, days, weeks, months, years

    elif unit == 'Months':
        months = user_value
        seconds = months * 2629800
        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24
        weeks = days / 7
        years = months / 12
        
        return seconds, minutes, hours, days, weeks, months, years

    elif unit == 'Years':
        years = user_value
        seconds = years * 31557600
        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24
        weeks = days / 7
        months = years * 12

        return seconds, minutes, hours, days, weeks, months, years