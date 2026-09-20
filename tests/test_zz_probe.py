"""Probe-only: a deliberately failing test, to observe what the
"Tests successful" gate job reports when the matrix fails."""


def test_probe_deliberate_failure() -> None:
    assert 1 == 2, "probe: deliberate failure"
