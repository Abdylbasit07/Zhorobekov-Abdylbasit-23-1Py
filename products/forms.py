from django import forms


class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=3)
    description = forms.CharField(widget=forms.Textarea())
    commentable = forms.BooleanField(widget=forms.CheckboxInput(attrs={'checked': True}))

class ReviewCreateForm(forms.Form):
    comments = forms.CharField(min_length=3, label='Your review:')
