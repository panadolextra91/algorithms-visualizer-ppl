# Algorithms Visualizer Server

## Configuration

Server configuration is stored in `.env` file:

```bash
PORT=8069
HOST=0.0.0.0
```

Edit `.env` to change the port or host.

## Run locally:

### Option 1: Using the run script (recommended)
```bash
conda activate base
pip install -r requirements.txt
python run_server.py  # Use 'python' not 'python3' when conda is activated
```

### Option 2: Using uvicorn directly
```bash
conda activate base
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8069
```

Example request:

```bash
curl -X POST http://localhost:8069/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user12345","command":"visualize bubble sort on [5, 2, 8, 1, 9]"}'
```

Then call `next` to advance:

```bash
curl -X POST http://localhost:8069/command \
  -H 'Content-Type: application/json' \
  -d '{"sessionId":"user12345","command":"next"}'
```

Generating ANTLR parser (optional for now):

```bash
# Ensure Java is installed. The ANTLR jar is at server/antlr4-4.9.2-complete.jar
make -C server generate
```

This generates Python parser/lexer code into `server/parser` using `server/grammar/AlgoDSL.g4`.


