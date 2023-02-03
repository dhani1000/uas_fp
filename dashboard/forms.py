from django.forms import ModelForm
from dashboard.models import Barang, Pinjam, Kembali
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

        widgets = {
            'kodebrg' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'stok' : forms.NumberInput({'class':'form-control'}),
            'harga' : forms.NumberInput({'class':'form-control'}),
            'link_gbr' : forms.TextInput({'class':'form-control'}),
            'jenis_id' : forms.Select({'class':'form-control'}),
        }

class FormPinjam(ModelForm):
    class Meta :
        model=Pinjam
        fields='__all__'

        widgets = {
            'id_buku' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
        }

class FormKembali(ModelForm):
    class Meta :
        model=Kembali
        fields='__all__'

        widgets = {
            'id_buku' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),

        }