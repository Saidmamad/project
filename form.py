from django import forms
from tours.models import Tour



class SearchTourForm(forms.ModelForm):
    class Meta:
        model = Tour
        # fields = ('Type','Destination', 'StartDate', 'Available') #Country
        exclude = ('Exclusions', )
