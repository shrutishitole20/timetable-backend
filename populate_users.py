import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable_project.settings')
django.setup()

from django.contrib.auth.models import User

# List of 50 realistic users with Marathi-inspired names
users = [
    {'username': 'sanjay_patil', 'email': 'sanjay.patil@timetabler.com', 'first_name': 'Sanjay', 'last_name': 'Patil'},
    {'username': 'anita_deshmukh', 'email': 'anita.deshmukh@timetabler.com', 'first_name': 'Anita', 'last_name': 'Deshmukh'},
    {'username': 'rajesh_kulkarni', 'email': 'rajesh.kulkarni@timetabler.com', 'first_name': 'Rajesh', 'last_name': 'Kulkarni'},
    {'username': 'sunita_gadre', 'email': 'sunita.gadre@timetabler.com', 'first_name': 'Sunita', 'last_name': 'Gadre'},
    {'username': 'manoj_pawar', 'email': 'manoj.pawar@timetabler.com', 'first_name': 'Manoj', 'last_name': 'Pawar'},
    {'username': 'swati_shinde', 'email': 'swati.shinde@timetabler.com', 'first_name': 'Swati', 'last_name': 'Shinde'},
    {'username': 'vikas_gaikwad', 'email': 'vikas.gaikwad@timetabler.com', 'first_name': 'Vikas', 'last_name': 'Gaikwad'},
    {'username': 'neha_mohite', 'email': 'neha.mohite@timetabler.com', 'first_name': 'Neha', 'last_name': 'Mohite'},
    {'username': 'rahul_tambe', 'email': 'rahul.tambe@timetabler.com', 'first_name': 'Rahul', 'last_name': 'Tambe'},
    {'username': 'komal_salunke', 'email': 'komal.salunke@timetabler.com', 'first_name': 'Komal', 'last_name': 'Salunke'},
    {'username': 'ajay_kale', 'email': 'ajay.kale@timetabler.com', 'first_name': 'Ajay', 'last_name': 'Kale'},
    {'username': 'mrunal_sardesai', 'email': 'mrunal.sardesai@timetabler.com', 'first_name': 'Mrunal', 'last_name': 'Sardesai'},
    {'username': 'bhushan_shah', 'email': 'bhushan.shah@timetabler.com', 'first_name': 'Bhushan', 'last_name': 'Shah'},
    {'username': 'pooja_jadhav', 'email': 'pooja.jadhav@timetabler.com', 'first_name': 'Pooja', 'last_name': 'Jadhav'},
    {'username': 'kiran_sathe', 'email': 'kiran.sathe@timetabler.com', 'first_name': 'Kiran', 'last_name': 'Sathe'},
    {'username': 'priya_joshi', 'email': 'priya.joshi@timetabler.com', 'first_name': 'Priya', 'last_name': 'Joshi'},
    {'username': 'amit_chavan', 'email': 'amit.chavan@timetabler.com', 'first_name': 'Amit', 'last_name': 'Chavan'},
    {'username': 'deepa_more', 'email': 'deepa.more@timetabler.com', 'first_name': 'Deepa', 'last_name': 'More'},
    {'username': 'suresh_yadav', 'email': 'suresh.yadav@timetabler.com', 'first_name': 'Suresh', 'last_name': 'Yadav'},
    {'username': 'kavita_nair', 'email': 'kavita.nair@timetabler.com', 'first_name': 'Kavita', 'last_name': 'Nair'},
    {'username': 'rohit_bhosale', 'email': 'rohit.bhosale@timetabler.com', 'first_name': 'Rohit', 'last_name': 'Bhosale'},
    {'username': 'sneha_gore', 'email': 'sneha.gore@timetabler.com', 'first_name': 'Sneha', 'last_name': 'Gore'},
    {'username': 'nitin_deshpande', 'email': 'nitin.deshpande@timetabler.com', 'first_name': 'Nitin', 'last_name': 'Deshpande'},
    {'username': 'manisha_wagh', 'email': 'manisha.wagh@timetabler.com', 'first_name': 'Manisha', 'last_name': 'Wagh'},
    {'username': 'sachin_mane', 'email': 'sachin.mane@timetabler.com', 'first_name': 'Sachin', 'last_name': 'Mane'},
    {'username': 'rupa_thakur', 'email': 'rupa.thakur@timetabler.com', 'first_name': 'Rupa', 'last_name': 'Thakur'},
    {'username': 'ganesh_kadam', 'email': 'ganesh.kadam@timetabler.com', 'first_name': 'Ganesh', 'last_name': 'Kadam'},
    {'username': 'seema_pandit', 'email': 'seema.pandit@timetabler.com', 'first_name': 'Seema', 'last_name': 'Pandit'},
    {'username': 'anil_sawant', 'email': 'anil.sawant@timetabler.com', 'first_name': 'Anil', 'last_name': 'Sawant'},
    {'username': 'varsha_naik', 'email': 'varsha.naik@timetabler.com', 'first_name': 'Varsha', 'last_name': 'Naik'},
    {'username': 'pramod_shukla', 'email': 'pramod.shukla@timetabler.com', 'first_name': 'Pramod', 'last_name': 'Shukla'},
    {'username': 'rekha_patel', 'email': 'rekha.patel@timetabler.com', 'first_name': 'Rekha', 'last_name': 'Patel'},
    {'username': 'vikram_tawde', 'email': 'vikram.tawde@timetabler.com', 'first_name': 'Vikram', 'last_name': 'Tawde'},
    {'username': 'lata_shirke', 'email': 'lata.shirke@timetabler.com', 'first_name': 'Lata', 'last_name': 'Shirke'},
    {'username': 'devendra_ghag', 'email': 'devendra.ghag@timetabler.com', 'first_name': 'Devendra', 'last_name': 'Ghag'},
    {'username': 'nisha_bond', 'email': 'nisha.bond@timetabler.com', 'first_name': 'Nisha', 'last_name': 'Bond'},
    {'username': 'sunil_bhatt', 'email': 'sunil.bhatt@timetabler.com', 'first_name': 'Sunil', 'last_name': 'Bhatt'},
    {'username': 'archana_rao', 'email': 'archana.rao@timetabler.com', 'first_name': 'Archana', 'last_name': 'Rao'},
    {'username': 'hemant_shirsat', 'email': 'hemant.shirsat@timetabler.com', 'first_name': 'Hemant', 'last_name': 'Shirsat'},
    {'username': 'pallavi_veer', 'email': 'pallavi.veer@timetabler.com', 'first_name': 'Pallavi', 'last_name': 'Veer'},
    {'username': 'milind_datar', 'email': 'milind.datar@timetabler.com', 'first_name': 'Milind', 'last_name': 'Datar'},
    {'username': 'jyoti_karpe', 'email': 'jyoti.karpe@timetabler.com', 'first_name': 'Jyoti', 'last_name': 'Karpe'},
    {'username': 'ravi_landge', 'email': 'ravi.landge@timetabler.com', 'first_name': 'Ravi', 'last_name': 'Landge'},
    {'username': 'sangita_apte', 'email': 'sangita.apte@timetabler.com', 'first_name': 'Sangita', 'last_name': 'Apte'},
    {'username': 'dilip_vichare', 'email': 'dilip.vichare@timetabler.com', 'first_name': 'Dilip', 'last_name': 'Vichare'},
    {'username': 'asha_shetty', 'email': 'asha.shetty@timetabler.com', 'first_name': 'Asha', 'last_name': 'Shetty'},
    {'username': 'pravin_jagtap', 'email': 'pravin.jagtap@timetabler.com', 'first_name': 'Pravin', 'last_name': 'Jagtap'},
    {'username': 'usha_borse', 'email': 'usha.borse@timetabler.com', 'first_name': 'Usha', 'last_name': 'Borse'},
    {'username': 'naresh_patankar', 'email': 'naresh.patankar@timetabler.com', 'first_name': 'Naresh', 'last_name': 'Patankar'},
    {'username': 'shruti_shitole', 'email': 'shruti.shitole@timetabler.com', 'first_name': 'Shruti', 'last_name': 'Shitole'},
]

created = 0
skipped = 0

for u in users:
    if not User.objects.filter(username=u['username']).exists():
        User.objects.create_user(
            username=u['username'],
            email=u['email'],
            password='Timetabler@123',  # All test users share this password
            first_name=u['first_name'],
            last_name=u['last_name']
        )
        created += 1
    else:
        skipped += 1

print(f"✅ Done! {created} users created, {skipped} already existed.")
print("📝 All users have password: Timetabler@123")
