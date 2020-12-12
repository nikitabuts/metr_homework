from flask_wtf import FlaskForm
from wtforms.validators import NumberRange, ValidationError, InputRequired
from wtforms import FileField, IntegerField, FloatField

def filename_check(sub: str='.txt'):
    message: str = f'Файл должен иметь расширение {sub}'
    def _filename_check(field):
        if str(field.data.filename).find(sub) == -1:
            raise ValidationError(message)
        return _filename_check

class Form(FlaskForm):
    file = FileField(validators=filename_check(".txt"))
    conf_level = FloatField(
        validators=[
            NumberRange(min=0.00000000001, max=0.9999999999999, message='Значение должно быть больше 0.00000000001 и меньше 0.9999999999999')
        ]
    )