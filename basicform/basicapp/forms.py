from django import forms
from django.core import validators

class FormName(forms.Form):
    # def check_for_z(value):
    #     if value[0].lower() != 'z':
    #         raise forms.ValidationError("Need to start with the z")

    # name = forms.CharField( validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="enter your email", required=False)
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=True,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)]
    #                              )
    
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email != vemail:
            raise forms.ValidationError("Make sure email match")
    
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher