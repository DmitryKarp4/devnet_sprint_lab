# Day 3 Report — Lab 4.5.5 + Auto-check artifacts

## 1) Student
- Name: [Карпюк Дмитрий]
- Group: [Иб-23-5б]
- Token: [D1-IB-23-5b-10-2D8F]
- Repo: [https://github.com/DmitryKarp4/devnet_sprint_lab]

## 2) Lab 4.5.5 completion evidence
- API docs (Try it out) screenshots: ![Скриншот API docs](img/screenshot_12.png)
- Postman screenshots: ![Скриншот Postman collection](img/screenshot_13.png) ![Скриншот Postman environment](img/screenshot_14.png)
- Python run screenshot: ![Скриншот тестов](img/screenshot_15.png) ![Скриншот запуска скрипта](img/screenshot_16.png)
- Netacad screenshot:![Скриншот пройденного модуля](img/screenshot_17.png) ![Скриншот пройденного квиза](img/screenshot_18.png)


## 3) Artifacts checklist
- artifacts/day3/books_before.json: **Yes**/No
- artifacts/day3/books_sorted_isbn.json: **Yes**/No
- artifacts/day3/mybook_post.json: **Yes**/No
- artifacts/day3/books_by_me.json: **Yes**/No
- artifacts/day3/add100_report.json: **Yes**/No
- artifacts/day3/postman_collection.json: **Yes**/No
- artifacts/day3/postman_environment.json: **Yes**/No
- artifacts/day3/curl_get_books.txt: **Yes**/No
- artifacts/day3/curl_get_books_isbn.txt: **Yes**/No
- artifacts/day3/curl_get_books_sorted.txt: **Yes**/No
- artifacts/day3/summary.json: **Yes**/No

## 4) Command outputs (paste exact)
### 4.1 Script run
```python
 python src/day3_library_lab.py 
{
  "schema_version": "3.1",
  "generated_utc": "2026-03-17T09:55:27.718545+00:00",
  "student": {
    "token": "D1-IB-23-5b-10-2D8F",
    "token_hash8": "4319d005",
    "name": "Karpyuk",
    "group": "IB-23-5B"
  },
  "lab": {
    "apihost": "http://library.demo.local",
    "must_use": {
      "login_endpoint": "http://library.demo.local/api/v1/loginViaBasic",
      "books_endpoint": "http://library.demo.local/api/v1/books",
      "api_key_header": "X-API-KEY"
    }
  },
  "artifacts_sha256": {
    "books_before": "a691ccf1933612c7f78b6b945edce0167f294a4da4a38265708c849933cf6ed3",
    "books_sorted_isbn": "33d9cb9d28e95a17af37ee6a5266216d1ff7016bd3e6cba99c284a21d8155892",
    "mybook_post": "ba80b8953968a16f08a4e92e4975b14b1d4184260bd058ddb07061859332ec91",
    "books_by_me": "c556f807134f9e0eb5ddeaaf8dda4924605f34ba75f91f7465b83cfe405bee85",
    "add100_report": "995035cb5a0b1334a6ff552d3217a0eb49efc593d595983d889c3f474b43907d",
    "postman_collection": "e96f41c4bf694cf5d50cd8d58ff20a26ffeae6c9cbe6c51dc05f61386486dde9",
    "postman_environment": "5a38bf0dc566ba50257238bd4a34bc2739b0da6b70cdebf0c38e6ab8dab61918",
    "curl_get_books": "0256e22b44731aec51b8038ae59e647199f68b493f8675fc4fff93635474ae14",
    "curl_get_books_isbn": "a5dbb4dd7042bd4447facec22a497d52ef855bee247f3faafc00002289a4d538",
    "curl_get_books_sorted": "a9e635606e8113c3d55e6facf96bee12c0346002adef0465969d2129576948c1"
  },
  "validation": {
    "must_have_mybook_title_contains_token_hash8": true,
    "must_have_added_100": true
  }
}

```

### 4.2 Tests
```text
 pytest -q
...                                                                      [100%]
3 passed in 0.97s

```

## 5) Problems & fixes (at least 1)
- Problem: Забыл установить библиотеку 'faker' для генерации данных, из-за чего скрипт выдавал ошибку при попытке создать фейковую книгу.
- Fix: Установил библиотеку командой `pip install faker`, после чего скрипт успешно сгенерировал книгу и прошёл все тесты.
- Proof: Скрипт запускается без ошибок, а тесты проходят успешно, что подтверждает исправление проблемы.
