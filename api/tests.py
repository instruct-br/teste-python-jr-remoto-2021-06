import json
from uuid import UUID
from django.test import TestCase, Client
from api.models import Project, PackageRelease

# https://stackoverflow.com/questions/48128714/how-to-make-an-inner-join-in-django

ERROR_DOESNT_EXIST = b'{"error":"One or more packages doesn\'t exist"}'


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
            name="ship", version="0.3", project=ship_of_theseus
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
        """Test project has right configuration"""
        ship_of_theseus = Project.objects.get(name="ship_of_theseus")
        remake = PackageRelease.objects.get(name="remake")
        ship = PackageRelease.objects.get(name="ship")
        packages = PackageRelease.objects.select_related("project")
        self.assertEqual(ship_of_theseus.name, "ship_of_theseus")
        self.assertEqual(ship.name, "ship")
        self.assertEqual(ship.version, "0.3")
        self.assertEqual(remake.name, "remake")
        self.assertEqual(remake.version, "0.6.1")
        self.assertEqual(ship.project, ship_of_theseus)
        self.assertEqual(remake.project, ship_of_theseus)
        self.assertTrue(isinstance(ship_of_theseus.id, UUID))
        self.assertTrue(isinstance(remake.id, UUID))
        self.assertTrue(isinstance(ship.id, UUID))
        self.assert_(ship in packages)
        self.assert_(remake in packages)

    def test_Api_response(self):
        """Test full cicle of API"""
        # https://www.studytonight.com/post/significance-of-prefix-b-in-a-string-in-python
        # https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
        response_string = b'{"name":"minotaur","packages":[{"name":"bull","version":"0.4.1"},{"name":"Axe","version":"0.0.4"}]}'
        request_dict = {
            "name": "minotaur",
            "packages": [
                {"name": "bull"},
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

    def test_Api_not_response(self):
        """Test error mensages of API"""
        request_dict = {
            "name": "Medusa",
            "packages": [
                {"name": "BreackMirror"},
                {"name": "StoneVictim123456789", "version": "0.0.4"},
            ],
        }
        c = Client()
        response = c.post(
            "/api/projects/",
            json.dumps(request_dict),
            content_type="application/json",
        )
        self.assertContains(
            response, "", count=None, status_code=400
        )
        self.assertEqual(response.content, ERROR_DOESNT_EXIST)
        response = c.get('/api/projects/medusa/')
        self.assertContains(
            response, "", count=None, status_code=404
        )
        self.assertEqual(response.content, b'{"detail":"Not found."}')
        response = c.delete('/api/projects/medusa/')
        self.assertContains(
            response, "", count=None, status_code=404
        )
        self.assertEqual(response.content, b'{"detail":"Not found."}')

    def test_check_post_rules(self):
        """Checking rules of Serializers"""
        request_dict = {
            "name": "Dionysus0",
            "packages": [
                {"name": "TensorFlow", "version": 10},
            ],
        }
        c = Client()
        response = c.post(
            "/api/projects/",
            json.dumps(request_dict),
            content_type="application/json",
        )
        self.assertContains(
            response, "", count=None, status_code=400
        )
        self.assertEqual(response.content, ERROR_DOESNT_EXIST)
        request_dict = {
            "name": "Dionysus1",
            "packages": [
                {"name": "TensorFlow", "version": "ten"},
            ],
        }
        response = c.post(
            "/api/projects/",
            json.dumps(request_dict),
            content_type="application/json",
        )
        self.assertContains(
            response, "", count=None, status_code=400
        )
        self.assertEqual(response.content, ERROR_DOESNT_EXIST)
        request_dict = {
            "name": "Dionysus2",
            "packages": [
                {"name": "MoreWinePLEASE"},
            ],
        }
        response = c.post(
            "/api/projects/",
            json.dumps(request_dict),
            content_type="application/json",
        )
        self.assertContains(
            response, "", count=None, status_code=400
        )
        self.assertEqual(response.content, ERROR_DOESNT_EXIST)
        request_dict = {
            "name": "Dionysus3",
            "packages": [
            ],
        }
        response = c.post(
            "/api/projects/",
            json.dumps(request_dict),
            content_type="application/json",
        )
        self.assertContains(
            response, "", count=None, status_code=400
        )
        self.assertEqual(response.content, ERROR_DOESNT_EXIST)
        request_dict = {
            "packages": [
                {"name": "wine-deamonizer"},
            ],
        }
        response = c.post(
            "/api/projects/",
            json.dumps(request_dict),
            content_type="application/json",
        )
        self.assertContains(
            response, "", count=None, status_code=400
        )
        self.assertEqual(response.content, b'{"name":["This field is required."]}')
        request_dict = {
            "name": "DionysusLastTry",
            "packages": [
                {"name": "wine-deamonizer", "version": "1.0.1"},
            ],
        }
        response = c.post(
            "/api/projects/",
            json.dumps(request_dict),
            content_type="application/json",
        )
        self.assertContains(
            response, "", count=None, status_code=201
        )
