# 🖥️ Custom Terminal Emulator

A simple, lightweight, Python-based terminal emulator that mimics common shell commands like `cd`, `ls`, `touch`, `rm`, `mkdir`, `echo`, and more — all built using only basic Python and standard libraries.

---

## 🚀 Features

- ✅ Command parsing using `shlex`
- ✅ Support for common shell commands:
  - `cd`, `ls`, `pwd`, `echo`
  - `cat`, `mkdir`, `rmdir`
  - `rm` (with flags support)
  - `touch` (with `-c` flag support)
  - `clear`, `exit`, `ping`
- ✅ Handles command-line flags like `-c`, `-rf`, etc.
- ✅ Graceful error handling for invalid commands
- ✅ Dynamic prompt showing username and current directory
- ✅ Cross-platform support (`cls` vs `clear`)

---

## 🧩 Libraries Used

- [`os`](https://docs.python.org/3/library/os.html) – for interacting with the OS (filesystem, environment, etc.)
- [`subprocess`](https://docs.python.org/3/library/subprocess.html) – for executing system-level commands safely
- [`shlex`](https://docs.python.org/3/library/shlex.html) – for parsing shell-like syntax

---

## 📂 Project Structure

```text
terminal/
├── src/
│   └── terminal.py      # main file that runs the terminal
├── README.md            # you're reading it
├── .gitignore
├── LICENSE
```

---

## 💻 Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/IshworTM/terminal-emulator.git
cd terminal-emulator/src
```

2. **Run the terminal:**

```bash
python3 terminal.py
```

---

## 📌 Notes

- You can only run allowed commands (check `ALLOWED_COMMANDS` dict).
- `TERM environment variable not set.` error might show when running in an IDE; try running it from a real terminal instead (`bash`, `zsh`, etc.).
- Designed to be simple and extensible — feel free to add more custom commands.

---

## 🛠️ To Do / Ideas to be implemented in the future

- [ ] Add support for command piping (`|`)
- [ ] Implement file redirection (`>`, `<`)
- [ ] Add a help command (`man`-like info for built-in commands)
- [ ] History & command autocomplete
- [ ] Implement history navigation using the Up/Down arrow keys.

---

## ⚖️ License

MIT License. Do whatever you want, just don’t claim you made it from scratch if you didn’t. Be chill.
