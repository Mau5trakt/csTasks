from django import forms


class NewTaskForm(forms.Form):
    task = forms.CharField(
        label="Agregar Tarea",
        widget=forms.TextInput(
            attrs={'placeholder': "Nueva Tarea", "is_required": True, "class": "form-control form-control-lg"}
        )
    )