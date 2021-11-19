1. submit data with forms
2. use the ModelForm class
3. distinguish between bound and unbound forms
4. use django cripsy forms
5. use the MultiValueField

Django forms 
- generate form HTML to render on the client side
- validate incoming data

class FormName(...):
	field_name =FieldType(widget=...)

	