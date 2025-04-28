from django import forms

class ThyroidForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    age = forms.IntegerField(min_value=0)
    tsh = forms.FloatField(label='TSH (mIU/L)', min_value=0)
    t3 = forms.FloatField(label='T3 (ng/dL)', min_value=0)
    t4 = forms.FloatField(label='T4 (µg/dL)', min_value=0)
    thyroid_meds = forms.ChoiceField(
        label='Thyroid meds',
        choices=[('Yes', 'Yes'), ('No', 'No')]
    )
