from django import forms

from .models import Ranking

class RankingForm(forms.ModelForm):

    class Meta:
        model = Ranking
        fields = ('ranking_name','ranking_num')