from django import forms
from cars.models import Car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car        
        fields = '__all__'  # Use all fields from the Car model
        labels = {
            'model': 'Modelo',
            'brand': 'Marca',
            'factory_year': 'Ano de Fabricação',
            'model_year': 'Ano do Modelo',
            'plate': 'Placa',
            'value': 'Valor',
            'photo': 'Foto'
        }
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value',"O valor mínimo do carro deve ser de R$10.000")
        return value        
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1950:
            self.add_error('factory_year', "O ano mínimo de fabricação é 1950")
        return factory_year