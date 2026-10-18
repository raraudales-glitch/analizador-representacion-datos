from django import forms
import re

class NumberAnalyzerForm(forms.Form):
    number_input = forms.CharField(
        label="Número de entrada",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1010, 42, FF'})
    )
    base_choice = forms.ChoiceField(
        label="Base de origen",
        choices=[(2, 'Binario (2)'), (8, 'Octal (8)'), (10, 'Decimal (10)'), (16, 'Hexadecimal (16)')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def clean(self):
        cleaned_data = super().clean()
        raw_val = cleaned_data.get('number_input')
        base = cleaned_data.get('base_choice')

        if not raw_val:
            raise forms.ValidationError("El campo de entrada no puede estar vacío.")

        raw_val = raw_val.strip()
        base_int = int(base)

        patterns = {
            2: r'^[0-1]+$',
            8: r'^[0-7]+$',
            10: r'^\d+$',
            16: r'^[0-9a-fA-F]+$'
        }

        if not re.match(patterns[base_int], raw_val):
            raise forms.ValidationError("El número contiene dígitos inválidos para la base seleccionada.")

        try:
            decimal_val = int(raw_val, base_int)
        except ValueError:
            raise forms.ValidationError("Formato de número inválido.")

        if decimal_val < 0 or decimal_val > 65535:
            raise forms.ValidationError("El valor convertido debe estar entre 0 y 65,535.")

        cleaned_data['decimal_val'] = decimal_val
        return cleaned_data


class TextAnalyzerForm(forms.Form):
    text_input = forms.CharField(
        label="Texto (máximo 20 caracteres)",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe algo...'})
    )

    def clean_text_input(self):
        text = self.cleaned_data.get('text_input')
        if not text:
            raise forms.ValidationError("El texto no puede estar vacío.")
        if len(text) > 20:
            raise forms.ValidationError("El texto excede los 20 caracteres permitidos.")
        return text