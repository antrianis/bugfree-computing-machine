import re
def validPhoneNumber(phoneNumber):
    return not re.match(r'^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$', phoneNumber) == None
