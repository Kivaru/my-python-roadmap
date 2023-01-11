import re

#*search and replace
#*patttern re.sub(pattern, replace, string, flags=0)

phone = "2004-959-559 # This is Phone Number"

#*? Delete Python-style comments

num = re.sub(r'#.*$', "", phone)

print("Phone number :", num)

#*? Remove anything other than digits

new_num = re.sub(r'\D', "", phone)
print("New Phone Number:", new_num)

