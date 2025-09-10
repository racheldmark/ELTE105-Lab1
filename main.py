basic.show_string("Rachel D'Amico Mark")
basic.pause(1000)
CurrentTemp = input.temperature()
CurrentTemp = (CurrentTemp * 9 / 5) + 32
basic.show_string("Temp: ")
basic.show_string("" + str((CurrentTemp)))
basic.show_string("°")

def on_forever():
    pass
basic.forever(on_forever)
