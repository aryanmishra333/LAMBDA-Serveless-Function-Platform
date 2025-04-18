import pytest
from backend.core.docker_executor import calculate_cpu_percent

def test_calculate_cpu_percent():
    # Test with valid stats
    stats = {
        'cpu_stats': {
            'cpu_usage': {'total_usage': 1000000000},
            'system_cpu_usage': 2000000000,
            'online_cpus': 2
        }
    }
    assert calculate_cpu_percent(stats) == 100.0

    # Test with zero usage
    stats = {
        'cpu_stats': {
            'cpu_usage': {'total_usage': 0},
            'system_cpu_usage': 1000000000,
            'online_cpus': 2
        }
    }
    assert calculate_cpu_percent(stats) == 0.0

    # Test with missing stats
    stats = {}
    assert calculate_cpu_percent(stats) == 0.0 