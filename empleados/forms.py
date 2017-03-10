from django import forms


def is_luhn_valid(cc):
    num = list(map(int, str(cc)))
    return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0


class EmpleadoForm(forms.Form):
    cedula = forms.CharField(label='Cedula', max_length=11)
    primer_nombre = forms.CharField(label='Primer nombre',max_length=150)
    segundo_nombre = forms.CharField(label='Segundo nombre',max_length=150)
    primer_apellido = forms.CharField(label='Primer apellido',max_length=150)
    segundo_apellido = forms.CharField(label='Segundo apellido',max_length=150)
    salario = forms.DecimalField(decimal_places=2, max_digits=10)

    def clean(self):
        cleaned_data = super(EmpleadoForm, self).clean()
        cedula = cleaned_data.get('cedula')
        salario = cleaned_data.get('salario')
        if cedula:
            if not is_luhn_valid(cedula) or '0'*len(cedula) == cedula:
                self.add_error('cedula', 'Por favor, introduzca una cedula valida.')
        if salario <= 0:
            self.add_error('salario', 'El salario no puede ser menor o igual que 0.')

        return cleaned_data
