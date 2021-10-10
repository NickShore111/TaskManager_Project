from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_employee_number(value):
    if len(value) < 4:
        raise ValidationError(_("Invalid Employee ID Number."))
    else:
        try:
            valueAsNum = int(value)
        except ValueError:
            raise ValidationError(_("Employee ID requires 4 digits."))
