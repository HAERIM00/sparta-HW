class Profile:
    def set_profile(self, set_profile):
        self.name = set_profile['name']
        self.gender = set_profile['gender']
        self.birthday = set_profile['birthday']
        self.age = set_profile['age']
        self.phone = set_profile['phone']
        self.email = set_profile['email']

    def get_name(self):
        return f"{self.name}"

    def get_gender(self):
        return f"{self.gender}"

    def get_birthday(self):
        return f"{self.birthday}"

    def get_age(self):
        return f"{self.age}"

    def get_phone(self):
        return f"{self.phone}"

    def get_email(self):
        return f"{self.email}"

profile = Profile()
profile.set_profile({
    "name": "lee",
    "gender": "man",
    "birthday": "01/01",
    "age": 32,
    "phone": "01012341234",
    "email": "python@sparta.com",
}
)
print(profile.get_name())
print(profile.get_gender())
print(profile.get_birthday())
print(profile.get_age())
print(profile.get_email())
