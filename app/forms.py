from django import forms

class HallTicketForm(forms.Form):
    hall_ticket_number = forms.CharField(max_length=10)


