import pywhatkit

contatos = ['+558598537885', '+558695567575', '+558699362080']

for item in contatos:
    pywhatkit.sendwhatmsg_instantly(item, 'Oi')