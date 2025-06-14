# PASSCRAFT — Advanced Password Generator Tool

![Python](https://img.shields.io/badge/Code-Python-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

> **Craft ultra‑secure passwords in seconds — straight from your terminal.**

---

## ✨ Why PASSCRAFT?

* **Highly Customisable** – choose exact counts of digits, letters & special characters or specify a single total length.
* **Leet Mode** – automatic character substitutions *(a→@, s→\$, i→1, t→7, …)* for extra entropy.
* **Human‑Readable Short Patterns** – use `w`, `d`, `s`, `l`, `u` to lay out your password structure (e.g. `wds` ⇒ `{word}{digit}{special}`).
* **Clear Strength Meter** – instantly tells you if your password is *Strong*, *Moderate* or *Weak*.
* **Colorized Output** – generated passwords appear in green for quick spotting (powered by **colorama**).
* **One‑shot Save** – write the whole batch to a text file with a single prompt.

---

## 🗝️ Supported Character Sets

```text
Lowercase : a‑z           Uppercase : A‑Z
Digits    : 0‑9           Specials  : `!@#$%^&*_-+=:;.?/~
```

---

## 📦 Installation

```bash
# 1. Clone the repo
$ git clone https://github.com/krish-foren6/passcraft.git && cd passcraft

# 2. Install the only external dependency
$ pip install colorama
```

*(Everything else comes from Python’s standard library.)*

---

## 🚀 Quick Start

```bash
$ python passcraft.py
```

Follow the interactive prompts:

```
--- Interactive Mode ---
Enter total password length (0 to skip, leave blank to customise your own): 0
How many digits? 2
How many lowercase letters? 4
How many uppercase letters? 2
How many special characters? 2
How many passwords to generate? 3
Enter a custom word to include (or leave blank): krish
Enter a custom pattern (e.g. 'wds' or {word}{digit}): wds
Apply leet style? (e.g. a → @, i → 1, s → $, t → 7) (y/n): y
```

Example output:

```
Generated Password: Kr1sh@9!  | Strength: Strong 🔒
```

---

## 🔣 Pattern Short‑codes

| Code | Inserts                     |
| ---- | --------------------------- |
| `w`  | `{word}` (custom word)      |
| `d`  | `{digit}` (all digits)      |
| `s`  | `{special}` (special chars) |
| `l`  | `{lower}` (lowercase)       |
| `u`  | `{upper}` (uppercase)       |

Combine them in any order → `dsw` ⇒ digits + specials + word.

---

## 📁 Saving Passwords

After generation you’ll be asked:

```
Do you want to save the passwords to a file? (y/n)
```

Choosing **y** writes each password on a new line in your chosen file.

---

## ⚙️ Command‑line Flags (coming soon)

*Flag mode is under construction – stay tuned!*

---

## 🤝 Contributing

Pull requests & suggestions are welcome! Feel free to open an issue first to discuss what you’d like to change.

---

## 📝 License

This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

## 🙌 Credits

Built with ❤️ by **krish\_foren6**.
