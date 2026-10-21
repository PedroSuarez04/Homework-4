"""Check fake-data boundaries and explicitly defer unimplemented safeguards."""

import ipaddress
import json
from pathlib import Path

import pytest


def test_fixture_uses_documentation_ips_and_expected_activity() -> None:
    """Fixture addresses must stay in reserved IPv4 documentation ranges."""
    path = Path(__file__).resolve().parents[1] / "data" / "sample_events.json"
    events = json.loads(path.read_text(encoding="utf-8"))
    documentation_networks = tuple(
        ipaddress.ip_network(cidr)
        for cidr in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24")
    )
    for event in events:
        address = ipaddress.ip_address(event["ip_address"])
        assert any(address in network for network in documentation_networks)
    assert {"login_success", "login_failure", "suspicious_ip_activity", "file_access"} <= {
        event["event_type"] for event in events
    }


@pytest.mark.skip(reason="MCP input and file-access validation are not implemented yet.")
def test_tools_reject_path_traversal_and_invalid_inputs() -> None:
    """Pending: reject paths outside approved data and malformed tool arguments."""


@pytest.mark.skip(reason="Agent and report handling are not implemented yet.")
def test_untrusted_events_cannot_trigger_actions_or_leak_secrets() -> None:
    """Pending: exercise log injection and secret redaction through the real pipeline."""
