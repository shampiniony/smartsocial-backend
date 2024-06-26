import requests

from backend.settings import AMOCRM_ACCESS_TOKEN


def get_custom_fields_to_id(url) -> dict[str, int]:
    headers = {
        'Authorization': f'Bearer {AMOCRM_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        custom_fields = response.json()['_embedded']['custom_fields']
        field_to_id = {}
        for field in custom_fields:
            field_to_id[field['name']] = field['id']
        return field_to_id
    else:
        print('Ошибка при получении пользовательских полей:', response.json())
        return {}


def get_statuses_to_id() -> dict[str, int]:
    headers = {
        'Authorization': f'Bearer {AMOCRM_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }

    response = requests.get("https://forvantar.amocrm.ru/api/v4/leads/pipelines", headers=headers)
    if response.status_code == 200:
        custom_fields = response.json()['_embedded']['pipelines'][0]["_embedded"]["statuses"]
        field_to_id = {}
        for field in custom_fields:
            field_to_id[field['name']] = field['id']
        return field_to_id
    else:
        print('Ошибка при получении пользовательских полей:', response.json())
        return {}
