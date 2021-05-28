# nested dictionary

data = {

    'myk' : {
        'first_name' : 'Mayank',
        'last_name' : 'Mishra'
    },

    'himzy' : {
        'first_name' : 'Himanshu',
        'last_name' : 'Chourasia'
    },

    'ram' : {
        'first_name' : 'shri ram',
        'last_name' : 'Raghuwanshi'
    },

    'ravan' : {
        'first_name' : 'lankapati',
        'last_name' : 'Shiv Bhakt'
    }
}

keys      = input("update username - ")
firstname = input( ' Mention first_name-')

data[keys]['first_name'] = firstname
print(data[keys])
