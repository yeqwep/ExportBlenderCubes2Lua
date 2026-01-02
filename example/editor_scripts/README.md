# Blender Cube Lua → Defold Collision GameObject Generator

This Defold **Editor Script** creates **GameObjects with collision objects**
from a Lua table exported by a Blender add-on.

About Editor Scripts
https://defold.com/manuals/editor-scripts/

---

## What This Editor Script Does

* Reads a Lua table containing Blender Cube data
* Creates Defold GameObjects (`.go`)
* Adds a **static box collision object** to the GameObject
* Writes the result directly into the project as assets

This script runs **inside the Defold Editor**, not at runtime.

---

## How to Use (Editor Script)

1. In the **Assets** panel, right-click a Cube Lua table file

2. Click
   **Create collision from Blender Cubes**

3. If a GameObject with the same name already exists in the same folder,
   an overwrite confirmation dialog will appear

4. Click **Overwrite it** to proceed

5. A GameObject with a collision object will be created

---
## Notes

* Existing files are never overwritten without confirmation
* This tool is intended for **blockout, collision, and level layout**
* Visual components (models, sprites) can be added later