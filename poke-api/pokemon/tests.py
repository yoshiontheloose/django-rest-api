from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Pokemon

class PokemonTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_thing = Pokemon.objects.create(name='rake', owner=testuser1,description='Better for collecting leaves than a shovel.')
        test_thing.save()

    def test_pokemon_model(self):
        pokemon = Pokemon.objects.get(id=1)
        actual_owner = str(pokemon.owner)
        actual_name = str(pokemon.name)
        actual_description = str(pokemon.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'rake')
        self.assertEqual(actual_description,'Better for collecting leaves than a shovel.')
