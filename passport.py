class Passport:
    def __init__(self, first_name, last_name, patronymic, date_of_birth, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.date_of_birth = date_of_birth
        self.passport_number = passport_number

    def __str__(self):
        return (f"Passport Info:\n"
                f"Name: {self.first_name} {self.patronymic} {self.last_name}\n"
                f"Date of Birth: {self.date_of_birth}\n"
                f"Passport Number: {self.passport_number}")


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, patronymic, date_of_birth, passport_number, foreign_passport_number):
        super().__init__(first_name, last_name, patronymic, date_of_birth, passport_number)
        self.foreign_passport_number = foreign_passport_number
        self.visas = []  

    def add_visa(self, country, visa_date, visa_expiry):
        visa = {
            "country": country,
            "visa_date": visa_date,
            "visa_expiry": visa_expiry
        }
        self.visas.append(visa)

    def remove_visa(self, country):
        self.visas = [visa for visa in self.visas if visa["country"] != country]

    def __str__(self):
        passport_info = super().__str__()
        visa_info = "\n".join(
            [f"Visa - Country: {visa['country']}, Date: {visa['visa_date']}, Expiry: {visa['visa_expiry']}" for visa in self.visas]
        )
        return (f"{passport_info}\n"
                f"Foreign Passport Number: {self.foreign_passport_number}\n"
                f"Visas:\n{visa_info if self.visas else 'No visas available'}")


passport = Passport("Ivan", "Petrenko", "Ivanovych", "1990-01-15", "AB123456")
print(passport)
print()
foreign_passport = ForeignPassport("Ivan", "Petrenko", "Ivanovych", "1990-01-15", "AB123456", "FP987654")
foreign_passport.add_visa("USA", "2023-06-01", "2025-06-01")
foreign_passport.add_visa("Germany", "2023-08-15", "2024-08-15")
print(foreign_passport)
print()
foreign_passport.remove_visa("USA")
print(foreign_passport)
