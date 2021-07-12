from django import forms


class OrderForm(forms.Form):  # Создаётся форма как класс
    name = forms.CharField(max_length=200,
                           required=False,  # Делает поле необязательным для заполнения
                           widget=forms.TextInput(attrs={'class': 'css_input'})  # Добавляет css-стили поля
                           )  # Поле формы
    phone = forms.CharField(max_length=200)  # Поле формы
