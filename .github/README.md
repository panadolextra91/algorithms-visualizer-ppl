# CI/CD Workflows

This repository uses GitHub Actions for continuous integration and deployment.

## Workflows

### 1. **CI Workflow** (`.github/workflows/ci.yml`)
Runs on all pushes and pull requests to `main` and `develop` branches.

**Jobs:**
- **Server Tests**: Validates Python server code
  - Installs dependencies
  - Generates ANTLR parser
  - Checks syntax
  - Tests command parsing
  
- **Client Lint & Type Check**: Validates React Native client code
  - Runs ESLint
  - Type checks with TypeScript

### 2. **Server CI** (`.github/workflows/server-ci.yml`)
Runs only when server files change.

**Triggers:**
- Changes to `server/**`
- Changes to `.github/workflows/server-ci.yml`

### 3. **Client CI** (`.github/workflows/client-ci.yml`)
Runs only when client files change.

**Triggers:**
- Changes to `algorithms-visualizer-client/**`
- Changes to `.github/workflows/client-ci.yml`

## Requirements

### Server
- Python 3.13
- Java (for ANTLR parser generation)
- Dependencies from `server/requirements.txt`

### Client
- Node.js 20
- npm dependencies from `algorithms-visualizer-client/package.json`

## Viewing Workflow Results

1. Go to the **Actions** tab in your GitHub repository
2. Click on a workflow run to see detailed results
3. Expand each job to see step-by-step output

## Adding New Checks

To add new checks:

1. **Server**: Add steps to `.github/workflows/server-ci.yml` or `.github/workflows/ci.yml`
2. **Client**: Add steps to `.github/workflows/client-ci.yml` or `.github/workflows/ci.yml`

## Workflow Status Badge

Add this to your README.md to show CI status:

```markdown
![CI](https://github.com/panadolextra91/algorithms-visualizer-ppl/workflows/CI/badge.svg)
```
