import enum
from pydantic import BaseModel

class GenderChoice(enum.Enum):
    male = "Male"
    female = "Female"
    def __str__(self) -> str:
        return self.value

class TrainingChoice(enum.Enum):
    trainer = "Trainer"
    personal = "Personal"
    def __str__(self) -> str:
        return self.value

class PlanChoice(enum.Enum):
    regular = "Regular"
    advance = "Advance"
    def __str__(self) -> str:
        return self.value

class BatchChoice(enum.Enum):
    morning = "Morning"
    evening = "Evening"
    def __str__(self) -> str:
        return self.value

class StatusChoice(enum.Enum):
    active = "Active"
    inactive = "Inactive"
    expired = "Expired"
    trial = "Trial"
    overdue = "Overdue"
    cancelled = "Cancelled"
    pending = "Pending"
    hold = "Hold"
    def __str__(self) -> str:
        return self.value

class MemberPublic(BaseModel):
    member_id: int
    member_name: str
    member_gender: GenderChoice
    member_phone: str

class MembersPublic(BaseModel):
    data: list[MemberPublic]