import dataclasses

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_num: str
    date_of_birth: dict[str]
    subject: str
    subject1: str
    hobbies: dict[str]
    file: str
    adress: str
    state: str
    city: str

test_user = User(
    first_name='Fedor',
    last_name='Lomovoy',
    email='fedyaosminog@ramb.com',
    gender='Other',
    mobile_num='1000000000',
    date_of_birth={'month_num': '9', 'month': 'October', 'year': '2000', 'day': '23'},
    subject='Maths',
    subject1='Computer Science',
    hobbies={'Sports': 'y', 'Reading': 'y', 'Music': 'n'},
    file='Octopus.jpg',
    adress='Moscow, Bulkina 65-39',
    state='Haryana',
    city='Panipat'
)
# print(test_user.hobbies)