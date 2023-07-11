from django import forms
def validator_for_a(Svalue):
    if Svalue[0]=='a':
        return forms.ValidationError('First letter should not be a')
def validator_for_len(Svalue):
    if len(Svalue)<=5:
        return forms.ValidationError('Len is lessthan 5')
class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[validator_for_a,validator_for_len])
    Sage=forms.IntegerField()
    email=forms.EmailField(validators=[validator_for_a])        