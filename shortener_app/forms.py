from django.forms import ModelForm
from shortener_app.models import AliasedUrl # Ensure this import is here

class AliasedUrlForm(ModelForm):
    class Meta:
        model = AliasedUrl
        fields = ['url']
