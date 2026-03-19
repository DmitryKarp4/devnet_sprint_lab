import os
import json
import pytest
import jsonschema

def test_summary_validity():
    summary_path = "artifacts/day5/summary.json"
    schema_path = "schemas/day5_summary.schema.json"
    
    assert os.path.exists(summary_path), "summary.json не найден"
    assert os.path.exists(schema_path), "Schema не найдена"
    
    with open(summary_path) as f:
        summary = json.load(f)
    with open(schema_path) as f:
        schema = json.load(f)
    
    # Валидация по схеме
    jsonschema.validate(instance=summary, schema=schema)

def test_token_consistency():
    with open("artifacts/day5/summary.json") as f:
        summary = json.load(f)
    
    expected_hash = summary["student"]["token_hash8"]
    
    # Проверка артефактов Webex на наличие хеша студента
    with open("artifacts/day5/webex/room_create.json") as f:
        room_data = json.load(f)
        assert expected_hash in room_data["title"], "В названии комнаты Webex нет хеша студента"

def test_required_artifacts_exist():
    required_files = [
        "artifacts/day5/yang/ietf-interfaces.yang",
        "artifacts/day5/pt/serviceTicket.txt",
        "artifacts/day5/pt/network_devices.json"
    ]
    for file_path in required_files:
        assert os.path.exists(file_path) and os.path.getsize(file_path) > 0, f"Файл {file_path} отсутствует или пуст"
