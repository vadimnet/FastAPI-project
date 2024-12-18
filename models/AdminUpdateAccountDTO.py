from models import UpdateAccountDTO
from models.Role import Role
from pydantic import Field

class AdminUpdateAccountDTO(UpdateAccountDTO):
    role: Role = Field(description='Роль пользователя в системе. Разрешенные значения: user|admin')