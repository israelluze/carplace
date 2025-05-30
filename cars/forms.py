from django import forms
from cars.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=200, label='Modelo')
    brand = forms.ModelChoiceField(Brand.objects.all(), label='Marca')
    factory_year = forms.IntegerField(label='Ano de Fabricação')
    model_year = forms.IntegerField(label='Ano do Modelo')
    plate = forms.CharField(max_length=10, label='Placa')
    value = forms.FloatField(label='Valor')
    photo = forms.ImageField(required=False, label='Foto')
    
    def save(self, commit=True):
        car = Car(
            model=self.cleaned_data['model'],
            brand=self.cleaned_data['brand'],
            factory_year=self.cleaned_data['factory_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            value=self.cleaned_data['value'],
            photo=self.cleaned_data.get('photo', None)
        )
        car.save()
        return car