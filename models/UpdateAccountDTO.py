from pydantic import BaseModel, Field, field_validator, ValidationError
from datetime import date

class UpdateAccountDTO(BaseModel):
    login: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=50)
    password_confirmation: str = Field(min_length=6, max_length=50)
    firstname: str = Field(min_length=1, max_length=50)
    lastname: str = Field(min_length=1, max_length=50)
    date_b: date = Field(description='Дата рождения в формате ГГГГ-ММ-ДД')

    @field_validator("password")
    @classmethod
    def validate_password(self, cls, values: str) -> str:
        if self.password != self.password_confirmation:
            raise ValidationError('Пароли должны совпадать')
        return values
    
    @field_validator("date_b")
    @classmethod
    def validate_date_of_birth(cls, values: date):
        if values and values >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return values