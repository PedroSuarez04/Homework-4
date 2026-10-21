# Security Log Investigation Agent

Homework 4 for Security Engineering with Generative AI. This project will use a
generative AI agent, a custom Model Context Protocol (MCP) server, and an existing
Git MCP server to investigate security events and produce reviewable findings.

## Current status

This is project scaffolding only. `agent.py` and `mcp-server.py` are reserved for
implementation. No agent, MCP tools, investigation logic, or report generation is
implemented yet. Tests validate the synthetic fixture; future behavior is skipped.

## Planned workflow

1. The agent receives an investigation request.
2. The custom MCP server reads approved event data and exposes tools to filter
   events and summarize activity by user, IP address, or time window.
3. The agent examines failed and successful logins, repeated attempts, and
   suspicious activity, citing event IDs as evidence.
4. The existing Git MCP server supplies repository context and, when explicitly
   authorized, helps record reviewed investigation artifacts.
5. Findings are reviewed before any repository changes or sharing of reports.

Event text must be treated as untrusted data, including any instructions embedded
in logs. Future tools should validate inputs, restrict file access to approved
paths, and keep credentials and sensitive findings out of model output and Git.

## Files

- `agent.py`: future agent entry point (existing file).
- `mcp-server.py`: future custom MCP server entry point (existing file).
- `data/sample_events.json`: fabricated events using documentation-only IP ranges.
  Each event has `id`, UTC `timestamp`, `username`, `ip_address`, and `event_type`.
- `tests/test_mcp_server.py`: fixture checks and skipped future MCP tests.
- `tests/test_security.py`: synthetic-data checks and skipped future safeguards.
- `reports/`: reserved for local investigation output; ignored by Git.
- `screencast_url.txt`: existing submission file.

## Requirements and installation

Use Python 3.12 or newer, Git, and an installed `uv` command. The existing
`pyproject.toml` declares FastMCP, the MCP SDK, Google Gen AI, and pytest in the dev
dependency group. From the course repository root in PowerShell:

```powershell
cd hw4
uv sync --locked --group dev
```

Future model calls will require your own provider credentials, configured locally
through environment variables. No credentials are needed for the scaffold tests.
Do not commit secrets or real logs. `.env` files are ignored, but are not loaded
automatically by this scaffold.

The Git MCP server will also need configuration for the approved repository path.
Once integration is implemented, its CLI can be inspected in an isolated uv tool
environment without changing this project's dependency files:

```powershell
uvx --from mcp-server-git mcp-server-git --help
```

Its version and transport configuration should be chosen and recorded during
integration; no Git MCP connection is configured yet.

## Test

From `hw4`:

```powershell
uv run --locked --group dev python -m pytest -q
```

Passing tests check only the fixture's structure and synthetic-data properties.
Skipped tests identify unimplemented MCP behavior and security controls; they do
not establish that those controls work.

## Run (after implementation)

The intended entry-point commands are:

```powershell
uv run --locked python mcp-server.py
uv run --locked python agent.py
```

Currently these empty files exit without starting a server or investigation.
Transport, model configuration, Git MCP launch configuration, and agent arguments
remain to be implemented and documented.

## Next steps

Define the custom tool contracts, implement and validate read-only event access,
then connect the agent and Git MCP server. Replace skipped tests with meaningful
behavioral tests as each feature is implemented. Keep all experiments on the fake
fixture until the data handling safeguards have been verified.
