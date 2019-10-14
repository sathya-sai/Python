import re
import datetime
text = " Hello <<Name>>,We have your fullname as <<FullName>> in our system.Your contact number is 91-xxxxxxxxxx Please let us know in case of any Clarification.Thank You BridgeLabz XX/XX/XXXX."
name = str(input("Enter the name"))
result = re.sub(r"<<Name>>", name, text)
fn = str(input("Enter the full name"))
result = re.sub(r"<<FullName>>", fn, result)
phno = input("Enter your Phone No")
result = re.sub(r"xxxxxxxxxx", phno, result)
date = datetime.date.today()
replace_date = str(date)
result = re.sub("XX/XX/XXXX", replace_date, result)
print(result)
