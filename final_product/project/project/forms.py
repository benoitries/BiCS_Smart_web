from django import forms
    
class plugs(forms.Form):
    """Actions = [('on_off','On/Off'),
               ('info','Info')]
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=Actions, required=False, label='Action')
    """
    Actions = [('on_off_1','On/Off'),
               ('info_1','Info'),
               ('on_off_2','On/Off'),
               ('info_2','Info')]
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=Actions, required=False, label='')
    
    def clean_choice_field(self):
        data = self.cleaned_data['choice_field']
        return data
