<div align="center">
  <img src=".github/assets/logo.png" alt="logo" width="200px" height="auto" />
  <h1>Cellular Automaton</h1>

  <p>The Game of Life is a cellular automaton. </p>

<!-- Badges -->
<p>
  <a href="https://github.com/Qu1nel/CellularAutomaton/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Qu1nel/CellularAutomaton" alt="contributors" />
  </a>
  <a href="https://github.com/Qu1nel/CellularAutomaton/commits/main">
    <img src="https://img.shields.io/github/last-commit/Qu1nel/CellularAutomaton" alt="last update" />
  </a>
  <a href="https://github.com/Qu1nel/CellularAutomaton/network/members">
    <img src="https://img.shields.io/github/forks/Qu1nel/CellularAutomaton" alt="forks" />
  </a>
  <a href="https://github.com/Qu1nel/CellularAutomaton/stargazers">
    <img src="https://img.shields.io/github/stars/Qu1nel/CellularAutomaton" alt="stars" />
  </a>
  <a href="https://github.com/Qu1nel/CellularAutomaton/issues/">
    <img src="https://img.shields.io/github/issues/Qu1nel/CellularAutomaton" alt="open issues" />
  </a>
</p>

<p>
  <a href="https://www.python.org/downloads/release/python-3110/" >
    <img src="https://img.shields.io/badge/Python-3.11%2B-blueviolet" alt="python Version" />
  <a>
  <a href="https://github.com/Qu1nel/CellularAutomaton/releases/">
    <img src="https://img.shields.io/github/v/release/Qu1nel/CellularAutomaton" alt="project version" />
  <a>
  <a href="https://github.com/Qu1nel/CellularAutomaton/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Qu1nel/CellularAutomaton?color=g" alt="license" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/actions/workflow/status/Qu1nel/CellularAutomaton/python_linting.yml" alt="linting" />
  </a>
</p>

<h4>
  <a href="#view-demo">View Demo</a>
  <span> · </span>
  <a href="#documentation">Documentation</a>
  <span> · </span>
  <a href="https://github.com/Qu1nel/CellularAutomaton/issues/">Report Bug</a>
  <span> · </span>
  <a href="https://github.com/Qu1nel/CellularAutomaton/issues/">Request Feature</a>
</h4>
</div>

<br />

<!-- Table of Contents -->

# Contents

- [About the Project](#about-cellular-automaton)
  - [Screenshots](#screenshots)
- [Installation](#installation)
  - [Requirements](#requirements)
- [Getting started](#getting-started)
  - [Windows](#windows)
  - [Linux](#linux)
- [Documentation](#documentation)
- [Flags](#flags)
- [Developers](#developers)
- [License](#license)

## About Cellular Automaton

Cellular Automaton - a simple interactive game Life for a visual representation of what it is.

<details>
  <summary><h3 id="screenshots">Screenshots</h3></summary>
  <div align="center">
    <img src=".github/assets/preview1.png" width=580px>
    <img src=".github/assets/preview2.png" width=580px>
  </div>
</details>

## Installation

Clone the repository, install all requirements and run the file `run.py`.

### Requirements

_The [`Python`](https://www.python.org/downloads/) interpreter version 3.11+ and preferably [`poetry`](https://python-poetry.org/)_

Install requirements with `poetry`:

```bash
poetry install
```

## Getting started

Clone this repository and navigate to it with the command:

```bash
git clone https://github.com/Qu1nel/CellularAutomaton.git
cd CellularAutomaton/
```

If you have the `make` and `poetry` installed, you can run the game with the command:

```bash
make run
```

Or

```bash
poetry run python run.py
```

Or you can simply run `run.py` using the python interpreter

#### Windows

```powershell
python run.py
```

#### Linux

```bash
python3 run.py
```

## Documentation

For full help with make commands, you can use the command:

```bash
make help
```


| Key      | Action        |
|----------|---------------|
| \<SPACE> | pause of game |

Pressing the space bar will ensure that the game stops until the next key is pressed.


Also in the game it is possible to change the neighborhood calculation mode for a cell (number of counted neighbors) to **"Moore neighborhood"** and **"Neumann neighborhood"**.

This can be done using two buttons on the screen, which can be minimized at will.


### Flags

#### --logging

If your game crashes and you want to understand why this is happening, or maybe you just want to see the entire
event log, then specify the `--logging` or `-L` flag. This will allow the game to enable internal logging, which will
be saved to the `debug.log` file in the `src/log` directory (generated automatically).

```bash
python run.py --logging  # Enable game logging
```

#### --hide-fps

If you want to disable the display of fps in the game in the upper right corner, then use the flag `--hide-fps` or `-H`

```bash
python run.py --hide-fps  # Disable showing fps in game
```

#### --Moore

If you want to explicitly (because this parameter is set by default) enable the so-called Moore neighborhood that counts all 8 cell neighbors, use `--Moore` or `-M` flags.

```bash
python run.py --Moore
```

#### --Neumann

If you want to include the so-called Neumann neighborhood that allows the game to count only 4 neighbors for a cell, use `--Neumann` or `-N` flags.

```bash
python run.py --Neumann
```

## Developers

- [Qu1nel](https://github.com/Qu1nel)

## License

[MIT](./LICENSE) © [Ivan Kovach](https://github.com/Qu1nel/)
