import json
from uuid import UUID
from django.test import TestCase, Client
from api.models import Project, PackageRelease

# https://stackoverflow.com/questions/48128714/how-to-make-an-inner-join-in-django


class ProjectsTestCase(TestCase):
    def setUp(self):
        Apollo = Project.objects.create(name="Apollo")
        ship_of_theseus = Project.objects.create(name="ship_of_theseus")
        PackageRelease.objects.create(
            name="Plone", version="6.0", project=Apollo
        )
        PackageRelease.objects.create(
            name="Opps", version="0.2.16", project=Apollo
        )
        PackageRelease.objects.create(
            name="remake", version="0.6.1", project=ship_of_theseus
        )
        PackageRelease.objects.create(
            name="just-ship-it", version="0.0.6", project=ship_of_theseus
        )

    def test_Project_Apollo(self):
        """Test project has right conficuration"""
        Apollo = Project.objects.get(name="Apollo")
        Opps = PackageRelease.objects.get(name="Opps")
        Plone = PackageRelease.objects.get(name="Plone")
        packages = PackageRelease.objects.select_related("project")
        self.assertEqual(Apollo.name, "Apollo")
        self.assert_(Plone in packages)
        self.assert_(Opps in packages)

    def test_Project_Ship_of_Theseus(self):
        """Test project has right conficuration"""
        ship_of_theseus = Project.objects.get(name="ship_of_theseus")
        remake = PackageRelease.objects.get(name="remake")
        just_ship_it = PackageRelease.objects.get(name="just-ship-it")
        packages = PackageRelease.objects.select_related("project")
        self.assertEqual(ship_of_theseus.name, "ship_of_theseus")
        self.assertEqual(just_ship_it.name, "just-ship-it")
        self.assertEqual(just_ship_it.version, "0.0.6")
        self.assertEqual(remake.name, "remake")
        self.assertEqual(remake.version, "0.6.1")
        self.assertEqual(just_ship_it.project, ship_of_theseus)
        self.assertEqual(remake.project, ship_of_theseus)
        self.assertTrue(isinstance(ship_of_theseus.id, UUID))
        self.assertTrue(isinstance(remake.id, UUID))
        self.assertTrue(isinstance(just_ship_it.id, UUID))
        self.assert_(just_ship_it in packages)
        self.assert_(remake in packages)

    def test_Api_response(self):
        response_string = b'{"name":"minotaur","packages":[{"name":"eye","version":"1.0"},{"name":"Axe","version":"0.0.4"}]}'
        request_dict = {
            "name": "minotaur",
            "packages": [
                {"name": "eye"},
                {"name": "Axe", "version": "0.0.4"},
            ],
        }
        c = Client()
        #  https://stackoverflow.com/questions/8583290/sending-json-using-the-django-test-client
        response = c.post(
            "/api/projects/",
            json.dumps(request_dict),
            content_type="application/json",
        )
        self.assertContains(
            response, "", count=None, status_code=201
        )
        response = c.get('/api/projects/minotaur/')
        self.assertContains(
            response, "", count=None, status_code=200
        )
        self.assertEqual(response.content, response_string)
        response = c.delete('/api/projects/minotaur/')
        self.assertContains(
            response, "", count=None, status_code=204
        )
        self.assertEqual(response.content, b"")
