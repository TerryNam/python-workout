def get_rainfall():
   rainfall = {}
   while True:
       city_name = input('Enter city name: ')

       if not city_name:
           break
       rain_amount = input('Enter rain mm: ')
       rainfall[city_name] = rainfall.get(city_name,0) + int(rain_amount)

   for city, rain in rainfall.items():
        print(f'{city}: {rain}')

get_rainfall()