# Day 5 Report — Module 8 Capstone

## 1) Student
- Name: [Карпюк Дмитрий]
- Group: [Иб-23-5б]
- Token: [D1-IB-23-5b-10-2D8F]
- Repo: [https://github.com/DmitryKarp4/devnet_sprint_lab]

## 2) YANG (8.3.5)
- Evidence files:
  - artifacts/day5/yang/ietf-interfaces.yang
  - artifacts/day5/yang/pyang_version.txt
  - artifacts/day5/yang/pyang_tree.txt
```bash
    artifacts/day5/yang/
    ├── ietf-interfaces.yang
    ├── pyang_tree.txt
    └── pyang_version.txt
```

## 3) Webex (8.6.7)
- Room title contains token_hash8: **Yes**/No
- Message text contains token_hash8: **Yes**/No
- Evidence files:
  - me.json / rooms_list.json / room_create.json / message_post.json / messages_list.json
```bash
artifacts/day5/webex/
├── me.json
├── message_post.json
├── messages_list.json
├── room_create.json
└── rooms_list.json
```

## 4) Packet Tracer Controller REST (8.8.3)
- external_access_check contains “empty ticket”: **Yes**/No
- serviceTicket saved: **Yes**/No
- Evidence files:
  - external_access_check.json / network_devices.json / hosts.json
  - postman_collection.json / postman_environment.json
  - pt_internal_output.txt
```bash
artifacts/day5/pt/
├── external_access_check.json
├── hosts.json
├── network_devices.json
├── postman_collection.json
├── postman_environment.json
├── pt_internal_output.txt
└── serviceTicket.txt
```

## 5) Commands output (paste exact)
```python
 python src/day5_summary_builder.py

==================== SUMMARY.JSON CONTENT ====================
{
    "schema_version": "5.0",
    "student": {
        "token_hash8": "4319d005",
        "name": "Karpyuk",
        "group": "IB-23-5B"
    },
    "yang": {
        "ok": true,
        "has_interfaces_node": true
    },
    "webex": {
        "ok": true,
        "room_title_contains_hash8": true
    },
    "pt": {
        "ok": true,
        "empty_ticket_seen": true
    },
    "validation_passed": true
}
==============================================================

pytest -q
.......                                                                  [100%]
7 passed in 0.76s

```
## 6) Problems & fixes (at least 1)
- Problem: Проблема была с Packet Tracer, вероятно из-за старой версии вкладка Programming не открывалась.
- Fix: Перешел на основную машину с сохранением всех данных, выполнил задание там, все заработало.
- Proof: Задание выполнено успешно.
...