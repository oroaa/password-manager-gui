import PySimpleGUI as sg
from analysisGenerator import analyze_pw
import pyperclip
import pwGenerator
import connector
import encrypt

def pwEntry():
    layout = [
        [sg.Text("Enter your Master Password", font=("Helvetica", 20, "bold"))],
        [sg.Input(key='-MP-', do_not_clear=False, enable_events=False, border_width=5, pad=5, expand_x=True, password_char='*')],
        [sg.Button("Submit", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-SUBMIT-", bind_return_key = True)]
    ]
    window = sg.Window("Authenticate", layout, size=(375, 135))
    while True:
        event, values = window.read()
        if event == '-SUBMIT-':
            if(encrypt.athorize(values['-MP-'], connector.getHashedPW())):
                masterPW = values['-MP-']
                deviceSecret = connector.getDeviceSecret()
                MK = encrypt.createMasterKey(masterPW, deviceSecret)
                break
            else:
                sg.Window("ERROR", [[sg.Text("Incorrect Entry. Try Again.", font=("Helvetica", 20, "bold"))],
                        [sg.OK(size = (19,1), )]]).read(close = True)
        elif event == sg.WIN_CLOSED:
            break
    window.close()
    return MK
def entryWindow():
    sg.theme('DarkGrey15')
    sg.set_options(font=("Verdona", 20))

    layout = [
        [sg.Text("Enter your Master Password", font=("Helvetica", 20, "bold"))],
        [sg.Input(key='-MP-', do_not_clear=False, enable_events=False, border_width=5, pad=5, expand_x=True, password_char='*')],
        [sg.Button("Submit", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-AUTHENTICATE-", bind_return_key = True)]
    ]

    window = sg.Window("Authenticate", layout, size=(375, 135))

    while True:
        event, values = window.read()
        if event == '-AUTHENTICATE-':
            if(encrypt.athorize(values['-MP-'], connector.getHashedPW())):
                deviceSecret = connector.getDeviceSecret()
                MK = encrypt.createMasterKey(values['-MP-'], deviceSecret)
                break
            else:
                sg.Window("ERROR", [[sg.Text("Incorrect Entry. Try Again.", font=("Helvetica", 20, "bold"))],
                        [sg.OK(size = (19,1), )]]).read(close = True)

        elif event == '-CANCEL-' or 'WIN_CLOSED':
            break

    window.close()
    mainWindow(MK)

def newWindow():
    sg.theme('DarkGrey15')
    sg.set_options(font=("Verdona", 20))

    layout = [
        [sg.Text("Create a Master Password", font=("Helvetica", 20, "bold"))],
        [sg.Input(key='-MP-', do_not_clear=False, enable_events=False, border_width=5, pad=5, expand_x=True, password_char='*')],
        [sg.Button("Create", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-CREATE-", bind_return_key = True)]
    ]

    window = sg.Window("Authenticate", layout, size=(375, 135))

    while True:
        event, values = window.read()
        if event == '-CREATE-':
            connector.createVault()
            connector.createAuth(values['-MP-'])
            deviceSecret = connector.getDeviceSecret()
            MK = encrypt.createMasterKey(values['-MP-'], deviceSecret)
            break  
        else:
            break

    window.close()
    mainWindow(MK)

def mainWindow(MK):
    sg.theme('DarkGrey15')
    sg.set_options(font=("Verdona", 20))
    data = connector.getAllEntries(MK)
    columns = ['NAME', 'URL', 'EMAIL', 'USERNAME', 'PASSWORD']
    layout = [[sg.Table(values = data[:][:], headings = columns,               
                        num_rows = 12, 
                        auto_size_columns = False, 
                        col_widths = [10, 10, 15, 10, 10],
                        font = ("Times", 15),
                        right_click_selects = True,
                        right_click_menu = ['The Vault', ['Copy Password', 'Copy Username', 'Delete', 'Exit']],
                        display_row_numbers = False,
                        justification = 'left',
                        key = '-TABLE-')], 
                [sg.Button("Add Item", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-ADDITEM-", pad = (10, 10)),
                sg.Button("Generate", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-GENERATOR-", pad = (10 , 10)),
                sg.Button("Lock", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-LOCK-", pad = (10, 10))]
    ]

    window = sg.Window("The Vault", layout, size=(700, 300))

    while True:
        event, values = window.read()
        if event == '-ADDITEM-':
            window.close()
            addItemWindow(MK)
        elif event == '-GENERATOR-':
            window.close()
            generatorWindow(MK)
        elif event == '-LOCK-':
            window.close()
            entryWindow()
        elif event == 'Copy Password':
            pw = pwEntry()
            pyperclip.copy(encrypt.decryptItem(pw, data[values['-TABLE-'][0]][6]))
        elif event == 'Copy Username':
            pw = pwEntry()
            pyperclip.copy(encrypt.decryptItem(pw, data[values['-TABLE-'][0]][5]))
        elif event == 'Delete':
            connector.deleteEntry(data[values['-TABLE-'][0]][0])
            window.close()
            mainWindow(MK)
        else: 
            break
    window.close()


def addItemWindow(MK):
    sg.theme('DarkGrey15')
    sg.set_options(font=("Times", 20))

    layout = [
        [sg.Text("Item Information", font=("Helvetica", 20, "bold"), justification = 'Center')],
        [sg.Text("Site Name"), sg.Text("*", text_color = "red")],
        [sg.Input(key='-NAME-', do_not_clear=False, enable_events=False, border_width=5, pad=5, expand_x=True)],
        [sg.Text("URL")],
        [sg.Input(key='-URL-', do_not_clear=False, enable_events=False, border_width=5, pad=5, expand_x=True)],
        [sg.Text("Email"), sg.Text("*", text_color = "red")],
        [sg.Input(key='-EMAIL-', do_not_clear=False, enable_events=False, border_width=5, pad=5, expand_x=True)],
        [sg.Text("Username")],
        [sg.Input(key='-USERNAME-', do_not_clear=False, enable_events=False, border_width=5, pad=5, expand_x=True)],
        [sg.Text("Password"), sg.Text("*", text_color = "red")],
        [sg.Input(key='-PW-', do_not_clear=False, enable_events=False, border_width=5, pad=5, expand_x=True, password_char = "*")],
        [sg.Button("Cancel", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-CANCEL-", pad = (10, 10)),
        sg.Button("Save", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-ENTER-", bind_return_key = True, pad = (10, 10))]
    ]

    window = sg.Window("Add Item", layout, size=(375, 487))

    while True:
        event, values = window.read()
        print(event, values)
        if event == '-ENTER-':
            if values['-NAME-'] and values['-EMAIL-'] and values['-PW-'] != "":
                MK = pwEntry()
                connector.addEntry(MK, values['-NAME-'], values['-EMAIL-'], values['-PW-'], values['-USERNAME-'], 
                    values['-URL-'])
                window.close()
                mainWindow(MK)
            else:
                sg.Window("ERROR", [[sg.Text("Please Fill Required Fields.", font=("Helvetica", 20, "bold"))],
                        [sg.OK(size = (19,1), )]]).read(close = True)
        elif event == '-CANCEL-':
            window.close()
            mainWindow(MK)
        else:
            break

    window.close()

def generatorWindow(MK):
    sg.theme('DarkGrey15')
    sg.set_options(font=("Times", 20))

    frameLayout = [[sg.Text("very weak", key="-STRENGTH-", text_color='#dc3545', font=("Times", 20, "bold"))]]
    frameLayout2 = [[sg.Text("less than a second", key="-TIME-", text_color='#175ddc', font=("Times", 20, "bold"))]]

    layout = [
        [sg.Text("Generate or Test Your Own Password!", font=("Times", 15, "bold"))],
        [sg.Input(key='-TEXTBOX-', do_not_clear=True, enable_events=True, border_width=5, pad=5, expand_x=True)],
        [sg.Button("Copy", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-COPY-"),
        sg.Button("Generate", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-GENERATE-", bind_return_key = True)],
        [sg.Button("Done", mouseover_colors=('#ffffff', '#2d2d2d'), expand_x=True, key="-DONE-")],
        [sg.Frame(title="Your password strength", layout=frameLayout, expand_x=True, font=("Times", 15)),
        sg.Frame(title="Estimated time to crack", font=("Times", 15), layout=frameLayout2, expand_x=True)],
        [sg.Text("Length", pad=((5, 10), (25, 0))),
        sg.Slider(border_width=3, expand_x=True, range=(1, 50), default_value=10, change_submits=True, size=(10, 15),
                orientation='h', key="-SLIDER-")],
        [sg.Text("Uppercase Letters"), sg.Push(), sg.Checkbox("", default=True, enable_events=True, key="-UPPER-")],
        [sg.Text("Lowercase Letters"), sg.Push(), sg.Checkbox("", default=True, enable_events=True, key="-LOWER-")],
        [sg.Text("Numbers"), sg.Push(), sg.Checkbox("", default=True, enable_events=True, key="-NUMBERS-")],
        [sg.Text("Symbols"), sg.Push(), sg.Checkbox("", default=False, enable_events=True, key="-SYMBOLS-")],
        [sg.Text("Whitespace"), sg.Push(), sg.Checkbox("", default=False, enable_events=True, key="-SPACE-")],
    ]

    window = sg.Window("Password Generator", layout, size=(375, 465))

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
        elif event == "-GENERATE-":
            pw = pwGenerator.generate_pw(int(values["-SLIDER-"]), values["-LOWER-"], values["-UPPER-"], values["-NUMBERS-"],
                                        values["-SYMBOLS-"], values["-SPACE-"])
            window["-TEXTBOX-"].update(pw)
        elif event == "-DONE-":
            window.close()
            mainWindow(MK)
        elif event == sg.WIN_CLOSED:
            break

    window.close()

if connector.newOrOld() == []:
    newWindow()
else:
    entryWindow()
