# 🎮 Mastermind — Stanford Code in Place (CS106A) Final Project

This project is a full graphical implementation of **Mastermind**, created as my final project for **Stanford Code in Place (CS106A) 2023**. It was my first experience building a larger, interactive program, and it became a foundational milestone in my programming journey.

The game is implemented entirely using the **Canvas** graphics library provided by the course. Every peg, every click, and every feedback indicator is drawn manually on the screen using coordinate logic, shapes, and event-based interactions.

---

## 📌 Project Overview

Mastermind is a classic two-player code-breaking game. In this version, the computer generates a secret sequence of four colored pegs, and the player must guess the correct combination within eight attempts. After each guess, the game provides feedback using the small “feedback pegs” on the right side:

- 🟢 **Green** — Correct color in the correct position  
- 🟡 **Yellow** — Correct color in the wrong position  
- 🔴 **Red** — Color not in the code at all  

The player interacts with the game entirely through **mouse clicks**, selecting colors from a palette and placing guesses visually onto the board.

---

## 🎨 Features

### 🖱️ Mouse-Driven Interaction
- No text input.
- Every move is determined by clicking on drawn shapes.
- Click detection uses Canvas's `get_last_click()` and hit-testing with `find_overlapping()`.

### 🎯 Visual Game Board
The interface includes:
- A top **color palette** (Teal, Magenta, Lime, Blue, Pink, Orange)
- Eight **rows of guess slots**
- Four **feedback slots** per row
- A dynamically drawn interface updated on each guess

### 🧠 Game Logic
The game uses:
- Random secret code generation
- One-hot lists for representing each color  
  (e.g., `master_pegs_0`, `user_pegs_3`, etc.)
- Sorted lists for determining color correctness
- Positional comparison for exact matches
- A feedback algorithm that produces four pegs per guess

While verbose, this logic reflects my early approach to problem-solving and demonstrates how I learned to translate rules into step-by-step procedures.

---

## 🧩 How the Game Works (Internally)

### 🎲 Secret Code Generation
The computer picks 4 random colors from the available 6.  
These are stored as numeric indices (0–5), but also generate one-hot vectors to help with comparison.

### 🎨 Drawing Functions
Three helper functions draw elements on the board:
- `draw_peg()` — main colored guess circles  
- `draw_feedback_peg()` — small red/yellow/green pegs  
- `draw_guess_number()` — (unused) text helper  

### 🟡 Feedback Algorithm
For each guess:
1. **Color match check**:  
   Uses sorted one-hot vectors to count how many colors appear in both the guess and the secret.
2. **Position match check**:  
   Compares each slot index directly for exact matches.
3. **Feedback array**:  
   Builds a list of 4 values:  
   - `2` → Green  
   - `1` → Yellow  
   - `0` → Red  
4. **Sort feedback** so greens appear first, then yellows, then reds.

The logic is intentionally straightforward and procedural—reflecting the programming level expected in Code in Place.

---

## 🚀 Running the Project

This program runs inside the **Stanford Code in Place online IDE**, which includes:
- The `canvas` graphics library
- Built-in event loop for click handling  
- Display window for drawing shapes

To run it locally, you would need:
- Python  
- A compatible Canvas implementation or an equivalent graphics wrapper (which I couldn't find any)
(because Canvas is not the same as Tkinter)

For most users, the easiest way is simply running it in the original CIP environment.
- Go to CIP public self-guided course: 
https://codeinplace.stanford.edu/public/studenthome
- Create an account
- Go to Code -> Your Own
- Create a New Graphics Project
- Copy & paste mastermind.py
- Run and/or share the project


---

## 📂 File Structure

This project consists of **a single Python file**, containing:
- All drawing functions  
- All game logic  
- All click-handling logic  
- The main event loop  
- The Mastermind rules and gameplay flow

Although today I would break this into modules, classes, and smaller functions, the single-file format was ideal for Code in Place and reflects the learning goals of CS106A.

---

## 📝 Reflections

This was the first large program I ever wrote. It taught me:

- How to think in terms of *states* and *events*  
- How to structure a longer program  
- How to manipulate graphics using coordinates  
- How to debug interactive behavior  
- How to implement a real game from scratch  

Looking back with more experience, I see many places I would refactor or simplify—but that is exactly what makes this project important. It marks the moment I began thinking like a programmer.

---

## 🧵 Part of a Learning Journey

This project is the **first article** in my series documenting key milestone projects from:

- Stanford Code in Place (CS106A)  
- Harvard CS50P  
- University of Michigan (SI206, SI364)  
- Google Data Analytics  
- Kaggle x Google: Generative AI Intensive  
- And my current work as a Data Scientist / Full Stack Developer  

Each project shows how far I’ve come and how every step built toward the next.

---

## 🔗 Links

**Full Project:**  
https://codeinplace.stanford.edu/cip3/share/I7bsgEQPpWdXBGMZ9TCd

**Related Medium Article:**  
_From Stanford Code in Place (CS106A) to Harvard CS50P — My First Real Project: Re-Creating Mastermind_  
https://medium.com/@barissoy/from-stanford-code-in-place-cs106a-to-harvard-cs50p-my-first-real-project-re-creating-62fd385286fa

---

## 📜 License

This project was created for educational purposes as part of the Stanford Code in Place program.  
All code is free to read, modify, and learn from.

---
