# Day 2 Report — Git + Data Formats + Tests

## 1) Student
- Name: [Карпюк Дмитрий]
- Group: [Иб-23-5б]
- Token: [D1-IB-23-5b-10-2D8F]
- Repo: [https://github.com/DmitryKarp4/devnet_sprint_lab]
- PR link (day2): (also in artifacts/day2/pr_link.txt) [https://github.com/DmitryKarp4/devnet_sprint_lab/pull/1]

## 2) NetAcad progress
- Module 2.2 done: [**Yes**/No] + ![Скриншот прохождения квиза 2.3.2](img/screenshot_8.png) ![Скриншот прохождения модуля 2](img/screenshot_9.png)
- Module 3.1–3.6 done: [list what completed] + ![Скриншот прохождения квиза 3.7.2](img/screenshot_10.png) ![Скриншот прохождения модуля 3](img/screenshot_11.png)

## 3) Git evidence
- File `artifacts/day2/git_log.txt` exists: [**Yes**/No]
- File `artifacts/day2/conflict_log.txt` exists: [**Yes**/No]
- Conflict note (1–2 lines): Конфликт в Readme.md из-за одновременного изменения одной и той же строки в двух ветках. Решение: сделал новую строку, которая объединяет изменения, и закоммитил с сообщением "Resolve conflict in README.md".

## 4) Generated artifacts (Day2)
- normalized.json: [**Yes**/No]
- normalized.yaml: [**Yes**/No]
- normalized.xml: [**Yes**/No]
- normalized.csv: [**Yes**/No]
- summary.json: [**Yes**/No]

## 5) Commands output (paste EXACT output)
### 5.1 Generator
```python
python src/day2_data_formats.py --input artifacts/day1/response.json
{
  "schema_version": "2.0",
  "generated_utc": "2026-03-17T05:54:13.546848+00:00",
  "student": {
    "token": "D1-IB-23-5b-10-2D8F",
    "token_hash8": "4319d005",
    "name": "Karpyuk",
    "group": "IB-23-5B"
  },
  "input": {
    "path": "artifacts/day1/response.json",
    "sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "outputs": {
    "normalized_json_sha256": "99b2706f8e43f6f3b76463ad90b2f4341ecfbd9a67e2b4dac077eca01e165813",
    "normalized_yaml_sha256": "ab81dcfe299e87b19c849cb7cc698df5d8cc4afaf43ec94e545a412c2b9e8afc",
    "normalized_xml_sha256": "f50a5f98726b74f5d2953bfd2a00c2df17c75435bae2548daaf9f8cac5318b0f",
    "normalized_csv_sha256": "81000528ac07f960a0f0fa11c0d9b9df3b1c77bbd83d980d98a68b46f4e6b6d6"
  },
  "computed": {
    "title_len": 18
  }
}
```

### 5.2 Tests
```text
pytest -q
..                                                                           [100%]
2 passed in 0.27s

```
## 6) What I learned (3–6 bullets)
- Разрешать конфликты в Git, объединяя изменения и коммитя с понятным сообщением.
- Использовать Python для генерации различных форматов данных (JSON, YAML, XML, CSV) из одного источника.
- Писать тесты для проверки корректности данных и их форматов.

## 7) Problems & fixes (at least 1)
- Проблем не было, всё штатно.