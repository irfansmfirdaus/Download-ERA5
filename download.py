import cdsapi
from function import type_data, pressure_levels, date, area, download_surface, download_pressure

c = cdsapi.Client()

## DEFINE VARIABLE
typedata = type_data('pressure')      ## Select 'single' or 'pressure'
variable_pressure = [                 ## Select parameters which want to download --> comment the unwanted one
    #'divergence', 
    #'fraction_of_cloud_cover', 
    'geopotential',
    #'ozone_mass_mixing_ratio', 
    'potential_vorticity', 
    'relative_humidity',
    #'specific_cloud_ice_water_content', 
    #'specific_cloud_liquid_water_content', 
    'specific_humidity',
    #'specific_rain_water_content', 
    #'specific_snow_water_content', 
    'temperature',
    'u_component_of_wind', 
    'v_component_of_wind', 
    'vertical_velocity',
    'vorticity']
variable_single = [                 ## Select parameters which want to download --> comment the unwanted one. Check full list variable in CDS Web
    '10m_u_component_of_wind', 
    '10m_v_component_of_wind', 
    '2m_temperature',
    'mean_sea_level_pressure', 
    'sea_surface_temperature', 
    'surface_pressure',
    'total_precipitation']
pressurelevel = pressure_levels(all)  ## If particular level, just write ['level1','level2','etc']

year = '2023'
month = '11'
day = date(27, 29)
areas = area(25, 75, -25, 150)
formats = 'netcdf' #or 'grib'
outputname = typedata+'_'+year+'_'+month+'_'+str(day[0])+'-'+str(day[-1])+'.nc'


## DOWNLOAD
download_surface(c, type, typedata, variable_single, year, month, day, areas, formats, outputname)
#download_pressure(c, type, typedata, variable_pressure, pressurelevel, year, month, day, areas, formats, outputname)