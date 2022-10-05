from smtplib import SMTPException

from django import forms
from django.core.exceptions import ValidationError

import smtplib

from .models import User, Security


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'email',
            'is_resident',
            'is_security',
            'is_supervisor',
            'is_residenceadmin',
            'is_condoadmin',
            'is_agencyadmin',
            'is_platformadmin',
            'is_staff',
            'is_superuser',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SecurityCreationForm(forms.ModelForm):
    security_email = forms.EmailField(label="Email")

    class Meta:
        model = Security
        fields = ('security_email', )

    def clean_security_email(self):
        security_email = self.cleaned_data["security_email"]
        if User.objects.filter(email=security_email).exists():
            raise ValidationError("This email already exists, please verify.")
        return security_email

    def save(self, commit=True):
        security = super().save(commit=False)

        # create user for security purpose
        user = User(email=self.cleaned_data["security_email"], is_active=False, is_security=True)
        user.save()

        # send email to complete the registration process
        message = """From: From Person <{}>
        To: To Person <{}>
        MIME-Version: 1.0
        Content-type: text/html
        Subject: System Registration

        This is a registration email, to confirm the account clic on the link below \n
        http://localhost:8000/api/confirm_account/{}/

        <b>This is an automatically generated e-mail, please do not reply.</b>
        <h1>System Registration.</h1>
        """.format("reg_system@test.com", self.cleaned_data["security_email"], str(user.uuid))

        try:
            mail_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            mail_server.login("es3824@gmail.com", 'S@linas2011')
            mail_server.sendmail("reg_system@test.com", [self.cleaned_data["security_email"]], message)
            mail_server.close()
        except SMTPException as error:
            raise ValidationError("Unable to send email.")

        security.user = user
        security.save()

        return security

