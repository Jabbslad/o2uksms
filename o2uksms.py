# Programatically sends an SMS through the O2 UK Website

# Requires following Python modules:-
# - mechanize
# - yaml

from mechanize import Browser
import yaml

contacts = yaml.load(open('contacts.yaml'))

print "Available contacts:-"
for contact in contacts:
	print  "%d: %s (%s)" % (contact, contacts[contact]['name'], contacts[contact]['number'])

chosen = raw_input('Select a contact no: ')
number = contacts[int(chosen)]['number']

br = Browser()
br.set_handle_robots(False)

br.open("https://o2.co.uk/login")
br.select_form(name='loginForm')

br['USERNAME'] = raw_input('Enter O2 username: ')
br['PASSWORD'] = raw_input('Enter O2 password: ')

br.submit()

br.open("http://sendtxt.o2.co.uk/sendtxt/action/compose")

br.select_form(name='sendtxtform')

br["compose.to"] = number
message = raw_input('Enter message: ')
br["compose.message"] = message
br["chars"] = str(444 - len(message))
br["total"] = str(len(message) / 160 + 1)

br.submit(id="send")