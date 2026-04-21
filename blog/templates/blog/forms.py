from django import forms
from .models import Post

# Option 1 — Plain Form
# you define every field manually
# good when the form is not directly tied to a model
class ContactForm(forms.Form):

    # these fields render as <input> elements in HTML
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

    # widget controls how the field renders in HTML
    # Textarea renders a <textarea> instead of <input>
    message = forms.CharField(widget=forms.Textarea)


# Option 2 — ModelForm (most common)
# automatically generates fields from your model
# no need to repeat yourself
# Express equivalent: like Mongoose's schema doing validation for you
class PostForm(forms.ModelForm):

    class Meta:
        # which model to base this form on
        model = Post

        # which fields to include in the form
        # '__all__' means include every field
        # or list specific ones: ['title', 'content']
        fields = ['title', 'content', 'is_published']