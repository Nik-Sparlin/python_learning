# dictionaries are a type of data structures that lets us store information in key-value pairs
# we can refer to values by a unique key

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# we can access a specific key or value in different ways
# get will let you know when a value is not within dictionary with "None"
print(month_conversions["Nov"])
print(month_conversions.get("Dec"))
print(month_conversions.get("Mur"))

# you can also specify what you would like the get function to return when a value is not within the dictionary
print(month_conversions.get("Mur", "Not a valid key."))
