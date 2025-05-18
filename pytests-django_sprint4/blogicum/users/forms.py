from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


User = get_user_model()


class MyUserForm(UserCreationForm):
    def clean(self):
        super().clean()

        send_mail(
            subject='Вы',
            message='Кто-то пытался опубликовать запись!',
            from_email='birthday_form@acme.not',
            recipient_list=['admin@acme.not'],
            fail_silently=True,
        )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
