from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from annonces.models import UserProfile, Annonce, Categorie


class ConnexionForm(forms.Form):
    """ Formulaire de connexion """

    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    

class Notation(forms.Form):
    """ Formulaire de notation d'une annonce """

    key = forms.IntegerField()
    mark = forms.IntegerField()


class UserForm(forms.ModelForm):
    """ Formulaire d'utilisateur """

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    """ Formulaire de profil """

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class AnnonceForm(forms.ModelForm):
    """ Formulaire pour l'ajout d'annonces """

    class Meta:
        model = Annonce
        fields = ('titre', 'categorie', 'descriptif')

class VoirAnnonces(forms.ModelForm):
    """ Formulaire pour la recherche d'annonces """

    class Meta:
        model = Annonce
        fields = ('categorie', 'ville')
