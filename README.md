# 🎮 AI Dungeon Game (Python + BFS + Genetic Algorithm)

An intelligent dungeon game built using **Python and Pygame**, featuring **AI-powered enemy movement**, **procedural map generation**, and **interactive UI with difficulty selection**.

---

## 🚀 Overview

This project combines **Game Development + Artificial Intelligence concepts** to create a dynamic dungeon environment where:

* 🧠 The **enemy uses BFS (Breadth-First Search)** to chase the player
* 🧬 Maps are generated using a **Genetic Algorithm (GA)**
* 🎯 Players can choose difficulty levels before starting
* 🔁 Player has a special **wrap-around ability** (edge teleport)
* 🟡 Enemy follows realistic constraints (no teleport, respects walls)

---

## 🎯 Features

### 🤖 AI Enemy System

* Uses **Breadth-First Search (BFS)** for shortest path finding
* Dynamically tracks player position
* Difficulty affects enemy speed

---

### 🧬 Procedural Map Generation

* Maps generated using **Genetic Algorithm**
* Fitness based on:

  * Solvability
  * Path length (complexity)
* Avoids impossible or trivial maps

---

### 🎮 Gameplay Mechanics

* Player starts at **S (Start)**
* Goal is to reach **E (End)**
* Avoid enemy (🟡)
* Walls (#) block movement

---

### 🔁 Unique Player Ability

* Player can **wrap around edges**

  * Left → Right
  * Top → Bottom
* Adds strategic gameplay advantage

---

### 🎯 Difficulty System

| Level  | Enemy Speed | Experience         |
| ------ | ----------- | ------------------ |
| Easy   | Slow        | Beginner-friendly  |
| Medium | Balanced    | Moderate challenge |
| Hard   | Fast        | Intense gameplay   |

---

### 🎨 UI System

* Interactive buttons:

  * Start Game
  * Difficulty Selection
  * Restart
* Hover effects
* Clean layout with step counter
* Win / Lose screens

---

## 🧠 Algorithms Used

### 1. Breadth-First Search (BFS)

* Used for enemy pathfinding
* Guarantees shortest path
* Implemented using queue (FIFO)

---

### 2. Genetic Algorithm (GA)

* Population-based map generation
* Includes:

  * Selection
  * Crossover
  * Mutation
* Fitness = path length (via BFS solver)

---

## 📁 Project Structure

```bash
AI-Dungeon-Game/
│
├── main.py        # Game loop + UI + logic
├── enemy.py       # BFS enemy movement
├── solver.py      # BFS path solver (fitness)
├── ga.py          # Genetic Algorithm for map generation
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Dungeon-Game.git
cd AI-Dungeon-Game
```

### 2️⃣ Install Dependencies

```bash
pip install pygame
```

---

## ▶️ Run the Game

```bash
python main.py
```

---

## 🎮 Controls

| Key         | Action         |
| ----------- | -------------- |
| ⬆️ ⬇️ ⬅️ ➡️ | Move Player    |
| 🖱️ Mouse   | UI Interaction |

---

## 🏆 Game Rules

* Reach the goal before enemy catches you
* Avoid walls
* Use wrap-around strategically
* Higher difficulty = faster enemy

---

## 📸 Screenshots

> *(Add your screenshots here for better presentation)*
> <img width="881" height="765" alt="Screenshot 2026-03-18 233809" src="https://github.com/user-attachments/assets/a4cd23eb-b22c-4804-9de7-7b6c8205a5de" />
> <img width="446" height="471" alt="image" src="https://github.com/user-attachments/assets/afa1b1b6-569f-4572-9699-d05cb493d4a2" />


---

## 🔥 Future Improvements

* 🎵 Sound effects & background music
* 🎬 Animations & transitions
* 🧠 Smarter enemy AI (prediction-based)
* 🌍 Larger dynamic maps
* 💾 Save/load game state
* 📱 Mobile version (Jetpack Compose)

---

## 💡 Learning Outcomes

* Game development using **Pygame**
* AI pathfinding (BFS)
* Optimization using **Genetic Algorithms**
* UI/UX design in games
* State management in real-time systems

---

## 👨‍💻 Author

**Your Name**

* GitHub: https://github.com/YOUR_USERNAME

---

## ⭐ Contribute

Feel free to fork this repo and improve:

* AI behavior
* UI/UX
* Performance

Pull requests are welcome!

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

🔥 *Built as a fusion of AI + Game Development for learning and experimentation.*
