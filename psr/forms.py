from django import forms
from psr.models import *
from django.forms import MultiWidget
from django.core import validators


class UploadShapefile(forms.Form):
    shpfileUpload = forms.FileField(
        label='Upload a shape file, *.shp',
    )
    # shpIndexUpload = forms.FileField(
    #     label='Upload a shape file index, *.shx',
    # )
    shpfileDataUpload = forms.FileField(
        label='Upload shape file data, *.dbf',
    )

    photoUpload = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        label='Upload all photos',
    )


class UploadShapefileDirectory(forms.Form):
    shapefileUpload = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'webkitdirectory': True, 'directory': True}),
        label='Upload shapefile directory',
    )


class UploadMDB(forms.Form):
    mdbUpload = forms.FileField(
        label='Upload an Access Database, *.mdb',
        widget=forms.FileInput(attrs={'accept': 'application/mdb'}) #not actually a file type, so doesn't limit
    )


class UploadJSON(forms.Form):
    jsonUpload = forms.FileField(
        label='Upload a JSON file, *.json',
        widget=forms.FileInput(attrs={'accept':'application/json'})
    )



# class UploadKMLForm(forms.Form):
#     kmlfileUpload = forms.FileField(
#         label='Upload a kml/kmz file, *.kml or *.kmz ',
#     )
#
# class DeleteAllForm(forms.Form):
#     pass
#
# class DownloadKMLForm(forms.Form):
#     FILE_TYPE_CHOICES = (('1', 'KML',), ('2', 'KMZ',))
#     kmlfileDownload = forms.ChoiceField(
#         required=False,
#         widget=forms.RadioSelect,
#         choices=FILE_TYPE_CHOICES,
#         label="File Type: "
#     )


# class ChangeXYForm(forms.ModelForm):
#     class Meta:
#         model = Occurrence
#         fields = ["barcode", "item_scientific_name", "item_description"]
#     DB_id = forms.IntegerField( max_value=100000)
#     old_easting = forms.DecimalField(max_digits=12)
#     old_northing = forms.DecimalField(max_digits=12)
#     new_easting = forms.DecimalField(max_digits=12)
#     new_northing = forms.DecimalField(max_digits=12)
#
#
# class Occurrence2Biology(forms.ModelForm):
#     class Meta:
#         model = Biology
#         fields = ["barcode", "catalog_number",
#                   "basis_of_record", "item_type", "collector", "collecting_method",
#                   "field_number", "year_collected",
#                   "item_scientific_name", "item_description", "taxon", "identification_qualifier"
#                   ]
#         #fields = ['barcode', 'taxon', 'identification_qualifier']


# from ArturM https://stackoverflow.com/questions/17021852/latitude-longitude-widget-for-pointfield
class LatLongWidget(forms.MultiWidget):
    """
    A Widget that splits Point input into two latitude/longitude boxes.
    """

    def __init__(self, attrs=None, date_format=None, time_format=None):
        widgets = (forms.TextInput(attrs=attrs),
                   forms.TextInput(attrs=attrs))
        super(LatLongWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return tuple(reversed(value.coords))
        return (None, None)


class LatLongField(forms.MultiValueField):
    widget = LatLongWidget
    srid = 4326

    default_error_messages = {
        'invalid_latitude': ('Enter a valid latitude.'),
        'invalid_longitude': ('Enter a valid longitude.'),
    }

    def __init__(self, *args, **kwargs):
        fields = (forms.FloatField(min_value=-90, max_value=90),
                  forms.FloatField(min_value=-180, max_value=180))
        super(LatLongField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            # Raise a validation error if latitude or longitude is empty
            # (possible if LatLongField has required=False).
            if data_list[0] in validators.EMPTY_VALUES:
                raise forms.ValidationError(self.error_messages['invalid_latitude'])
            if data_list[1] in validators.EMPTY_VALUES:
                raise forms.ValidationError(self.error_messages['invalid_longitude'])
            # SRID=4326;POINT(1.12345789 1.123456789)
            srid_str = 'SRID=%d'%self.srid
            point_str = 'POINT(%f %f)'%tuple(reversed(data_list))
            return ';'.join([srid_str, point_str])
        return None
