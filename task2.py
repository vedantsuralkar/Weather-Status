


from tkinter import *
from requests import *


root = Tk()
root.title("Weather Forecasting app")
root.geometry("700x500+222+122")
f=("Calibri", 25, "bold")
root.config(bg="lightblue")


def gi():
    try:
        city=city_entry.get()
        

        api_key="4e9bd239db834b93bb6170448241507" 
	
        url=f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        res=get(url)
        data=res.json()

        
        lat=data['location']['lat']
        lon=data['location']['lon']
        temp_c=data['current']['temp_c']
        condition=data['current']['condition']['text']

        result_label.config(text=f"Latitude: {lat}\nLongitude: {lon}\nTemperature: {temp_c} °C\nCondition: {condition}")
    except Exception as e:
        result_label.config(text=f"Issue: {e}")



city_label=Label(root, text="Enter city name", font=f)
city_label.pack(pady=10)

city_entry=Entry(root, font=f)
city_entry.pack(pady=10)

get_weather_button=Button(root, text="Get Weather Updates", font=f, command=gi)
get_weather_button.pack(pady=20)



result_label=Label(root, text="", font=f)
result_label.pack(pady=20)

root.mainloop()
