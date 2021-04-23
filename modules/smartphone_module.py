from ppadb.client import Client

import voice_assistant as assistant

adb = Client(host='127.0.0.1', port=5037)

def check_device_connected():
    devices = adb.devices()
    if len(devices) == 0:
        quit()
        return False
    else:
        return True, devices[0]

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
        print('I am unable to access you phone.')
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
#             device.shell('input keyevent KEYCODE_ENDCALL')
#         else:
#             print('I am unable to access you phone.')
#     except:
#         print('I am unable to access you phone.')