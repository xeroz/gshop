from django.db import models


class CartQuerySet(models.QuerySet):

    def new(self, user=None):
        print (user.authenticated())
        user_obj = None
        if user is not None:
            if user.authenticated():
                user_obj = user
        return self.create(user=user_obj)
