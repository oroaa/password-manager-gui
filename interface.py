import PySimpleGUI as sg
import pyperclip
import pwGenerator
from analysisGenerator import analyze_pw

# Define the window's contents
sg.theme('DarkGrey15')
sg.set_options(font=("Times", 20))

frameLayout = [[sg.Text("very weak", key="-STRENGTH-", text_color='#dc3545', font=("Times", 20, "bold"))]]
frameLayout2 = [[sg.Text("less than a second", key="-TIME-", text_color='#175ddc', font=("Times", 20, "bold"))]]

layout = [
    [sg.Text("Generate or Test Your Own Password!", font=("Times", 15, "bold"))],
    [sg.Input(key='-TEXTBOX-', do_not_clear=True, enable_events=True, border_width=5, pad=5, expand_x=True)],
    [sg.Button("Copy", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-COPY-"),
     sg.Button("Generate", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-GENERATE-")],
    [sg.Frame(title="Your password strength", layout=frameLayout, expand_x=True, font=("Times", 15)),
     sg.Frame(title="Estimated time to crack", font=("Times", 15), layout=frameLayout2, expand_x=True)],
    [sg.Text("Length", pad=((5, 10), (25, 0))),
     sg.Slider(border_width=3, expand_x=True, range=(1, 50), default_value=10, change_submits=True, size=(10, 15),
               orientation='h', key="-SLIDER-")],
    [sg.Text("Uppercase Letters"), sg.Push(), sg.Checkbox("", default=True, enable_events=True, key="-UPPER-")],
    [sg.Text("Lowercase Letters"), sg.Push(), sg.Checkbox("", default=True, enable_events=True, key="-LOWER-")],
    [sg.Text("Numbers"), sg.Push(), sg.Checkbox("", default=True, enable_events=True, key="-NUMBERS-")],
    [sg.Text("Symbols"), sg.Push(), sg.Checkbox("", default=False, enable_events=True, key="-SYMBOLS-")],
    [sg.Text("Whitespace"), sg.Push(), sg.Checkbox("", default=False, enable_events=True, key="-SPACE-")]
]

window = sg.Window("Password Generator", layout, size=(375, 425))

while True:
    event, values = window.read()

    if event == "-TEXTBOX-" or "-GENERATE-":
        if values["-TEXTBOX-"] != "":
            window["-STRENGTH-"].update(analyze_pw(values["-TEXTBOX-"])[0])
            window["-TIME-"].update(analyze_pw(values["-TEXTBOX-"])[1])

        match window["-STRENGTH-"].get():
            case "very weak":
                window["-STRENGTH-"].update(text_color='#dc3545')
            case "weak":
                window["-STRENGTH-"].update(text_color='#ffc107')
            case "good":
                window["-STRENGTH-"].update(text_color='#17a2b8')
            case "strong":
                window["-STRENGTH-"].update(text_color='#175ddc')

    if event == "-COPY-":
        pyperclip.copy(values["-TEXTBOX-"])

    if event == "-GENERATE-":
        pw = pwGenerator.generate_pw(int(values["-SLIDER-"]), values["-LOWER-"], values["-UPPER-"], values["-NUMBERS-"],
                                     values["-SYMBOLS-"], values["-SPACE-"])
        window["-TEXTBOX-"].update(pw)

    if event == sg.WIN_CLOSED:
        break

window.close()
