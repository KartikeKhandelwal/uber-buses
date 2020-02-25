import countries

cc = countries.CountryChecker('TM_WORLD_BORDERS-0.3.shp')
print(cc.getCountry(countries.Point(49.7821, 3.5708)).iso)
print('test working')