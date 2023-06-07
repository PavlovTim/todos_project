from django.contrib.auth.models import User

from .models import Todo


def create_initial_db():
    user_1 = User.objects.create_user(
        username='PopCrave',
        email='pop.crave@gmail.com',
        password='12345',
        is_active=True
    )
    user_2 = User.objects.create_user(
        username='SaeedDiCaprio',
        email='SaeedDiCaprio@gmail.com',
        password='12345',
        is_active=False
    )
    user_3 = User.objects.create_user(
        username='PopCulture2000s',
        email='PopCulture2000s@gmail.com',
        password='12345',
        is_active=True
    )

    Todo(
        name="Make noise",
        description="Making spherical sound to u'r neighbor",
        user=user_3
    ).save()
    Todo(
        name="Cleaning",
        description="3 hours of cleaning apartment",
        user=user_2
    ).save()
    Todo(
        name="Happy birthday",
        description="It's ur sister's birthday, so be happy",
        user=user_1
    ).save()
    Todo(
        name="my professor ",
        description="Teach some new models in django framework",
        user=user_2
    ).save()
    Todo(
        name="I just got home from watching it",
        description="I just got home from watching it and oh my god I literally have"
                    " zero notes it’s perfect through and through",
        user=user_1
    ).save()