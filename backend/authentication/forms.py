from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage, BadHeaderError
from django.template.loader import get_template

from .models import User, Security
from structure.models import Agency


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

    connected_user = None

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
        try:
            subject, from_email, to = 'System Registration', 'reg_system@test.com', self.cleaned_data["security_email"]
            mail_context = {"confirm_url": "http://localhost:8000/api/security/confirm-account/{}/".format(str(user.uuid))}
            message = get_template('emails/registration.html').render(mail_context)
            email = EmailMessage(subject, message, from_email, [to])
            email.content_subtype = "html"
            email.send()

        except BadHeaderError as error:
            raise ValidationError("Unable to send email.")

        agency = Agency.objects.get(owner__user=self.connected_user)

        security.user = user
        security.agency = agency
        security.save()

        return security


class SupervisorCreationForm(forms.ModelForm):
    supervisor_email = forms.EmailField(label="Email")

    connected_user = None

    class Meta:
        model = Security
        fields = ('supervisor_email', )

    def clean_supervisor_email(self):
        supervisor_email = self.cleaned_data["supervisor_email"]
        if User.objects.filter(email=supervisor_email).exists():
            raise ValidationError("This email already exists, please verify.")
        return supervisor_email

    def save(self, commit=True):
        supervisor = super().save(commit=False)

        # create user for security purpose
        user = User(email=self.cleaned_data["supervisor_email"], is_active=False, is_supervisor=True)
        user.save()

        # send email to complete the registration process
        try:
            subject, from_email, to = 'System Registration', 'reg_system@test.com', self.cleaned_data["supervisor_email"]
            mail_context = {"confirm_url": "http://localhost:8000/api/supervisor/confirm-account/{}/".format(str(user.uuid))}
            message = get_template('emails/registration.html').render(mail_context)
            email = EmailMessage(subject, message, from_email, [to])
            email.content_subtype = "html"
            email.send()

        except BadHeaderError as error:
            raise ValidationError("Unable to send email.")

        agency = Agency.objects.get(owner__user=self.connected_user)

        supervisor.user = user
        supervisor.agency = agency
        supervisor.save()

        return supervisor

