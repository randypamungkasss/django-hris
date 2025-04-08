from django.contrib.auth.mixins import LoginRequiredMixin

class LoginRequiredViewMixins(LoginRequiredMixin):
    login_url = "/login/"
    redirect_field_name = "next"

    class Meta:
        abstract = True