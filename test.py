from ApiConfiguration import ApiConfiguration

obj = ApiConfiguration(user = '', password = '')

# ListID = 19

# Create a new contact
#print obj.create_contact(email='dssgfdoer@yahoo.com.mx',name='ggmfdi')

# Create a new list contacts
#print obj.create_contactlist(address='yo@dharwinperez.com',name='Sparky-Children')
# Add contact to list
#print obj.add_contact_to_list( contact_id = obj.currentUser, list_id = obj.currentList )

# View a contactlist 

print obj.view_contactlist( contactslist_id = 3)