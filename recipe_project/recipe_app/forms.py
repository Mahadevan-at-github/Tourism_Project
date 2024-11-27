from .models import *

from django import forms


class UserForm(forms.ModelForm):


    class Meta:

      model = User
      fields = '__all__'

class TourismForm(forms.ModelForm):

    class Meta:

        model = Tourism
        fields = ['PlaceName','Description','State','District','Weather','Location_Link','Destination_Img','Destination_Img1','Destination_Img2','Destination_Img3']

        widgets = {
            'PlaceName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place Name'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'State': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'District': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District'}),
            'Weather': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Weather'}),
            'Location_Link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Location Link'}),
            'Destination_Img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'Destination_Img1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'Destination_Img2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'Destination_Img3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
