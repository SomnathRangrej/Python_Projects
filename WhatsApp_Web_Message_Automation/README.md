- Source link: https://levelup.gitconnected.com/automate-whatsapp-messages-with-python-instantly-3e08d6600612

- Module required: pip install pywhatkit

>>> dir(pywhatkit)
['__VERSION__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'ascii_art', 'cancel_shutdown', 'core', 'handwriting', 'image_to_ascii_art',
'info', 'mail', 'misc', 'open_web', 'playonyt', 'sc', 'search', 'send_hmail', 'send_mail', 'sendwhatmsg', 'sendwhatmsg_instantly', 'sendwhatmsg_to_group', 'sendwhats_image', 'show_history', 'shutdown', 'system',
 'take_screenshot', 'text_to_handwriting', 'whats']

>>> help(pywhatkit.sendwhatmsg)
Help on function sendwhatmsg in module pywhatkit.whats:

sendwhatmsg(phone_no: str, message: str, time_hour: int, time_min: int, wait_time: int = 15, tab_close: bool = False, close_time: int = 3) -> None
    Send a WhatsApp Message at a Certain Time

>>> pywhatkit.sendwhatmsg('+911231231231', 'Message from pywhatkit', 19, 41)
In 48 Seconds WhatsApp will open and after 15 Seconds Message will be Delivered!
>>> pywhatkit.sendwhatmsg('+911231231231', 'Message from pywhatkit', 19, 43)
In 9 Seconds WhatsApp will open and after 15 Seconds Message will be Delivered!
>>>

- It will open WhatsApp web on Chrome browser & search for the number in your contact list & type & send text message you entered

- Issue noted: If whatsApp web is already opened before execution of the code in one tab of the browser, module tries to open fresh tab of WhatsApp web & fail to open the page properly