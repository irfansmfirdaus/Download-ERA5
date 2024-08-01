import cdsapi
c = cdsapi.Client()

def type_data(type):
    '''
    Choosing of single level (surface level) or pressure level
    '''
    if type == 'single':
        return 'reanalysis-era5-single-levels'
    elif type == 'pressure':
        return 'reanalysis-era5-pressure-levels'

def pressure_levels(all):
    '''
    'all' means all pressure level that ERA5 provided
    '''
    list_pressure = ['1', '2', '3', '5', '7', '10', '20', '30', '50', '70', '100', '125', '150', '175', '200',
            '225', '250', '300', '350', '400', '450', '500', '550', '600', '650', '700', '750', '775', '800', '825',
            '850', '875', '900', '925', '950', '975', '1000']
    return list_pressure

def date(day1, day2):
    '''
    return list of date
    '''
    output_list = []
    for i in range (day1, day2+1, 1):
        output_list.append(str(i).zfill(2))
    return output_list

def area(north, west, south, east):
    return [north, west, south, east]

def download_surface(c, type, typedata, variable_surface, year, month, day, areas, formats, outputname):
    c.retrieve(
        typedata,
        {
        'product_type': 'reanalysis',
        'variable': variable_surface,
        'year': year,
        'month': month,
        'day': day,
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': areas,
        'format': formats,
        },
        outputname)
    return print('Download '+str(outputname))

def download_pressure(c, type, typedata, variable_pressure, pressurelevel, year, month, day, areas, formats, outputname):
    c.retrieve(
        typedata,
        {
        'product_type': 'reanalysis',
        'variable': variable_pressure,
        'pressure_level': pressurelevel,
        'year': year,
        'month': month,
        'day': day,
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': areas,
        'format': formats,
        },
        outputname)
    return print('Download '+str(outputname))