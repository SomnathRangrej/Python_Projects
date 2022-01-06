import pywhatkit

# pywhatkit.sendwhatmsg('+911231231231', 'Message from pywhatkit', 19, 41)
# I have tested this with valid number in my contact, it works!

#sendwhatmsg_to_group is NOT working even with valid group_id, shared feedback with author
pywhatkit.sendwhatmsg_to_group('valid_group_id','Message from pywhatkit', 19, 55)

