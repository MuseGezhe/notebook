from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, ValidationError, FileField
from wtforms.validators import Length, Regexp, EqualTo, DataRequired

from App.models import User

# 从WTForms中定义一个集成Form的类，可以生成登录页面不用写模板，每个字段相当于一个html标签
class RegistrationForm(Form):
    # Regexp 验证函数，确保 username 字段只包含字母、数字、下划线和点号
    name = StringField('name', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
    'name must have only letters, ''numbers, dots or underscores')])
    # 验证两个密码字段中的值是否一致，这种验证可使用WTForms 提供的另一验证函数实现，即 EqualTo
    pwd = PasswordField('pwd', validators=[DataRequired(), EqualTo('repwd', message='Passwords must match.')])
    repwd = PasswordField('repwd', validators=[DataRequired()])
    pic = FileField('pic',validators=[DataRequired()])
    submit = SubmitField('reg')


    # 如果表单类中定义了以validate_ 开头且后面跟着字段名的方法，这个方法就和常规的验证函数一起调用
    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            # 自定义的验证函数要想表示验证失败，可以抛出 ValidationError 异常，其参数就是错误消息。
            raise ValidationError('name already in use.')


class UpdateForm(Form):
    pwd = PasswordField('pwd', validators=[DataRequired(), EqualTo('repwd', message='Passwords must match.')])
    repwd = PasswordField('repwd', validators=[DataRequired()])
    pic = FileField('pic', validators=[DataRequired()])
    submit = SubmitField('update')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('name already in use.')