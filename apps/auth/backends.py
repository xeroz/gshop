from django.contrib.auth.models import User


class EmailAuthBackend:

    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(email=username)
            success = user.check_password(password)
            if success:
                return user
        # This exception is not even defined in User, it gets generated by django
        except User.DoesNotExist:
            pass
        return None

    def get_user(self, uid):
        try:
            return User.objects.get(pk=uid)
        except:
            return None

    def list_wish(self):
        return 'sdkdsdsl'