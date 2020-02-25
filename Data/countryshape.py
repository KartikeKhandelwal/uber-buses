import copyshapes
copyshapes.filter_file(
    lambda x: x.GetField('REGION') == 150,
    'TM_WORLD_BORDERS-0.3.shp', 'EUROPE.shp'
)