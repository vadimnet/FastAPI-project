from models import UpdateAccountDTO
from models.Role import Role


class AdminUpdateAccountDTO(UpdateAccountDTO):
    role: Role