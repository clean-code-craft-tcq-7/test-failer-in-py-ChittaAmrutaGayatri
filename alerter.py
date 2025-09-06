# alerter.py
alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    return 200

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0


# ===== Strengthened failing test =====
def test_alert_failure_count_when_network_fails():
    """Simulate a network failure and expect failure counter to increment."""
    global network_alert_stub, alert_failure_count
    original_stub = network_alert_stub
    try:
        def failing_stub(c):
            print(f'ALERT: Temperature is {c} celcius')
            return 500  # simulate failure
        network_alert_stub = failing_stub
        alert_failure_count = 0
        alert_in_celcius(400)  # definitely calls the stub
        # This should be 1, but the buggy code adds 0 -> test must FAIL
        assert alert_failure_count == 1
    finally:
        network_alert_stub = original_stub


if __name__ == "__main__":
    test_alert_failure_count_when_network_fails()
    print("All is well (maybe!)")
