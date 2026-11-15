# e2e-chat-single-s-nonui-20261115-200224-3732
office-crew-sprint-runner e2e case chat-single-s-nonui

## Projektbeschreibung

`textutils` ist eine kleine, eigenständige Python-Bibliothek mit fünf voneinander unabhängigen String-Hilfsfunktionen: `slugify`, `truncate`, `word_count`, `is_palindrome` und `reverse_words`. Die Bibliothek hat keine Benutzeroberfläche, speichert keine Daten und nutzt ausschließlich die Python-Standardbibliothek.

## Tech-Stack

- Python 3.11+
- Packaging: `pyproject.toml`, src-Layout mit dem Paket `textutils`
- Tests: pytest
- Lint und Formatierung: ruff
- Laufzeitabhängigkeiten: keine (nur Standardbibliothek)

## Installation

```bash
git clone <repository-url>
cd <repository-verzeichnis>
pip install .
```

Für die Entwicklung (inklusive pytest und ruff):

```bash
pip install -e ".[dev]"
```

## Entwicklung

```bash
pytest                 # Tests ausführen
ruff check .           # Lint
ruff format --check .  # Formatierung prüfen
```

Es gibt nichts zu starten und nichts zu bauen: `textutils` ist eine Bibliothek. Ein Paket für die Verteilung entsteht mit `python -m build`.

## Verwendung

Alle Funktionen werden direkt aus dem Paket importiert:

```python
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words
```

Jede Funktion löst einen `TypeError` aus, wenn `text` kein `str` ist (z. B. `None` oder eine Zahl).

### `slugify(text: str) -> str`

Erzeugt einen URL-tauglichen Slug: Kleinbuchstaben, Akzente entfernt, Gruppen aus Sonderzeichen und Leerraum werden zu einem einzelnen Bindestrich, führende und abschließende Bindestriche entfallen.

```python
slugify("Hello, World!")  # 'hello-world'
slugify("  Crème  Brûlée -- Rezept ")  # 'creme-brulee-rezept'
slugify("!!!")  # ''
```

### `truncate(text: str, max_len: int) -> str`

Kürzt den Text auf höchstens `max_len` Zeichen. Wird gekürzt, endet das Ergebnis auf `...` (die Auslassungspunkte zählen zur Länge). Ein negatives `max_len` löst einen `ValueError` aus.

```python
truncate("Hello World", 8)  # 'Hello...'
truncate("Hi", 8)  # 'Hi'
truncate("Hello", 5)  # 'Hello'
truncate("Hello", -1)  # ValueError
```

### `word_count(text: str) -> int`

Zählt die durch Leerraum (Leerzeichen, Tabulatoren, Zeilenumbrüche) getrennten Wörter.

```python
word_count("one two  three")  # 3
word_count("one\ttwo\nthree")  # 3
word_count("   ")  # 0
```

### `is_palindrome(text: str) -> bool`

Prüft, ob der Text vorwärts und rückwärts gleich gelesen wird. Groß-/Kleinschreibung, Satzzeichen und Leerraum werden ignoriert; der leere Text ist ein Palindrom.

```python
is_palindrome("A man, a plan, a canal: Panama")  # True
is_palindrome("Racecar")  # True
is_palindrome("hello")  # False
is_palindrome("")  # True
```

### `reverse_words(text: str) -> str`

Kehrt die Reihenfolge der Wörter um. Mehrfacher Leerraum sowie führender und abschließender Leerraum werden zu einzelnen Leerzeichen zusammengefasst.

```python
reverse_words("one two three")  # 'three two one'
reverse_words("  a   b ")  # 'b a'
reverse_words("")  # ''
```

## Funktionen

- `slugify`: URL-Slug aus beliebigem Text
- `truncate`: Text auf eine Maximallänge kürzen
- `word_count`: Wörter zählen
- `is_palindrome`: Palindrom-Prüfung
- `reverse_words`: Wortreihenfolge umkehren
- Nur Python-Standardbibliothek, durchgängig typannotiert
