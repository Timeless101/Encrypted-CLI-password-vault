# Encrypted CLI Password Vault

A modular command-line password manager built with Python, SQLite, Argon2id, Fernet, Rich, and pytest.

![Python 3.14](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-pytest-0A9EDC?logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20development-orange)

> This project is under active development. It has not been independently security-audited and should not yet be used to store production credentials.

## Overview

Encrypted CLI Password Vault is a local password manager with a terminal interface. It supports user registration and login, encrypts credential passwords before writing them to SQLite, and separates interface, application logic, storage, validation, and cryptographic responsibilities into dedicated modules.

The project began as a way to learn Python by building a complete application rather than isolated exercises. The current goal is to finish and harden the CLI as a complete v1.0 release before moving on to a REST API and web interface.

## Current interface

![Main interface](docs/images/main_view.png)

The main interface displays an overview of credentials stored in the vault and provides keyboard-driven navigation to the main vault features.

![All credentials view](docs/images/view-credentials.png)

The credential view displays five records per page, masks passwords in list views, orders credentials predictably, and supports opening individual credentials for further actions.

## Current features

### Authentication

- Local user registration and login
- Email validation and duplicate-account prevention
- Master-password verification using Argon2id
- Separate salts for password verification and encryption-key derivation
- Per-user credential records
- Session encryption-key derivation after successful authentication

### Password vault

- Add credentials through an interactive CLI flow
- Encrypt credential passwords with Fernet before database storage
- Confirm entered data before saving
- Display credentials in Rich tables
- Sort credentials by service and username
- Five-record pagination with previous/next navigation
- Dynamic `Showing x-y of total` and page information
- Open an individual credential from the View screen
- Keep passwords masked in overview/detail screens until explicitly requested
- Reveal and copy a selected credential password
- Edit Service, Username, Password, and Comment
- Delete credentials with confirmation
- Store creation and modification timestamps
- Dedicated empty-vault handling

### Application design

- Layered, modular project structure
- Separate interface, logic, service, storage, validation, and cryptography modules
- Feature-specific vault services for Add, View, and Edit
- Custom application exceptions
- Automatic SQLite database and table initialization
- Parameterized SQL values
- Type hints across the application

### Testing

- pytest-based automated test suite
- Tests for cryptography, validation, login logic, vault logic, storage, and storage logic
- Temporary SQLite databases through pytest's `tmp_path`
- Mocking and exception-path testing
- Additional tests are being added for Edit, Delete, Search, pagination edge cases, ownership checks, and crypto failures

## Development status

The majority of the CLI feature set is implemented. Search is the final major CLI feature before the project moves into a larger refactor, security-hardening, test-cleanup, documentation, and release phase.

### Implemented

- [x] Database initialization
- [x] Registration and login
- [x] Argon2id password verification
- [x] Session encryption-key derivation
- [x] Fernet encryption for stored credential passwords
- [x] Add Credential flow
- [x] Vault dashboard
- [x] Alphabetically sorted credential view
- [x] Five-record pagination
- [x] Previous and next page navigation
- [x] Dynamic pagination metadata
- [x] Open an individual credential
- [x] Reveal a password only after explicit user action
- [x] Copy a revealed password
- [x] Edit credentials
- [x] Delete credentials
- [x] Dedicated empty-state handling

### In progress

- [ ] Search credentials
- [ ] Fix remaining Delete edge cases
- [ ] Make the main overview consistently show the most recent credentials
- [ ] Bring the complete automated test suite in sync with the current application

### CLI v1.0 cleanup and hardening

- [ ] Full code refactor and responsibility cleanup
- [ ] Error-handling refactor
- [ ] Credential ownership checks on reads and deletes
- [ ] SQL identifier hardening
- [ ] Clipboard cleanup for copied passwords
- [ ] Session cleanup on lock/logout
- [ ] Database schema/constraint review
- [ ] Crypto failure handling
- [ ] Final CLI navigation and UX polish
- [ ] README and architecture documentation
- [ ] Security documentation
- [ ] Clean-install verification
- [ ] Full manual acceptance test
- [ ] CLI v1.0 release

### Future platform development

After the CLI v1.0 milestone, the project is planned to continue with:

- [ ] FastAPI REST API
- [ ] Web interface using HTML/CSS/JavaScript
- [ ] PostgreSQL support
- [ ] Server-side multi-user authentication/session design
- [ ] Docker deployment
- [ ] Cloud deployment

## Security model

The current implementation uses the following high-level flow:

1. The master password is processed with Argon2id during registration and authentication.
2. Password verification and encryption-key derivation use separate stored salts.
3. After a successful login, an encryption key is derived for the active session.
4. Credential passwords are encrypted with Fernet before being written to SQLite.
5. List views retrieve only the fields required for display and show passwords as masked values.
6. A credential password is fetched/decrypted only when the user explicitly requests access to it.

Security-sensitive code is still being reviewed and hardened. Before the first stable CLI release, the project roadmap includes ownership enforcement, session and clipboard cleanup, database constraint review, crypto failure handling, improved tests, and documentation of security limitations.

This project has not undergone an independent security audit and does not make production-grade security guarantees.

## Project structure

```text
Encrypted-CLI-password-vault/
|
|-- src/
|   |-- interface/
|   |   |-- error_messages.py
|   |   |-- helper_functions.py
|   |   |-- login_interface.py
|   |   `-- vault_interface.py
|   |
|   |-- vault_services/
|   |   |-- add_items.py
|   |   |-- edit.py
|   |   |-- helper_functions.py
|   |   `-- view_items.py
|   |
|   |-- crypto.py
|   |-- errors.py
|   |-- login_logic.py
|   |-- main.py
|   |-- main_logic.py
|   |-- storage.py
|   |-- storage_logic.py
|   |-- validator.py
|   `-- vault_logic.py
|
|-- tests/
|   |-- crypto/
|   |-- login_logic/
|   |-- storage/
|   |-- storage_logic/
|   |-- validator/
|   `-- vault_logic/
|
|-- pytest.ini
|-- requirements.txt
`-- README.md
```

The structure is still being actively refactored. The goal is for interface modules to focus on input/output, vault services to own feature-specific flows, application logic to coordinate behavior, and storage modules to isolate database access.

## Technology stack

| Technology | Purpose |
|---|---|
| Python 3.14 | Application runtime |
| SQLite | Local persistent storage |
| cryptography | Fernet encryption and supporting cryptographic operations |
| Argon2id | Master-password verification / key-derivation-related password processing |
| Rich | Terminal layout, panels, tables, and prompts |
| InquirerPy | Interactive CLI input |
| pyperclip | Clipboard support for copied passwords |
| pytest | Automated testing |

## Installation

Python 3.14 is currently used for development.

```bash
git clone https://github.com/Timeless101/Encrypted-CLI-password-vault.git
cd Encrypted-CLI-password-vault
python -m pip install -r requirements.txt
```

Run the application from the repository root:

```bash
python -m src.main
```

The SQLite database is created automatically on first start and should remain excluded from Git.

## Running the tests

Run the complete test suite:

```bash
python -m pytest
```

Run tests with detailed output:

```bash
python -m pytest -vv
```

Run a single test file while showing printed output:

```bash
python -m pytest -s path/to/test_file.py
```

The test suite is currently being updated alongside the final CLI feature and refactor work, so some existing tests may temporarily need adjustment as older application flows are removed or changed.

## Roadmap to CLI v1.0

The remaining work is tracked through GitHub Issues and is grouped around six main areas:

1. **Search** — complete the final major CLI feature.
2. **Refactor** — simplify structure, responsibilities, naming, typing, and error handling.
3. **Testing** — bring the full automated suite up to date and cover important edge cases.
4. **Security hardening** — enforce user ownership and review sensitive-data handling.
5. **CLI polish** — make navigation, empty states, errors, and feedback consistent.
6. **Release** — verify a clean install, update documentation, run an acceptance test, and publish CLI v1.0.

The API and web interface are intentionally treated as the next project phase rather than part of the CLI v1.0 milestone.

## Design goals

This project is being developed around a few practical goals:

- Keep user-interface code separate from business and storage logic.
- Make security-sensitive operations explicit and testable.
- Keep database access replaceable so SQLite can later be exchanged for PostgreSQL.
- Reuse application/domain logic when the API and web interface are introduced.
- Prefer understandable code and incremental refactoring over prematurely complex abstractions.
- Finish features before introducing abstractions that are not yet justified by the codebase.

## Contributing

Feedback, bug reports, security observations, and architecture discussions are welcome. Because this is also a learning project, please open an issue before submitting a large change so the reasoning and design can be discussed first.

Do not include real credentials, database files, encryption keys, master passwords, or other secrets in issues, logs, screenshots, or pull requests.

## License

This repository does not currently include an open-source license. Selecting and adding a license is part of the CLI v1.0 release roadmap.

## Author

**Diego Wuck**

System Engineer building practical Python and cloud engineering skills through hands-on projects.
