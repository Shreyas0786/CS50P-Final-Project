#from unittest.mock import Mock
import project
import pytest

def test_diplay_village_info(mocker):
    mocker.patch('builtins.input', return_value=1)
    test_input = {"v1":{"title":"test", 'characters':[]},"v2":{"title":"test", "characters":[]}}
    try:
        project.display_village_info(test_input)
    except:
        assert False, "exception raised"
    assert True
    mocker.patch('builtins.input', return_value=10)
    with pytest.raises(Exception) as exc:
        project.display_village_info(test_input)

def test_random_character_info(mocker):
    mocker.patch("random.randint", return_value=1)
    with pytest.raises(Exception) as exc:
        project.random_character_info([])

    characters_test = [{
            "id": 2,
            "name": "Three-Headed Guardian Beast",
            "images": ["https://static.wikia.nocookie.net/naruto/images/7/79/Three-Heads_after_release.png"],
            "personal": { "affiliation": "Yumegakure" }
        },
        {
            "id": 3,
            "name": "A (First Raikage)",
            "images": ["https://static.wikia.nocookie.net/naruto/images/7/70/A.png"],
            "debut": { "manga": "Naruto Chapter #648", "anime": "Naruto Shippūden Episode #369", "appearsIn": "Anime, Manga" },
            "personal": {
            "birthdate": "December 1",
            "sex": "Male",
            "status": "Deceased",
            "height": { "Part II": "210.1cm" },
            "weight": { "Part II": "97.2kg" },
            "bloodType": "O",
            "occupation": "Raikage",
            "affiliation": "Kumogakure"
            },
            "rank": { "ninjaRank": { "Part II": "Kage" } },
            "voiceActors": { "japanese": "Kōsuke Gotō", "english": "Steven Blum" }
        }]
    mocker.patch("random.randint", return_value=1)

    name,jutsus,nature_type, kekkei_genkai, titles = project.random_character_info(characters_test)
    assert name == "A (First Raikage)"
    assert kekkei_genkai == None


def test_formulate_village_ouput():
    with pytest.raises(Exception) as exc:
        project.formulate_village_ouput(["test"])
    test_input = [{"name":"test1", "uniqueTraits":"test"},{"name":"test2"}]
    actual = project.formulate_village_ouput(test_input)
    assert [("test1","test",None),("test2",None,None)] == actual
