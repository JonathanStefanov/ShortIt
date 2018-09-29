from django import forms

class ShortUrlGuestForm(forms.Form):
    longUrl = forms.URLField(label="", widget= forms.TextInput(attrs={'id':'url-shorter', 'placeholder' : 'Enter an URL'}))

class SignUpForm(forms.Form):
    username = forms.CharField(label="",max_length=50, widget= forms.TextInput(attrs={'placeholder' : 'Your Username', 'class' : 'sign'}))
    email = forms.EmailField(label="", widget= forms.TextInput(attrs={'placeholder' : 'Your Email Adress','class' : 'sign'}))
    passw = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder' : 'Your Password','class' : 'sign'}))
    #verify_passw = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder' : 'Verify Your Password','class' : 'sign'}))

    '''def clean_SignUpForm(self):
        #Verifies that the two passwords match
        passw = self.cleaned_data['passw']
        verify_passw = self.cleaned_data['verify_passw']
        if passw != verify_passw:
            raise forms.ValidationError("Please make sure the two passwords match")
        return passw, verify_passw'''

class SignInForm(forms.Form):
    username = forms.CharField(label="",max_length=50, widget= forms.TextInput(attrs={'placeholder' : 'Your Username', 'class' : 'sign'}))
    passw = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder' : 'Your Password','class' : 'sign'}))


class ShortUrlAuthForm(forms.Form):
    longUrl = forms.URLField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter an URL', 'class' : 'sign'}))
    customText = forms.CharField(label="", required=False ,widget=forms.TextInput(attrs={'placeholder': 'Custom Text (not required)', 'class' : 'sign'}))
