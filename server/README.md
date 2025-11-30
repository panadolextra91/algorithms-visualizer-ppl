# Algorithms Visualizer Server

Run locally:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn server.main:app --reload
```

Example request:

```bash
curl -X POST http://localhost:8000/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user12345","command":"visualize bubble sort on [5, 2, 8, 1, 9]"}'
```

Then call `next` to advance:

```bash
curl -X POST http://localhost:8000/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user12345","command":"next"}'
```

Supported sorting algorithms:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

Menu-driven command flow:

1. `menu` – show top-level categories. Use `sorting` or `1` to enter the sorting menu.
2. Select an algorithm via name or number (e.g., `bubble`, `5`, `quick sort`).
3. Enter the input array as comma-separated integers, for example `5, 2, 8, 1`.
4. Use `next` to advance, `explain` for complexity, and `reset` to start over.
5. Legacy shortcut `visualize bubble sort on [5, 2, 8]` still works if you prefer the old single-command style.

Generating ANTLR parser (optional for now):

```bash
# Ensure Java is installed. The ANTLR jar is at server/antlr4-4.9.2-complete.jar
make -C server generate
```

This generates Python parser/lexer code into `server/parser` using `server/grammar/AlgoDSL.g4`.


