import tkinter

#window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=350,height=250)
window.config(padx=20,pady=20)
FONT=("Arial",11,"normal")

#labels and entries
weightLabel = tkinter.Label(text="Enter your weight (kg)",font=FONT,pady=5)
weightEntry = tkinter.Entry()
heightLabel = tkinter.Label(text="Enter your height (cm)",font=FONT,pady=5)
heightEntry = tkinter.Entry()
resultLabel = tkinter.Label(text="",font=FONT,pady=20)

#button and calculating
def buttonClick():
    try:
        weight = float(weightEntry.get())
        height = float(heightEntry.get())
        bmiValue = weight/(height/100)**2
        if bmiValue<=18.5:
            resultLabel.config(text=f"Your BMI is {round(bmiValue, 2)}. You are under weight.")
        elif bmiValue<24.9:
            resultLabel.config(text=f"Your BMI is {round(bmiValue, 2)}. You are normal weight.")
        elif bmiValue<29.9:
            resultLabel.config(text=f"Your BMI is {round(bmiValue, 2)}. You are over weight.")
        elif bmiValue<34.9:
            resultLabel.config(text=f"Your BMI is {round(bmiValue, 2)}. You are obese. (Class-I)")
        elif bmiValue<39.99:
            resultLabel.config(text=f"Your BMI is {round(bmiValue, 2)}. You are obese. (Class-II)")
        elif bmiValue>=40:
            resultLabel.config(text=f"Your BMI is {round(bmiValue, 2)}. You are extreme obese.")
    except:
        if weightEntry.get() == "" or heightEntry.get() == "":
            resultLabel.config(text="Enter both height and weight values.")
        else:
            resultLabel.config(text="Enter valid values.")

calculateButton = tkinter.Button(text="Calculate",font=FONT,command=buttonClick)

#packs
weightLabel.pack()
weightEntry.pack()
heightLabel.pack()
heightEntry.pack()
calculateButton.pack()
resultLabel.pack()

window.mainloop()