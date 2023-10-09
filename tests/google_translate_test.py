import requests
from hamcrest import assert_that, equal_to
from cerberus import Validator

BASE_URI = "https://google-translate1.p.rapidapi.com/language/translate/v2"
HEADERS = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": "2e958e27c2mshfd71883a80b193cp1697aejsndb6a3a68669c",
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}


def test_translate_with_required_param():
    params = {
        "q": "Hello, world!",
        "target": "es"
    }
    response = requests.post(BASE_URI, headers=HEADERS, data=params)
    assert_that(response.status_code, equal_to(200))
    assert_that(response.json()["data"]["translations"][0]["translatedText"], equal_to("¡Hola Mundo!"))
    assert_that(response.json()["data"]["translations"][0]["detectedSourceLanguage"], equal_to("en"))


def test_translate_with_optional_param():
    params = {
        "source": "en",
        "q": "Hello, world!",
        "target": "es",
        "format": "text"
    }
    response = requests.post(BASE_URI, headers=HEADERS, data=params)
    assert_that(response.status_code, equal_to(200))
    assert_that(response.json()["data"]["translations"][0]["translatedText"], equal_to("¡Hola Mundo!"))
    assert_that(response.json()["data"]["translations"][0].get("detectedSourceLanguage"), equal_to(None))


def test_translate_without_any_required_params():
    params = {
        "source": "en",
    }
    response = requests.post(BASE_URI, headers=HEADERS, data=params)
    assert_that(response.status_code, equal_to(502))


def test_translate_without_required_param():
    params = {
        "source": "en",
        "q": "Hello, world!",
    }
    response = requests.post(BASE_URI, headers=HEADERS, data=params)
    assert_that(response.status_code, equal_to(400))
    assert_that(response.json()["error"]["message"], equal_to("Missing required field target"))


def test_translate_with_invalid_param():
    params = {
        "source": "en",
        "q": "Hello, world!",
        "target": "es",
        "format": "invalid"
    }
    response = requests.post(BASE_URI, headers=HEADERS, data=params)
    assert_that(response.status_code, equal_to(400))
    assert_that(response.json()["error"]["message"], equal_to("Invalid Value"))


def test_translate_multiple_translations():
    params = [
        ("q", "Hello, world!"),
        ("q", "Goodbye, world!"),
        ("target", "es")
    ]
    response = requests.post(BASE_URI, headers=HEADERS, data=params)
    assert_that(response.status_code, equal_to(200))
    assert_that(response.json()["data"]["translations"][0]["translatedText"], equal_to("¡Hola Mundo!"))
    assert_that(response.json()["data"]["translations"][1]["translatedText"], equal_to("¡Adiós mundo!"))


def test_translate_with_invalid_key():
    params = {
        "q": "Hello, world!",
        "target": "es"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "invalid",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.post(BASE_URI, headers=headers, data=params)
    assert_that(response.status_code, equal_to(403))
    assert_that(response.json()["message"], equal_to("You are not subscribed to this API."))


def test_translate_with_invalid_host():
    params = {
        "q": "Hello, world!",
        "target": "es"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "2e958e27c2mshfd71883a80b193cp1697aejsndb6a3a68669c",
        "X-RapidAPI-Host": "invalid"
    }
    response = requests.post(BASE_URI, headers=headers, data=params)
    assert_that(response.status_code, equal_to(400))


def test_translate_with_invalid_method():
    params = {
        "q": "Hello, world!",
        "target": "es"
    }
    response = requests.get(BASE_URI, headers=HEADERS, data=params)
    assert_that(response.status_code, equal_to(404))
    assert_that(response.json()["message"], equal_to("Endpoint '/language/translate/v2' does not exist"))


def test_translate_with_invalid_url():
    params = {
        "q": "Hello, world!",
        "target": "es"
    }
    response = requests.post("https://google-translate1.p.rapidapi.com/language/translate/v3", headers=HEADERS,
                             data=params)
    assert_that(response.status_code, equal_to(404))
    assert_that(response.json()["message"], equal_to("Endpoint '/language/translate/v3' does not exist"))


def test_validate_response_schema_with_detected_source_language():
    params = {
        "q": "Hello",
        "target": "es"
    }
    response = requests.post(BASE_URI, headers=HEADERS, data=params)
    print(response.json()["data"])
    schema = {
        "translations": {
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
                    "translatedText": {"type": "string"},
                    "detectedSourceLanguage": {"type": "string"}
                }
            }
        }
    }
    assert_that(response.status_code, equal_to(200))
    assert_that(Validator(schema).validate(response.json()["data"]), equal_to(True))


def validate_response_schema_without_detected_source_language():
    params = {
        "q": "Hello",
        "target": "es",
        "source": "en",
    }
    response = requests.post(BASE_URI, headers=HEADERS, data=params)
    print(response.json()["data"])
    schema = {
        "translations": {
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
                    "translatedText": {"type": "string"}
                }
            }
        }
    }
    assert_that(response.status_code, equal_to(200))
    assert_that(Validator(schema).validate(response.json()["data"]), equal_to(True))


def test_validate_response_schema_with_model_and_source_params():
    params = {
        "q": "Hello",
        "target": "es",
        "source": "en",
        "model": "nmt"
    }
    response = requests.post(BASE_URI, headers=HEADERS, data=params)
    print(response.json()["data"])
    schema = {
        "translations": {
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
                    "translatedText": {"type": "string"},
                    "model": {"type": "string"},
                }
            }
        }
    }
    assert_that(response.status_code, equal_to(200))
    assert_that(Validator(schema).validate(response.json()["data"]), equal_to(True))
