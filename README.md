<p align="center">
  <img src="https://github.com/Qu1nel/Life/blob/main/.github/preview.png" width=580px>
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Python-3.10-blueviolet" alt="Python Version">
   <img src="https://img.shields.io/github/v/release/Qu1nel/Life" alt="Version">
   <img src="https://img.shields.io/github/license/Qu1nel/Life?color=g" alt="License" />
   <img src="https://img.shields.io/github/actions/workflow/status/Qu1nel/Life/pylint_mypy.yml?label=Linting&logo=github" alt="Linting"/>
</p>

## About Life

The game of Life is a cellular automaton written using Python.

## Installation

Clone the repository and run the file **_main.py_**.
Make sure that all [requirements](#requirements) are met.

## Requirements

_The Python interpreter version 3.10+_

All python dependencies specified in the file [requirements.txt](./requirements.txt)

    pip install -r requirements.txt

## Documentation

| Key      | Action        |
| -------- | ------------- |
| \<SPACE> | pause of game |

Pressing the space bar will ensure that the game stops until the next key is pressed.

---

### Flags

#### --debug

If your game crashes and you want to understand why this is happening, or maybe you just want to see the entire
event log, then specify the `--debug` or `-D` flag. This will allow the game to enable internal logging, which will
be saved to the `debug.log` file in the `src/log` directory (generated automatically).

```bash
python ./main.py --debug  # Enable game logging
```

#### --hide-fps

If you want to disable the display of fps in the game in the upper right corner, then use the flag `--hide-fps` or `-H`

```bash
python ./main.py --hide-fps  # Disable showing fps in game
```

## Developers

- [Qu1nel](https://github.com/Qu1nel)

## License

This Project Qu1nel.Life in distributive under the **[MIT License](./LICENSE)**, and it also uses those codes that are
distributed under the **[MIT License](./LICENSE)**.
