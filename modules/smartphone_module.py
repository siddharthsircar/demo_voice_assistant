from ppadb.client import Client
import voice_assistant as assistant
import cmd_module as cmd

adb = Client(host='127.0.0.1', port=5037)
mobile_ip = '192.168.29.187'

def connect_device():
    try:
        cmd.runcommand('adb devices')
        out = cmd.runcommand(f'adb connect {mobile_ip}:5555"')
        if 'already connected' in out or 'successfully connected' in out:
            assistant.speak('Mobile connected to home network.')
        else:
            assistant.speak('Unable to connect mobile device. You need to configure it manually.')
            assistant.speak('Sir, Do you need my assitance?')
            command = assistant.takeCommand()
            if 'yes' in command:
                connection_assitant()
            else:
                assistant.speak('Sir, Please make sure mobile is connected to the same network and try again manually.')
    except:
        assistant.speak('Unable to connect mobile device. You need to configure it manually.')
        assistant.speak('Sir, Do you need my assitance?')
        connection_assitant()

def connection_assitant():
    devices = adb.devices()
    assistant.speak('Sir, Please connect mobile device to the laptop using a usb cable')
    while len(devices)==0:
        assistant.speak('Trying to fetch connected devices')
        devices = adb.devices()
    device = devices[0]
    print(device)
    assistant.speak('Getting devide ip.')
    ipdetails = device.shell('ip addr show wlan0')
    if 'inet' in ipdetails:
        print(f'IP: {ipdetails}')
        ip = mobile_ip
        cmd.runcommand(f'adb connect {ip}:5555"')
        assistant.speak('Mobile connected to home network.')
    else:
        assistant.speak('Device not responding.')
        assistant.speak('Sir, Please make sure mobile is connected to the same network and try again manually.')

def check_device_connected():
    try:
        devices = adb.devices()
        if len(devices) == 0:
            quit()
            return False
        else:
            return True, devices[0]
    except:
        assistant.speak('Please check if your mobile is connected to the home interface.')

def get_contact_number(person):
    try:
        status, device = check_device_connected()
        if status:
            contactName = person.capitalize()
            # print('Contact Name: ' + contactName)
            number = device.shell(f'content query --uri content://com.android.contacts/data --where \'mimetype="vnd.android.cursor.item/phone_v2" and display_name="{contactName}"\' --projection data4 | cut -d= -f2')
            return number
        else:
            assistant.speak('I am unable to access you phone.')
            return 'none'
    except:
        return 'none'

def make_a_call(contactName):
    try:
        status, device = check_device_connected()
        assistant.speak('Getting contact details')
        number = get_contact_number(contactName)
        # print('Number is: ' + number)
        if 'none' in number or 'No result found.' not in number:
            if status:
                assistant.speak(f'Calling {contactName}')
                device.shell(f'am start -a android.intent.action.CALL -d tel:{number}')
                print('Call successful')
            else:
                assistant.speak('I am unable to access you phone.')
        else:
            assistant.speak('Unable to find contact details')
    except:
        assistant.speak('Unable to make the call')

def receive_call():
    try:
        status, device = check_device_connected()
        if status:
            assistant.speak('Picking up the call.')
            device.shell('input keyevent KEYCODE_CALL')
        else:
            assistant.speak('I am unable to access you phone.')
    except:
        assistant.speak('unable to pick up the call')

def disconnect_call():
    try:
        status, device = check_device_connected()
        if status:
            assistant.speak('Hanging up the call.')
            device.shell('input keyevent KEYCODE_ENDCALL')
        else:
            assistant.speak('I am unable to access you phone.')
    except:
        assistant.speak('unable to disconnect the call')

# def show_my_phone():
#     try:
#         status, device = check_device_connected()
#         if status:
#             os.system('cmd /c "scrcpy"')
#         else:
#             print('I am unable to access you phone.')
#     except:
#         print('I am unable to access you phone.')
