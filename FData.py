from faker import Faker
import time
print("""

██╗    ██╗██╗  ██╗ ██████╗      █████╗ ███╗   ███╗    ██╗
██║    ██║██║  ██║██╔═══██╗    ██╔══██╗████╗ ████║    ██║
██║ █╗ ██║███████║██║   ██║    ███████║██╔████╔██║    ██║
██║███╗██║██╔══██║██║   ██║    ██╔══██║██║╚██╔╝██║    ██║
╚███╔███╔╝██║  ██║╚██████╔╝    ██║  ██║██║ ╚═╝ ██║    ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝
                                                         
By Qu3ti:)

""")
start = input('Apreta una tecla para empezar...')
fake = Faker()
fake.name()
fake.address()
fake.phone_number()
print("Nombre: "+fake.name())
print("Direccion: "+fake.address())
print("Mail: "+fake.email())
print("Numero: "+fake.phone_number())
time.sleep(100)
