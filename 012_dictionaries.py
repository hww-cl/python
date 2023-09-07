# Creating dictionary
# keys should be unique
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar" :"March", 
    "Apr": "April",
    "May": "May",
    "Jun": "June",
     "Jul": "July",
      "Aug": "August",
      "Sep":"September",
      "Oct":"October",
      "Nov":"November",
      "Dec":"December"
}

print(monthConversions) # {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April', 'May': 'May', 'Jun': 'June', 'Jul': 'July', 'Aug': 'August', 'Sep': 'September', 'Oct': 'October', 'Nov': 'November', 'Dec': 'December'}

print(monthConversions["Nov"]) # November
print(monthConversions.get('Dec')) #December