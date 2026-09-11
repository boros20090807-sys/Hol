from django import forms
from apps.models import Post,Cotegory

# class ProductForms(forms.Form):
#     title = forms.CharField(widget=forms.Textarea, max_length=20,min_length=0)
#     text = forms.CharField(widget=forms.Textarea,max_length=20,min_length=0)
#     image = forms.ImageField(required=False)
#     category = forms.ModelChoiceField(queryset=Cotegory.objects.all(),
#         label="Категория"
#     )
#     price = forms.IntegerField(widget=forms.NumberInput)
#     count = forms.IntegerField(widget=forms.NumberInput)
# def title_product(self):
#     title=self.cleaned_data.get('title')
#     if title=="Ibrohim тупой":
#         raise forms.ValidationError("сам тупой")
#     return title

class ProductForms(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['slug']
        
        # filds='__all__'



