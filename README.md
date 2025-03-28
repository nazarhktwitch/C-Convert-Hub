# C-Convert-Hub  

![](demo.gif)

**⚠️ BETA WARNING:** This is experimental software. Always verify converted code - some edge cases may require manual adjustments.

## What's This?

A no-nonsense GUI tool that actually understands how to convert between:  
- C ↔ C++ (goodbye, prehistoric structs!)
- C++ ↔ C# (without butchering your logic)
- C ↔ C# (black magic included)

Runs smooth, won't melt your CPU, and looks decent (dark mode FTW).  

## Why Bother?

✔ **Preserves comments** (unlike your last intern)
✔ **Smart OOP conversion** (structs → classes with actual methods)
✔ **No Java-style atrocities** (we respect your code)
✔ **Actually usable UI** (not another terminal nightmare)

## Installation  

### For Normal People (Windows Only):  
1. Grab the [latest release](https://github.com/nazarhktwitch/C-Convert-Hub/releases) (.exe)
2. Open

### For Terminal Warriors:  
```bash
# Linux/macOS
git clone https://github.com/nazarhktwitch/C-Convert-Hub.git
cd C-Convert-Hub
pip install PyQt6
python3 main.py

# Windows (yes, it works)
python -m pip install PyQt6
python main.py
```

## How It Works  
1. **File → Open** (Ctrl+O)
2. Pick languages (C→C++ etc.)
3. Hit **Convert**
4. Watch magic happen
5. **File → Save** (Ctrl+S) - because we're not animals

## Real Example

**Before (C):**
```c
void print_user(User* u) {
    printf("User %d: %s\n", u->id, u->name);
}
```

**After (C++):**

```cpp
void User::print() const {
    std::cout << "User " << id << ": " << name << "\n";
}
```

---

**Warning:** May cause sudden urge to refactor old code. Not responsible for lost productivity.  

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
