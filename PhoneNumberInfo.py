import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier




x = phonenumbers.parse("+917068320393", None)
print(x)
#To get time-zone of a number
print(timezone.time_zones_for_number(x))
gb_number = phonenumbers.parse("+447986123456", "GB")
print(timezone.time_zones_for_number(gb_number))

print(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL))
print(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164))

#You might want to get some information about the location that corresponds to a phone number. 
#The geocoder.area_description_for_number does this, when possible.
ch_number = phonenumbers.parse("+917068320393", "CH")
print(geocoder.description_for_number(ch_number, "en"))

#For mobile numbers in some countries, you can also find out information about which carrier originally owned a phone number.
ro_number = phonenumbers.parse("+917000569874", "RO")
print(carrier.name_for_number(ro_number, "en"))


text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am."
for match in phonenumbers.PhoneNumberMatcher(text, "US"):
    print(match)
