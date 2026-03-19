import os
import json
import hashlib

def get_token_hash8(token):
    """Вычисляет sha256(STUDENT_TOKEN)[:8] согласно требованиям."""
    return hashlib.sha256(token.encode()).hexdigest()[:8]

def build_summary():
    # Загрузка переменных окружения (имитация из .env)
    student_token = os.getenv("STUDENT_TOKEN", "default_token")
    token_hash = get_token_hash8(student_token)
    
    base_path = "artifacts/day5"
    summary_file_path = os.path.join(base_path, "summary.json")
    
    # 1. Анализ YANG (Lab 8.3.5)
    yang_tree_path = os.path.join(base_path, "yang/pyang_tree.txt")
    has_yang = os.path.exists(yang_tree_path)
    interfaces_found = False
    if has_yang:
        with open(yang_tree_path, 'r') as f:
            content = f.read()
            # Проверка наличия обязательного блока по лабе
            interfaces_found = "+--rw interfaces" in content

    # 2. Анализ Webex (Lab 8.6.7)
    webex_room_path = os.path.join(base_path, "webex/room_create.json")
    has_webex = os.path.exists(webex_room_path)
    room_ok = False
    if has_webex:
        with open(webex_room_path, 'r') as f:
            try:
                data = json.load(f)
                # Уникальность: название содержит token_hash8
                room_ok = token_hash in data.get("title", "")
            except json.JSONDecodeError:
                room_ok = False

    # 3. Анализ Packet Tracer Controller (Activity 8.8.3) [cite: 740]
    pt_check_path = os.path.join(base_path, "pt/external_access_check.json")
    has_pt = os.path.exists(pt_check_path)
    empty_ticket_ok = False
    if has_pt:
        with open(pt_check_path, 'r') as f:
            content = f.read()
            # Ожидаемый ответ при проверке доступа извне
            empty_ticket_ok = "Ticket-based authorization: empty ticket" in content

    # Сборка финального объекта
    summary = {
        "schema_version": "5.0",
        "student": {
            "token_hash8": token_hash,
            "name": os.getenv("STUDENT_NAME", "Unknown"),
            "group": os.getenv("STUDENT_GROUP", "Unknown")
        },
        "yang": {
            "ok": has_yang,
            "has_interfaces_node": interfaces_found
        },
        "webex": {
            "ok": has_webex,
            "room_title_contains_hash8": room_ok
        },
        "pt": {
            "ok": has_pt,
            "empty_ticket_seen": empty_ticket_ok
        },
        "validation_passed": all([has_yang, interfaces_found, room_ok, empty_ticket_ok])
    }

    # Сохранение в файл
    os.makedirs(os.path.dirname(summary_file_path), exist_ok=True)
    with open(summary_file_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)

    # ВЫВОД В КОНСОЛЬ (Output для проверки)
    print("\n" + "="*20 + " SUMMARY.JSON CONTENT " + "="*20)
    print(json.dumps(summary, indent=4, ensure_ascii=False))
    print("="*62 + "\n")

if __name__ == "__main__":
    build_summary()
