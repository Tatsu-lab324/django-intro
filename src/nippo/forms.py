from django import forms
from .models import NippoModel

class NippoModelForm(forms.ModelForm):
    class Meta:
        model = NippoModel
        exclude = ["user"]
        # fields = "__all__"

    def __init__(self,user=None, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        nippo_obj = super().save(commit=False)
        if self.user:
            nippo_obj.user = self.user
        if commit:
            nippo_obj.save()
        return nippo_obj

# class NippoFormClass(forms.Form):
#     title = forms.CharField(max_length=255,label="タイトル")
#     content = forms.CharField(widget=forms.Textarea(),max_length=1000,label="内容")

