import enum

class GenderChoice(enum.Enum):
    male = "Male"
    female = "Female"

class TrainingChoice(enum.Enum):
    trainer = "Trainer"
    personal = "Personal"

class PlanChoice(enum.Enum):
    regular = "Regular"
    advance = "Advance"

class BatchChoice(enum.Enum):
    morning = "Morning"
    evening = "Evening"

class StatusChoice(enum.Enum):
    active = "Active"
    inactive = "Inactive"
    expired = "Expired"
    trial = "Trial"
    overdue = "Overdue"
    cancelled = "Cancelled"
    pending = "Pending"
    hold = "Hold"