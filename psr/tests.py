from django.test import TestCase
from django.test.client import RequestFactory
import pytz

from psr.views import *
from psr.utilities import *


# Create your tests here.


class ImportShapefileMethodsTest(TestCase):
    fixtures = [
        'psr/fixtures/psr-testing-data.json'
    ]

    def setUp(self):
        self.factory = RequestFactory()
        self.import_shapefile = ImportShapefileDirectory
        self.test_file_path = 'psr/testing-data/PSR Testing_Cave_Rockshelter'
        infile = open(self.test_file_path, 'rb')
        request = self.factory.post('/django-admin/psr/geologicalcontext/import_data/', {'shapefileUpload': infile})
        self.import_shapefile.request = request


class SurveyOccurrenceMethodsTests(TestCase):
    fixtures = [
        'psr/fixtures/psr-testing-data.json'
    ]

    def test_psr_occurrence_save_simple(self):
        starting_record_count = Occurrence.objects.count()  # get current number of occurrence records
        new_occurrence = Occurrence(id=1, item_type="Faunal",
                                    basis_of_record="HumanObservation",
                                    collecting_method="Surface Standard",
                                    field_number=datetime.now(pytz.utc),
                                    geom="POINT (40.8352906016 11.5303732536)")
        new_occurrence.save()
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_x(), 40.8352906016)
        self.assertEqual(new_occurrence.point_y(), 11.5303732536)

    def test_psr_create_method(self):
        """
        Test Occurrence instance create method with simple set of attributes.
        :return:
        """
        starting_record_count = Occurrence.objects.count()
        new_occurrence = Occurrence.objects.create(id=1, item_type="Faunal",
                                                   basis_of_record="HumanObservation",
                                                   collecting_method="Surface Standard",
                                                   field_number=datetime.now(pytz.utc),
                                                   geom="POINT (40.8352906016 11.5303732536)")
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_x(), 40.8352906016)

    def test_psr_create_method_invalid_item_type(self):
        """
        """
        starting_record_count = Occurrence.objects.count()
        new_occurrence = Occurrence.objects.create(id=1, item_type="Fake",
                                                   basis_of_record="HumanObservation",
                                                   collecting_method="Surface Standard",
                                                   field_number=datetime.now(pytz.utc),
                                                   geom="POINT (40.8352906016 11.5303732536)")
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_x(), 40.8352906016)
        self.assertEqual(new_occurrence.item_type, "Fake")

    def test_psr_save_method_valid_item_type(self):
        """
        """
        starting_record_count = Occurrence.objects.count()
        new_occurrence = Occurrence()
        new_occurrence.item_type = "Faunal"
        new_occurrence.basis_of_record = "HumanObservation"
        new_occurrence.collecting_method = "Surface Standard"
        new_occurrence.field_number = datetime.now(pytz.utc)
        new_occurrence.geom = "POINT (40.8352906016 11.5303732536)"
        new_occurrence.save()

        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_x(), 40.8352906016)
        self.assertEqual(new_occurrence.item_type, "Faunal")

    def test_psr_save_method_invalid_item_type(self):
        """
        """
        starting_record_count = Occurrence.objects.count()
        new_occurrence = Occurrence()
        new_occurrence.item_type = "Fake"
        new_occurrence.basis_of_record = "HumanObservation"
        new_occurrence.collecting_method = "Surface Standard"
        new_occurrence.field_number = datetime.now(pytz.utc)
        new_occurrence.geom = "POINT (40.8352906016 11.5303732536)"
        new_occurrence.save()

        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_x(), 40.8352906016)
        self.assertEqual(new_occurrence.item_type, "Fake")


class SurveyGeologicalContextMethodsTest(TestCase):

    def test_psr_survey_occurrence_import(self):
        testshp = 'psr/testing-data/PSR Testing_Cave_Rockshelter/PSR Testing_Cave_Rockshelter.shp'
        testdbf = 'psr/testing-data/PSR Testing_Cave_Rockshelter/PSR Testing_Cave_Rockshelter.dbf'
        testname = "Test Cave 1"

        import_geo_contexts(testshp, testdbf, [])
        createdGC = GeologicalContext.objects.get(name=testname)

        #TODO add testing things in here