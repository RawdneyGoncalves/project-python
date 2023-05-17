from faker import Faker

fake = Faker()

def generate_fake_data():
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()

    return {'name': name, 'email': email, 'phone': phone}
