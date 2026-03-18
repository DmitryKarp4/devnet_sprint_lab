# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name: [Карпюк Дмитрий]
- Group: [Иб-23-5б]
- Token: [D1-IB-23-5b-10-2D8F]
- Repo: [https://github.com/DmitryKarp4/devnet_sprint_lab]

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: +
- artifacts/day4/docker/sampleapp_token_proof.txt: +
- artifacts/day4/docker/sampleapp_docker_ps.txt: +
- artifacts/day4/docker/sampleapp_build_log.txt: +

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt: +
- artifacts/day4/jenkins/buildapp_console.txt: +
- artifacts/day4/jenkins/testapp_console.txt: +
- artifacts/day4/jenkins/pipeline_script.groovy: +
- artifacts/day4/jenkins/pipeline_console.txt: +
- artifacts/day4/jenkins/jenkins_url.txt: +

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_ping.txt: +
- artifacts/day4/ansible/ansible_hello.txt: +
- artifacts/day4/ansible/ansible_playbook_install.txt: +
- artifacts/day4/ansible/ports_conf_after.txt: +
- artifacts/day4/ansible/curl_apache_8081.txt: +

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt: +
- artifacts/day4/security/login_v1.txt: +
- artifacts/day4/security/signup_v2.txt: +
- artifacts/day4/security/login_v2.txt: +
- artifacts/day4/security/db_tables.txt: +
- artifacts/day4/security/db_user_hash_sample.txt: +

## 3) Commands output
```text
python src/day4_summary_builder.py
{
  "schema_version": "4.1",
  "generated_utc": "2026-03-18T12:00:42.627380+00:00",
  "student": {
    "token": "D1-IB-23-5b-10-2D8F",
    "token_hash8": "4319d005",
    "name": "Karpyuk",
    "group": "IB-23-5B"
  },
  "checks": {
    "docker_token_in_page": true,
    "docker_tokenproof": true,
    "ansible_port_8081": true,
    "jenkins_pipeline_has_stages": true,
    "security_db_has_tables": true
  },
  "evidence_sha256": {
    "docker_sampleapp_curl": "d75a4071ff1ce8e4bec88ddf4ae1b1d2ebfae225a293f54582484953f0d4a90c",
    "docker_ps": "391ce2f3ce3af2b92cdc2371c43b1de05d858197dd2a3623cca917bc4948d9e9",
    "docker_build_log": "f580eba324215b51ad7874c1d6e3ba26250348c30345e6a836cf37303249b0de",
    "docker_token_proof": "81b619ccfeab6dbc206bbf6d0aecfb15253a3e8b12f425120fac9621d7fb5ecd",
    "jenkins_docker_ps": "0ee835f0c62afb9e4081a43c5d2c3a36fa0182dac8f679bfc145bd18c06884cb",
    "buildapp_console": "b2960684f9fab1c75114cb9701c1ecb59b5b2ff2dfbce9e5c667fe2d5a2443f7",
    "testapp_console": "c9b469ed488bd95a24345f500a4f60a246a44c795f9889501d29c80fed516158",
    "pipeline_script": "55cdfb944ffadc5a680855519ee745abda1c8d87554f5b4410c422884df1ea58",
    "pipeline_console": "4f6d0c732195b98b509925abc1f20a8457588abaaf16de90e3d3617770c1d69d",
    "jenkins_url": "185f195598830dbc315eb3a6741f97eace245e9d9d2a7225c5da77b87f27f3fc",
    "ansible_ping": "005e9245df2c530d64aee6bfec751dfc3ced4b06361f597e7fde4163bc44fd69",
    "ansible_hello": "6b506fcd95eb0febede6e36542f9524299ecd459f7b11b6743bef44138cbb0fb",
    "ansible_playbook_install": "780a930fdc01318e3b45c474d7947b8716a2433723aa3db9c981cff178781583",
    "ports_conf_after": "8ee0ac8272eaa90ca6a9597cb472034768331e543d074cc72141b520ffb6f686",
    "curl_apache_8081": "e870932d034a48187d6685a82452e2dfbd36db1ae9840a89275eaab07b73a009",
    "signup_v1": "cbec021c2c093dc9d12a1e89376f20e050573b7b89059b5cc5593709d498a441",
    "login_v1": "4e885c0fa26fb9497717e18e8a289a45d1cce748c0bd91a401302c729ca48cfc",
    "signup_v2": "d299da4792553b50de72449cda41e26da947f741018a6c11f3a94b009be6579f",
    "login_v2": "4e885c0fa26fb9497717e18e8a289a45d1cce748c0bd91a401302c729ca48cfc",
    "db_tables": "dabd3431f2b5b343f501644e201a38fdaad5d5f185717854809ef3d7745a89f3",
    "db_user_hash_sample": "8c68d04d8bddadf80ae05ddda4c0fa7d42b9626fb1e63beb0d62b36505bbe3d6"
  },
  "validation_passed": true,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}
````

```text
pytest -q
....                                                                     [100%]
4 passed in 0.82s

```
## 4) Short reflection (5–8 lines)
- Сложнейшей частью было разобраться с Jenkins, так как инстуркции в документации были старыми и вызывали конфликты с новыми версиями. Пришлось искать решения в интернете и адаптировать их.
- Научились работать с Docker, создавать образы и запускать контейнеры.
- Поняли основы CI/CD с помощью Jenkins и написали простой pipeline.
- Освоили Ansible для автоматизации конфигурации серверов и развертывания.
- Избежали ошибки при работе с базой данных в части безопасности хранения паролей.

## 5) Problems & fixes (at least 1)
- Problem: Jenkins отказывался запускаться корректно в докер-образе
- Fix: Костыли выполненные с помощью нейронки
- Proof: В конечном итоге Jenkins запустился и успешно выполняет pipeline, что подтверждается выводом консоли и результатами тестов.
...