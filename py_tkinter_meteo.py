import tkinter as tk
from tkinter import StringVar
from sense_emu import SenseHat


hat = SenseHat()
main_window = tk.Tk()

class MeteoApp():
    def __init__(self, master):
        self.master = master
        self.master.title("Python METEO")
        self.master.geometry("600x400")


        self.lbl_temperature_label = tk.Label(self.master,
                                    text="Temperatura zraka",
                                    font=("Segoe UI", 15))
        self.lbl_temperature_label.grid(row=0, column=0, padx=15,pady=20, sticky="e")
        self.lbl_temperature_var = tk.StringVar()
        self.lbl_temperature = tk.Label(self.master,
                                    textvariable=self.lbl_temperature_var,
                                    font=("Segoe UI", 15))
        self.lbl_temperature.grid(row=0, column=1, padx=15,pady=20, sticky="e")


        self.lbl_humidity_label = tk.Label(self.master,
                                    text="Vlaznost zraka",
                                    font=("Segoe UI", 15))
        self.lbl_humidity_label.grid(row=1, column=0, padx=15,pady=20,sticky="e")
        self.lbl_humidity_var = tk.StringVar()
        self.lbl_humidity = tk.Label(self.master,
                                    textvariable=self.lbl_humidity_var,
                                    font=("Segoe UI", 15))
        self.lbl_humidity.grid(row=1, column=1, padx=15,pady=20,sticky="e")


        self.lbl_pressure_label = tk.Label(self.master,
                                    text="Tlak zraka",
                                    font=("Segoe UI", 15))
        self.lbl_pressure_label.grid(row=2, column=0, padx=15,pady=20,sticky="e")
        self.lbl_pressure_var = tk.StringVar()
        self.lbl_pressure = tk.Label(self.master,
                                    textvariable=self.lbl_pressure_var,
                                    font=("Segoe UI", 15))
        self.lbl_pressure.grid(row=2, column=1, padx=15,pady=20,sticky="e")

        self.update_values()
        
    def update_values(self):
        temperature = round(hat.get_temperature(),2)
        pressure = round(hat.get_pressure(),2)
        humidity = round(hat.get_humidity(),2)

        self.lbl_humidity_var.set(f"{str(humidity)} %")
        self.lbl_temperature_var.set(f"{str(temperature)} \u2103")
        self.lbl_pressure_var.set(f"{str(pressure)} hPa")

        self.master.after(500, self.update_values)

if __name__ == "__main__":
    window = tk.Tk()
    app = MeteoApp(window)
    
    window.mainloop()