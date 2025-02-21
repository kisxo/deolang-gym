import enum

class UserRole(enum.Enum):
    admin = "Admin"
    staff = "Staff"
    member = "Member"
    def __str__(self) -> str:
        return self.value