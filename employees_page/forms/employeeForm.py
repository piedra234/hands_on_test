from django.forms import Form, CharField, TextInput

class EmployeeForm(Form):
    id = CharField( widget=TextInput(attrs={'type':'number'}),required=False)
