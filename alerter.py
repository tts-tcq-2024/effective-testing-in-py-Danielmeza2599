# Daniel Meza
# Jr Embedded Software Developer
# Alerter.py

alert_failure_count = 0


#The network_alert_stub function is modified to return 500 in some cases, 
# which should increase the failure counter.
#a test was added to verify that the counter is incremented correctly.
def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    ####return 200
    # Simulate a failure if temperature is above 100°C
    return 500 if celcius > 100 else 200


def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0  ## Bug: should be += 1


alert_in_celcius(400.5) # Should increment alert_failure_count
alert_in_celcius(303.6) # Should increment alert_failure_count
print(f'{alert_failure_count} alerts failed.')
assert(alert_failure_count == 2)  # This should fail because the count is not incremented
print('All is well (maybe!)')

#Alerter.py: The test will fail because the failure counter is not incremented correctly.
